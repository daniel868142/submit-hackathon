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

from dataclasses import dataclass
from typing import List
from cl.runtime.records.dataclasses_extensions import field
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.schema.handler_param_decl import HandlerParamDecl
from cl.runtime.schema.handler_type import HandlerType
from cl.runtime.schema.handler_variable_decl import HandlerVariableDecl


@dataclass(slots=True, kw_only=True)
class HandlerDeclareDecl:
    """Handler declaration data."""

    name: str = missing()
    """Handler name."""

    label: str | None = missing()
    """Handler label."""

    comment: str | None = missing()
    """Handler comment."""

    type_: HandlerType = field(name="Type")
    """Handler type."""

    params: List[HandlerParamDecl] | None = missing()
    """Handler parameters."""

    return_: HandlerVariableDecl | None = field(name="Return")  # TODO: Remove trailing _ automatically
    """Handler return value."""

    static: bool | None = missing()
    """If set as true, handler will be static, otherwise non-static."""
