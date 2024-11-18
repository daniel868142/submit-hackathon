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

import re
from dataclasses import dataclass
from typing import List
from typing_extensions import Self
from cl.runtime import Context
from cl.runtime.experiments.trial_key import TrialKey
from cl.runtime.log.exceptions.user_error import UserError
from cl.runtime.primitive.string_util import StringUtil
from cl.runtime.records.dataclasses_extensions import missing
from cl.convince.entries.entry_key import EntryKey
from cl.convince.llms.gpt.gpt_llm import GptLlm
from cl.convince.llms.llm import Llm
from cl.convince.retrievers import retrieval
from cl.convince.retrievers.annotating_retriever import AnnotatingRetriever
from cl.tradeentry.entries.rates.swaps.any_leg_entry import AnyLegEntry
from cl.tradeentry.entries.trade_entry import TradeEntry

_PROMPT_TEMPLATE = """In this text, surround information about each leg in curly brackets. Make no other changes
to the text. Take into account the following:

- Only one set of curly brackets per leg should be present, surrounding the information specific to the leg
- Include information about who pays the leg
- Do not surround with curly brackets any text that is not specific to a single leg
- Do not miss any information from the original text

Text: 
```
{input_text}
```

Enclose you output text in triple backticks."""

_BRACES_RE = re.compile(r"\{(.*?)\}")
"""Regex for text between curly braces."""


@dataclass(slots=True, kw_only=True)
class RatesSwapEntry(TradeEntry):
    """Swap consists of two or more legs."""

    legs: List[EntryKey] | None = None
    """List of swap legs."""

    max_retries: int = missing()
    """How many times to retry the annotation in case changes other than braces are detected."""

    def init(self) -> Self:
        """Similar to __init__ but can use fields set after construction, return self to enable method chaining."""

        # Default max_retries
        if self.max_retries is None:
            self.max_retries = 1

        # Return self to enable method chaining
        return self

    def extract_legs(self, legs_annotation_prompt: str) -> List[str] | None:
        """Extract entry text for the legs from the entry text for the trade."""

        # Load the full LLM specified by the context
        context = Context.current()
        llm = context.load_one(Llm, context.full_llm)

        input_text = self.text
        trial_count = 2
        for retry_index in range(self.max_retries):
            is_last_trial = retry_index == self.max_retries - 1

            # Append retry_index to trial_id to avoid reusing a cached completion
            if self.max_retries > 1:
                context = Context.current()
                if context.trial is not None:
                    trial_key = TrialKey(trial_id=f"{context.trial.trial_id}\\{retry_index}")
                else:
                    trial_key = TrialKey(trial_id=str(retry_index))
            else:
                trial_key = context.trial
            with Context(trial=trial_key) as context:

                try:
                    # Create a brace extraction prompt using input parameters
                    rendered_prompt = legs_annotation_prompt.format(input_text=input_text)

                    # Get text annotated with braces and check that the only difference is braces and whitespace
                    completion = llm.completion(rendered_prompt)

                    # Remove triple backticks and curly brackets
                    to_compare = completion.replace("`", "").strip().replace("{", "").replace("}", "").strip()
                    if to_compare != input_text:
                        if not is_last_trial:
                            # Continue if not the last trial
                            continue
                        else:
                            # Otherwise report an error
                            # TODO: Use unified diff
                            raise UserError(
                                f"Annotated text has changes other than curly braces.\n"
                                f"Input text: ```{input_text}```\n"
                                f"Annotated text: ```{completion}```\n"
                            )

                    # Extract legs descriptions inside braces
                    extracted_legs = []
                    matches = re.findall(_BRACES_RE, completion)
                    for match in matches:
                        if "{" in match or "}" in match:
                            if not is_last_trial:
                                continue
                            else:
                                raise UserError(
                                    f"Nested curly braces are present in annotated text.\n"
                                    f"Annotated text: ```{completion}```\n"
                                )
                        else:
                            extracted_legs.append(match)

                    return extracted_legs

                except Exception as e:
                    if is_last_trial:
                        # Rethrow only when the last trial is reached
                        raise UserError(
                            f"Unable to extract legs from the input text after {trial_count} trials.\n"
                            f"Input text: {input_text}\n"
                            f"Last trial error information: {str(e)}\n"
                        )
                    else:
                        # Otherwise continue
                        pass

        # The method should always return from the loop, adding as a backup in case this changes in the future
        raise UserError(f"Unable to extract legs from the input text.\n" f"Input text: {input_text}\n")

    def run_generate(self) -> None:
        """Identify which part of the user input describes each leg and create an AnyLegEntry for each one."""

        # Reset before regenerating to prevent stale field values
        self.run_reset()

        leg_descriptions = self.extract_legs(_PROMPT_TEMPLATE)

        self.legs = []
        for leg_title in leg_descriptions:
            leg_entry = AnyLegEntry(text=leg_title).init()
            leg_entry.run_generate()
            Context.current().save_one(leg_entry)
            self.legs.append(leg_entry.get_key())

        Context.current().save_one(self)
