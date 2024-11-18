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

import inspect
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import List
from typing_extensions import Self
from cl.runtime import ClassInfo
from cl.runtime.context.context import Context
from cl.runtime.primitive.case_util import CaseUtil
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.records.protocols import KeyProtocol
from cl.runtime.schema.schema import Schema
from cl.runtime.serialization.dict_serializer import DictSerializer
from cl.runtime.serialization.string_serializer import StringSerializer
from cl.runtime.tasks.callable_task import CallableTask
from cl.runtime.tasks.task_key import TaskKey
from cl.runtime.tasks.task_queue_key import TaskQueueKey

key_serializer = StringSerializer()
param_dict_serializer = DictSerializer()  # TODO: Support complex params


@dataclass(slots=True, kw_only=True)
class InstanceMethodTask(CallableTask):
    """Invoke a class instance method, do not use for @classmethod or @staticmethod."""

    key_type_str: str = missing()
    """Key type as dot-delimited string in module.ClassNameKey format inclusive of Key suffix if present."""

    key_str: str = missing()
    """Key as semicolon-delimited string."""

    method_name: str = missing()
    """The name of instance method in snake_case or PascalCase format, do not use for @classmethod or @staticmethod."""

    method_params: List[str] | None = None
    """Optional list of method parameters."""

    def _execute(self) -> None:
        """Invoke the specified instance method."""

        # Get current context
        context = Context.current()

        # Save self to ensure the worker process loads the same record
        context.save_one(self)

        key_type = ClassInfo.get_class_type(self.key_type_str)
        key = key_serializer.deserialize_key(self.key_str, key_type)

        # Load record from storage
        record = context.load_one(key_type, key)  # TODO: Require record type?

        # Convert the name to snake_case and get method callable
        method_name = self.normalize_method_name(self.method_name)
        method = getattr(record, method_name)

        # Invoke the callable
        if self.method_params:
            method(*self.method_params)
        else:
            method()

    @classmethod
    def create(
        cls,
        *,
        queue: TaskQueueKey,
        record_or_key: KeyProtocol | None = None,
        method_callable: Callable,
    ) -> Self:
        """
        Create from the record or its key and an instance-bound or class-bound method callable.

        Notes:
            - The key is required if the callable is for a class rather than an instance.

        Args:
            queue: Queue that will run the task
            record_or_key: Record or its key
            method_callable: Callable bound to a class (ClassName.method_name) or its instance (obj.method_name)
        """

        # Populate known fields
        result = cls(queue=queue)

        # Get key type and key
        key_type = record_or_key.get_key_type()
        result.key_type_str = f"{key_type.__module__}.{key_type.__name__}"
        result.key_str = key_serializer.serialize_key(record_or_key)

        # Two tokens because the callable is bound to a class or its instance
        method_tokens = method_callable.__qualname__.split(".")
        if len(method_tokens) == 2:
            # Second token is method name
            result.method_name = method_tokens[1]
        else:
            raise RuntimeError(
                f"Callable '{method_callable.__qualname__}' for task_id='{result.task_id}' does not "
                f"have two dot-delimited tokens indicating it is not a method bound to a class."
            )

        # Set label and return
        method_name_pascal_case = CaseUtil.snake_to_pascal_case(result.method_name)
        result.label = f"{key_type.__name__};{result.key_str};{method_name_pascal_case}"
        return result
