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
from stubs.cl.runtime import StubDataclassRecordKey
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_dict_fields import StubDataclassDictFields
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_list_fields import StubDataclassListFields
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_primitive_fields import StubDataclassPrimitiveFields
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_record import StubDataclassRecord


def test_smoke():
    """Smoke test."""

    # Create test record and populate with sample data
    record = StubDataclassRecord()

    # Test primary key
    key = record.get_key()
    assert key == StubDataclassRecordKey(id="abc")


def test_with_primitive_fields():
    """Test for a record with primitive fields."""

    # TODO: Complete
    record = StubDataclassPrimitiveFields()
    record = StubDataclassListFields()
    pass


def test_with_lists():
    """Test for a record with primitive fields."""

    record = StubDataclassListFields()
    pass


def test_with_dicts():
    """Test for a record with primitive fields."""

    record = StubDataclassDictFields()
    pass


if __name__ == "__main__":
    pytest.main([__file__])
