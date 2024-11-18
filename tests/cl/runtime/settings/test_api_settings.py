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
from cl.runtime.settings.api_settings import ApiSettings


def test_defaults():
    """Test defaults for ApiSettings class."""

    api_settings = ApiSettings.instance()
    assert api_settings.hostname == "localhost"
    assert api_settings.port == 7008
    assert api_settings.allow_credentials
    assert api_settings.allow_methods == ["*"]
    assert api_settings.allow_headers == ["*"]


if __name__ == "__main__":
    pytest.main([__file__])
