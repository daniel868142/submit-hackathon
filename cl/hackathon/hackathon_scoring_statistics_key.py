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
from dataclasses import field
from typing import Type
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.records.key_mixin import KeyMixin
from cl.hackathon.hackathon_solution_key import HackathonSolutionKey


@dataclass(slots=True, kw_only=True)
class HackathonScoringStatisticsKey(KeyMixin):
    """Output fields for a single hackathon trade obtained using the specified solution."""

    solution: HackathonSolutionKey = missing()
    """Solution that generated the output."""

    trade_group: str = missing()
    """Trade group for which trade_id is defined (trade_id is unique within the group)."""

    trade_id: str = missing()
    """Unique trade identifier within the trade group."""

    @classmethod
    def get_key_type(cls) -> Type:
        return HackathonScoringStatisticsKey
