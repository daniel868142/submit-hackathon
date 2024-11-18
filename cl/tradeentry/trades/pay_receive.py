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

from abc import ABC
from dataclasses import dataclass
from cl.runtime.records.record_mixin import RecordMixin
from cl.tradeentry.trades.pay_receive_key import PayReceiveKey


@dataclass(slots=True, kw_only=True)
class PayReceive(PayReceiveKey, RecordMixin[PayReceiveKey], ABC):
    """Determines if we pay or receive payments or periodic coupons for a trade or leg."""

    comment: str | None = None
    """Optional comment."""

    def get_key(self) -> PayReceiveKey:
        return PayReceiveKey(pay_receive_id=self.pay_receive_id)
