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
from cl.runtime.primitive.string_util import StringUtil
from cl.runtime.testing.regression_guard import RegressionGuard


def test_is_empty():
    """Test for StringUtil.is_empty."""
    assert StringUtil.is_empty(None)
    assert StringUtil.is_empty("")
    assert not StringUtil.is_empty("abc")


def test_digest():
    """Test EntryKey.create_key method."""

    guard = RegressionGuard()

    # Record type
    locale = "en-GB"

    guard.write("Check short text without params with and without data, hash should be different")
    guard.write(StringUtil.digest(text="Sample Text"))
    guard.write(StringUtil.digest(text="Sample Text", hash_params=("Sample Data",)))

    guard.write("Check short text with params with and without data, hash should be different")
    guard.write(StringUtil.digest(text="Sample Text", text_params=(locale,)))
    guard.write(StringUtil.digest(text="Sample Text", text_params=(locale,), hash_params=("Sample Data",)))

    guard.write("Check long text with and without data, hash should be different")
    guard.write(StringUtil.digest(text=" ".join(20 * ["Long Text"]), text_params=(locale,)))
    guard.write(
        StringUtil.digest(text=" ".join(20 * ["Long Text"]), text_params=(locale,), hash_params=("Sample Data",))
    )

    guard.write("Check multiline text with and without data, hash should be different")
    guard.write(StringUtil.digest(text="Multiline\nText", text_params=(locale,)))
    guard.write(StringUtil.digest(text="Multiline\nText", text_params=(locale,), hash_params=("Sample Data",)))

    guard.write("The same inputs one more time, hash should be the same")
    guard.write(StringUtil.digest(text="Multiline\nText", text_params=(locale,), hash_params=("Sample Data",)))

    # Verify
    guard.verify_all()


if __name__ == "__main__":
    pytest.main([__file__])