# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import dataclasses
from typing import Any
from typing import Dict
from typing import List
from pydantic import BaseModel
from pydantic import Field
from cl.runtime import Context
from cl.runtime.backend.core.ui_app_state import UiAppState
from cl.runtime.backend.core.ui_app_state_key import UiAppStateKey
from cl.runtime.backend.core.ui_type_state import UiTypeState
from cl.runtime.backend.core.ui_type_state_key import UiTypeStateKey
from cl.runtime.backend.core.user_key import UserKey
from cl.runtime.primitive.case_util import CaseUtil
from cl.runtime.records.class_info import ClassInfo
from cl.runtime.routers.schema.type_request import TypeRequest
from cl.runtime.routers.schema.type_response_util import TypeResponseUtil
from cl.runtime.routers.storage.record_request import RecordRequest
from cl.runtime.schema.field_decl import primitive_types  # TODO: Move definition to a separate module
from cl.runtime.schema.module_decl_key import ModuleDeclKey
from cl.runtime.schema.schema import Schema
from cl.runtime.schema.type_decl_key import TypeDeclKey
from cl.runtime.serialization.string_serializer import StringSerializer
from cl.runtime.serialization.ui_dict_serializer import UiDictSerializer

RecordResponseSchema = Dict[str, Any]
RecordResponseData = Dict[str, Any]


def to_record_dict(node):  # TODO: Apply type hints
    """Recursively apply record dictionary conventions to the argument dictionary."""

    node_type = type(node)
    if node_type in primitive_types:
        # Primitive type, serialize as string
        # TODO: Apply custom formatting
        result = str(node)
        return result
    elif node_type is list:
        # TODO: !!! Generally should not skip nodes that have the value of None
        return [to_record_dict(v) for v in node if v is not None]
    elif node_type is tuple:
        # TODO: Decision on short alias
        # Tuple key, remove Key suffix from key type to obtain table name
        table = node[0].__name__
        result = ";".join([table] + node[1:])
        return result
    elif node_type.__name__.endswith("Key"):
        # Key type, use semicolon-delimited serialization
        # TODO: Do not use a method from dataclasses
        node_dict = dataclasses.asdict(node)
        result = ";".join(node_dict.keys())
        return result
    elif hasattr(node, "get_key"):
        # Data or record
        # TODO: Do not use a method from dataclasses
        node_dict = dataclasses.asdict(node)
        node_dict = {k: getattr(node, k) for k in node_dict.keys()}
        result = {k: to_record_dict(v) for k, v in node_dict.items() if v is not None}
        return result
    else:
        return node


def to_legacy_dict(node: Dict[str, Any] | List[Dict[str, Any]] | str) -> Dict[str, Any] | List[Dict[str, Any]] | str:
    """Recursively apply record dictionary conventions to the argument dictionary."""

    if isinstance(node, dict):
        # Skip nodes that have the value of None
        # Remove suffix _ from field names if present
        result = {
            CaseUtil.snake_to_pascal_case(k.removesuffix("_")): to_legacy_dict(v)
            for k, v in node.items()
            if v is not None
        }
        return result
    elif isinstance(node, list):
        # Skip nodes that have the value of None
        return [to_legacy_dict(v) for v in node if v is not None]
    elif isinstance(node, tuple):
        # TODO: Decision on short alias
        # Generic key, remove Key suffix from key type to obtain table name
        table = node[0].__name__
        result = ";".join([table] + node[1:])
        return result
    else:
        return node


class RecordResponse(BaseModel):
    """Response data type for the /storage/record route."""

    schema_: RecordResponseSchema = Field(..., alias="schema")
    """Schema field of the response data type for the /storage/record route."""

    data: RecordResponseData | None
    """Data field of the response data type for the /storage/record route."""

    @classmethod
    def get_record(cls, request: RecordRequest) -> RecordResponse:
        """Implements /storage/record route."""

        if True:  # TODO: ";" not in request.key:
            # TODO: Use after module is specified
            record_type = Schema.get_type_by_short_name(request.type)
        else:
            key_tokens = request.key.split(";")
            key_module = CaseUtil.pascal_to_snake_case(key_tokens[0])
            key_class = key_tokens[1]

            # record_type = Schema.get_type_by_short_name(request.type)
            # TODO: Use after module is specified
            record_type = ClassInfo.get_class_type(f"{key_module}.{key_class}")

        # Get database from the current context
        db = Context.current().db

        # Load record from storage
        key_serializer = StringSerializer()

        # TODO (Roman): UiAppState record request from FE should have key in proper format where user is embedded key
        if record_type == UiAppState and "KEY" not in request.key:
            # TODO: Ensure user is specified in all deployment scenarios instead of using default value
            deserialized_key = UiAppStateKey(user=UserKey(username=request.key or "root"))
        elif record_type == UiTypeState and "KEY" not in request.key:
            # Construct the UiTypeStateKey by parsing the key value
            splitted_key = request.key.split(";")
            type_state_record_module, type_state_record_type_name, *_ = splitted_key
            username = splitted_key[-1] if len(splitted_key) == 3 else None

            deserialized_key = UiTypeStateKey(
                user=UserKey(username=username or "root"),
                type_=TypeDeclKey(
                    name=type_state_record_type_name, module=ModuleDeclKey(module_name=type_state_record_module)
                ),
            )
        else:
            deserialized_key = key_serializer.deserialize_key(request.key, record_type.get_key_type())

        # TODO: Review the use of is_record_optional flag here
        record = db.load_one(record_type, deserialized_key, is_record_optional=True)
        if not record and record_type == UiTypeState:
            # TODO (Yauheni): remove temporary workaround of pinning handlers for all requested types
            type_state_record_type = Schema.get_type_by_short_name(type_state_record_type_name)
            type_state_record_type_schema = Schema.for_type(type_state_record_type)

            # Iterate over type declarations to get all handlers
            all_handlers = []
            for decl_dict in type_state_record_type_schema.values():
                declare_block = decl_dict.get("Declare")
                if not declare_block:
                    continue

                handlers_block = declare_block.get("Handlers")
                if not handlers_block:
                    continue

                all_handlers.extend(
                    [
                        handler_name
                        for handler_decl in handlers_block
                        if (handler_name := handler_decl.get("Name")) not in all_handlers
                    ]
                )

            record = UiTypeState(
                user=deserialized_key.user,
                type_=deserialized_key.type_,
                pinned_handlers=all_handlers,
            )

        # Get type declarations based on the actual record type
        type_decl_dict = (
            TypeResponseUtil.get_type(
                TypeRequest(
                    name=type(record).__name__,
                    module=request.module,
                    user="root",
                ),
            )
            if record is not None
            else dict()
        )  # Handle not found record

        # Serialize record to ui format
        # TODO: Optimize speed
        ui_serializer = UiDictSerializer()
        record_dict_in_legacy_format = ui_serializer.serialize_data(record)

        # TODO: Update to return record_dict after legacy dict format is removed
        return RecordResponse(schema=type_decl_dict, data=record_dict_in_legacy_format)
