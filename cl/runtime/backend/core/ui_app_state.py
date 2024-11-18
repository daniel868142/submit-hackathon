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
from typing import List
from typing import Optional
from cl.runtime import Context
from cl.runtime.backend.core.app_theme import AppTheme
from cl.runtime.backend.core.tab_info import TabInfo
from cl.runtime.backend.core.ui_app_state_key import UiAppStateKey
from cl.runtime.backend.core.user_key import UserKey
from cl.runtime.records.dataclasses_extensions import field
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.records.record_mixin import RecordMixin


@dataclass(slots=True, kw_only=True)
class UiAppState(UiAppStateKey, RecordMixin[UiAppStateKey]):
    """UiAppState."""

    opened_tabs: List[TabInfo] | None = missing()
    """Information about opened tabs."""

    active_tab_index: int | None = missing()
    """Index of active opened tab."""

    backend_version: str | None = missing()
    """DEPRECATED. Use versions instead."""

    application_name: str | None = missing()
    """Application name."""

    read_only: bool | None = missing()
    """Flag indicating that UI is read-only."""

    application_theme: str | None = missing()  # TODO: Replace by AppTheme
    """Application theme (dark, light, etc.)."""

    user_secret_identifiers: List[str] | None = missing()
    """
    Suggested key names in My Keys section of the head and shoulders dialog.

    Notes:
        - This is a list of suggestions, no restriction on entering secrets with other names
        - The secret names should be in snake_case, for example ["openai_api_key", "anthropic_api_key"] 
    """

    def get_key(self) -> UiAppStateKey:
        return UiAppStateKey(user=self.user)

    @classmethod
    def get_current_user_app_theme(cls) -> AppTheme | None:
        """Get current user app theme."""

        default_app_state_key = UiAppStateKey(user=UserKey(username="root"))  # TODO: Review the use of root default

        default_app_state = Context.current().load_one(UiAppStateKey, default_app_state_key, is_record_optional=True)
        if default_app_state is not None and default_app_state.application_theme is not None:
            return default_app_state.application_theme

        # Default to System if not previously selected by the user
        return "System"
