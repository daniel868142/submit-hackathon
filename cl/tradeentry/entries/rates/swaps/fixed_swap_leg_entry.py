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
from cl.runtime import Context
from cl.runtime.records.dataclasses_extensions import missing
from cl.convince.entries.entry_key import EntryKey
from cl.convince.llms.gpt.gpt_llm import GptLlm
from cl.convince.retrievers.annotating_retriever import AnnotatingRetriever
from cl.tradeentry.entries.fixed_rate_entry import FixedRateEntry
from cl.tradeentry.entries.pay_freq_entry import PayFreqEntry
from cl.tradeentry.entries.pay_receive_fixed_entry import PayReceiveFixedEntry
from cl.tradeentry.entries.rates.swaps.rates_swap_leg_entry import RatesSwapLegEntry

_SIDE = """The words Buy or Sell, or the words Pay or Receive, or an indication who pays or receives such as
'Bank pays', 'Bank receives', 'We pay', 'We receive', 'Client pays', 'Client receives', etc.
"""
_FIXED_RATE = "Fixed rate"
_PAY_FREQ = "Payment frequency"


@dataclass(slots=True, kw_only=True)
class FixedSwapLegEntry(RatesSwapLegEntry):
    """A series of interest rate payments with fixed coupon."""

    fixed_rate: EntryKey | None = None
    """Fixed rate entry."""

    def run_generate(self) -> None:
        """Retrieve parameters from this entry and save the resulting entries."""

        # Reset before regenerating to prevent stale field values
        self.run_reset()

        # Get retriever
        # TODO: Make configurable
        retriever = AnnotatingRetriever(
            retriever_id="test_annotating_retriever",
        )
        retriever.init_all()

        # Process fields
        context = Context.current()
        input_text = self.get_text()

        # Pay or receive flag
        if pay_receive_description := retriever.retrieve(
            input_text=input_text, param_description=_SIDE, is_required=False
        ):
            pay_receive = PayReceiveFixedEntry(text=pay_receive_description)
            context.save_one(pay_receive)
            self.pay_receive = pay_receive.get_key()

        # Fixed Rate
        if fixed_rate_description := retriever.retrieve(
            input_text=input_text, param_description=_FIXED_RATE, is_required=False
        ):
            fixed_rate = FixedRateEntry(text=fixed_rate_description)
            context.save_one(fixed_rate)
            self.fixed_rate = fixed_rate.get_key()

        # Payment Frequency
        if pay_freq_description := retriever.retrieve(
            input_text=input_text, param_description=_PAY_FREQ, is_required=False
        ):
            pay_freq = PayFreqEntry(text=pay_freq_description)
            context.save_one(pay_freq)
            self.pay_freq = pay_freq.get_key()

        # Save self to DB
        Context.current().save_one(self)
