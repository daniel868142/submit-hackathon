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
from typing import Type
from cl.convince.entries.entry import Entry
from cl.tradeentry.trades.pay_receive_fixed_key import PayReceiveFixedKey


@dataclass(slots=True, kw_only=True)
class PayReceiveFixedEntry(Entry):
    """User input to determine if we pay or receive fixed leg coupons in a fixed-for-floating swap."""

    pay_receive_fixed: PayReceiveFixedKey | None = None
    """Determines if we pay or receive fixed leg coupons in a fixed-for-floating swap."""

    def get_base_type(self) -> Type:
        return PayReceiveFixedEntry
