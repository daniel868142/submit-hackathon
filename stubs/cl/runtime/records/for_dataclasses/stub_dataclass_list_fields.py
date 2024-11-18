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

import datetime as dt
from dataclasses import dataclass
from typing import List
from cl.runtime.primitive.date_util import DateUtil
from cl.runtime.records.dataclasses_extensions import field
from cl.runtime.records.dataclasses_extensions import missing
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_data import StubDataclassData
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_derived_record import StubDataclassDerivedRecord
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_record import StubDataclassRecord
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_record import StubDataclassRecordKey


def stub_dataclass_str_list_factory() -> List[str]:
    """Create stub values."""
    return ["abc", "def"]


def stub_dataclass_float_list_factory() -> List[float]:
    """Create stub values."""
    return [
        0.0000123456789,
        0.000123456789,
        0.00123456789,
        0.0123456789,
        0.123456789,
        1.23456789,
        12.3456789,
        123.456789,
        1234.56789,
        12345.6789,
    ]


def stub_dataclass_date_list_factory() -> List[dt.date]:
    """Create stub values."""
    return [
        DateUtil.from_fields(2003, 4, 21),
        DateUtil.from_fields(2003, 5, 1),
    ]


def stub_dataclass_data_list_factory() -> List[StubDataclassData]:
    """Create stub values."""
    return [
        StubDataclassData(str_field="A", int_field=0),
        StubDataclassData(str_field="B", int_field=1),
    ]


def stub_dataclass_key_list_factory() -> List[StubDataclassRecordKey]:
    """Create stub values."""
    return [
        StubDataclassRecordKey(id="A"),
        StubDataclassRecordKey(id="B"),
    ]


def stub_dataclass_record_list_factory() -> List[StubDataclassRecord]:
    """Create stub values."""
    return [
        StubDataclassRecord(id="A"),
        StubDataclassRecord(id="B"),
    ]


def stub_dataclass_derived_record_list_factory() -> List[StubDataclassDerivedRecord]:
    """Create stub values."""
    return [
        StubDataclassDerivedRecord(id="A"),
        StubDataclassDerivedRecord(id="B"),
    ]


@dataclass(slots=True, kw_only=True)
class StubDataclassListFields(StubDataclassRecord):
    """Stub record whose elements are lists."""

    str_list: List[str] = field(default_factory=stub_dataclass_str_list_factory)
    """Stub field."""

    float_list: List[float] = field(default_factory=stub_dataclass_float_list_factory)
    """Stub field."""

    date_list: List[dt.date] = field(default_factory=stub_dataclass_date_list_factory)
    """Stub field."""

    data_list: List[StubDataclassData] = field(default_factory=stub_dataclass_data_list_factory)
    """Stub field."""

    key_list: List[StubDataclassRecordKey] = field(default_factory=stub_dataclass_key_list_factory)
    """Stub field."""

    record_list: List[StubDataclassRecord] = field(default_factory=stub_dataclass_record_list_factory)
    """Stub field."""

    derived_record_list: List[StubDataclassDerivedRecord] = field(
        default_factory=stub_dataclass_derived_record_list_factory
    )
    """Stub field."""
