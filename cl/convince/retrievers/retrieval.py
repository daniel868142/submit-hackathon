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
from typing_extensions import Self
from cl.runtime import RecordMixin
from cl.runtime.experiments.trial_key import TrialKey
from cl.runtime.primitive.timestamp import Timestamp
from cl.runtime.records.dataclasses_extensions import missing
from cl.convince.retrievers.retrieval_key import RetrievalKey
from cl.convince.retrievers.retriever_key import RetrieverKey


@dataclass(slots=True, kw_only=True)
class Retrieval(RetrievalKey, RecordMixin[RetrievalKey]):  # TODO: Derive from Task
    """Records inputs and results of a retrieval."""

    retriever: RetrieverKey = missing()
    """Retriever which generated this retrieval."""

    trial: TrialKey | None = None
    """Optional trial key when running multiple trials."""

    def get_key(self) -> RetrievalKey:
        return RetrievalKey(retrieval_id=self.retrieval_id)

    def init(self) -> Self:
        """Similar to __init__ but can use fields set after construction, return self to enable method chaining."""
        if self.retrieval_id is None:
            self.retrieval_id = Timestamp.create()

        # Return self to enable method chaining
        return self
