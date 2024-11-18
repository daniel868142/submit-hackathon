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

import pytest
from typing import Dict
from matplotlib import pyplot as plt
from cl.runtime import Context
from cl.runtime.context.env_util import EnvUtil
from cl.runtime.context.testing_context import TestingContext
from cl.runtime.experiments.experiment import Experiment
from cl.runtime.experiments.trial_key import TrialKey
from cl.runtime.plots.group_bar_plot import GroupBarPlot
from cl.runtime.testing.regression_guard import RegressionGuard
from cl.convince.retrievers.retriever_util import RetrieverUtil
from stubs.cl.convince.experiments.stub_llms import get_stub_full_llms
from stubs.cl.tradeentry.experiments.stub_tag_utils import add_line_numbers
from stubs.cl.tradeentry.experiments.stub_tag_utils import fields_to_text
from stubs.cl.tradeentry.experiments.stub_trade_checker import StubFormattedStringChecker
from stubs.cl.tradeentry.experiments.stub_trade_entries import stub_amortizing_swap_entry
from stubs.cl.tradeentry.experiments.stub_trade_entries import stub_floored_swap_entry
from stubs.cl.tradeentry.experiments.stub_trade_entries import stub_vanilla_swap_entry

PROMPT_TEMPLATE = """You will be given a description of a trade entry with numbered rows, followed by a list of fields to identify within that text.
Your task is to find relevant information about the field and reference to place in the row where you found the information.

Here is the input trade entry:
```
{input_text}
```

The description of the fields you need to identify:
```
{fields}
```

Each field description contain datatype and occurrences type.
If the occurrences type is single you should look for a single place among that contains the most relevant information about the field.
If the occurrences type is multiple you should include every place that has information relevant to the field.
Datatype helps you understand what data you are looking for. However, when you are asked to get the piece of data you should copy it and return as a string always.

For each field you should do the following:
1. Find all data corresponding to the field in the trade entry.
2. If the occurrence type is single, then select only one piece of data that is the most relevant, if the occurrence type is multiple, then select all of them.
3. For every such piece of data create the following dictionary
{{
    "data": <piece of data, string>,
    "formatted_row": <the original row from the description, with the extracted information replaced by the field name in curly brackets>
}}
4. If the occurrence type is single, then the output should be one dictionary, if the occurrence type is multiple, then the answer should be list of dictionaries.
5. If there is no piece of data that has relevant information than the generated dictionary should have empty strings as default values.
6. Make sure that if you put the data into a formatted string, it will match the string in the input trade entry, do nor forgot row number.

Generate json dictionary with the field names as keys. The above algorithm describes how to create value for every field.

Enclose json in triple single quotes and ensure that it is parsable."""

FIELDS = [
    {"name": "FloatLegCurrency", "type": "string", "freq": "single", "short_name": "FLC"},
    {"name": "FloatLegIndex", "type": "string", "freq": "single", "short_name": "FLI"},
    {"name": "FloatLegSpread", "type": "float", "freq": "single", "short_name": "FLS"},
    {"name": "FloatLegFrequency", "type": "string", "freq": "single", "short_name": "FLF"},
    {"name": "FloatLegDaycountBasis", "type": "string", "freq": "single", "short_name": "FLB"},
    {"name": "FixedLegCurrency", "type": "string", "freq": "single", "short_name": "FDC"},
    {"name": "FixedLegFixedRate", "type": "float", "freq": "single", "short_name": "FDR"},
    {"name": "FixedLegFrequency", "type": "string", "freq": "single", "short_name": "FDF"},
    {"name": "FixedLegDaycountBasis", "type": "string", "freq": "single", "short_name": "FDB"},
    {"name": "StartDate", "type": "date", "freq": "single", "short_name": "SDT"},
    {"name": "NotionalAmount", "type": "float", "freq": "multiple or single", "short_name": "NA"},
]


def _testing_formatted_string(trade_description: str, run_count: int) -> plt.Figure:
    # Text for the fields
    fields_text = fields_to_text(FIELDS)

    # Create Llm objects for test
    stub_full_llms = get_stub_full_llms()

    prompt = PROMPT_TEMPLATE.format(input_text=trade_description, fields=fields_text)
    field_names = [field["name"] for field in FIELDS]
    plot_bar_labels = []
    plot_group_labels = []
    plot_values = []
    for llm in stub_full_llms:
        results = {field: 0 for field in field_names}
        for trial_index in range(run_count):
            with Context(trial=TrialKey(trial_id=str(trial_index))) as context:
                result = llm.completion(prompt)

                json_result = RetrieverUtil.extract_json(result)
                guard = RegressionGuard(channel=llm.llm_id)
                if json_result is not None:
                    guard.write(json_result)
                else:
                    guard.write("ERROR: can not extract json")

                guard_checker = RegressionGuard(channel=f"{llm.llm_id}-checker")
                if isinstance(json_result, Dict):
                    json_checker_output = StubFormattedStringChecker(trade_description, FIELDS).check_answer(
                        json_result
                    )
                    for field in field_names:
                        if json_checker_output[field]["status"] == "OK":
                            results[field] += 1
                    guard_checker.write(json_checker_output)
                else:
                    guard_checker.write("ERROR: No input to check")

        plot_bar_labels.extend([llm.llm_id] * len(results))
        plot_group_labels.extend([field["short_name"] for field in FIELDS])
        plot_values.extend(list(results.values()))

    normalized_plot_values = [round(val / run_count * 100, 2) for val in plot_values]

    plot = GroupBarPlot(
        plot_id="accuracy",
        bar_labels=plot_bar_labels,
        group_labels=plot_group_labels,
        values=normalized_plot_values,
        value_ticks=list(range(0, 101, 10)),
    )
    plot.save_png()


def test_vanilla_swap():
    with TestingContext():
        numbered_vanilla_swap = add_line_numbers(stub_vanilla_swap_entry)
        _testing_formatted_string(numbered_vanilla_swap, run_count=50)
        RegressionGuard().verify_all()


def test_floored_swap():
    with TestingContext():
        numbered_floored_swap = add_line_numbers(stub_floored_swap_entry)
        _testing_formatted_string(numbered_floored_swap, run_count=50)
        RegressionGuard().verify_all()


def test_amortizing_swap():
    with TestingContext():
        numbered_amortizing_swap = add_line_numbers(stub_amortizing_swap_entry)
        _testing_formatted_string(numbered_amortizing_swap, run_count=50)
        RegressionGuard().verify_all()


if __name__ == "__main__":
    pytest.main([__file__])
