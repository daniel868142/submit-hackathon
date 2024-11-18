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
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Type
from typing_extensions import Self
from cl.runtime import Context
from cl.runtime.log.exceptions.user_error import UserError
from cl.runtime.primitive.bool_util import BoolUtil
from cl.runtime.primitive.case_util import CaseUtil
from cl.runtime.primitive.string_util import StringUtil
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.records.record_mixin import RecordMixin
from cl.convince.entries.entry_key import EntryKey
from cl.convince.settings.convince_settings import ConvinceSettings


@dataclass(slots=True, kw_only=True)
class Entry(EntryKey, RecordMixin[EntryKey], ABC):
    """Contains description, body and supporting data of user entry along with the entry processing result."""

    entry_type: str = missing()
    """Entry type string is set in 'init' method of a descendant of this class."""

    text: str = missing()
    """Description exactly as provided by the user (included in MD5 hash)."""

    locale: str = missing()
    """Locale in BCP 47 ll-CC where ll is language and CC is country (included in MD5 hash)."""

    data: str | None = None
    """Optional supporting data in YAML format (included in MD5 hash)."""

    verified: bool | None = None
    """Flag indicating the entry is verified."""

    def get_key(self) -> EntryKey:
        return EntryKey(entry_id=self.entry_id)

    def init(self) -> Self:
        """Generate entry_id from text, locale and data fields."""

        # Check text
        if StringUtil.is_empty(self.text):
            raise UserError(f"Empty 'text' field in {type(self).__name__}.")

        # Check locale format or set based on the default in ConvinceSettings if not specified
        if self.locale is not None:
            # This performs validation
            ConvinceSettings.parse_locale(self.locale)
        else:
            self.locale = ConvinceSettings.instance().locale

        # Convert field types if necessary
        if self.verified is not None and isinstance(self.verified, str):
            self.verified = BoolUtil.parse_optional_bool(self.verified, field_name="verified")

        # Base type resolves the ambiguity of different entry types with the same text
        base_type = self.get_base_type()
        self.entry_type = base_type.__name__.removesuffix("Entry")

        # Generate digest if multiline or more than 80 characters
        self.entry_id = StringUtil.digest(
            self.text,
            text_params=(
                self.entry_type,
                self.locale,
            ),
            hash_params=(self.data,),
        )

        # Return self to enable method chaining
        return self

    @abstractmethod
    def get_base_type(self) -> Type:
        """Lowest level of class hierarchy that resolves the ambiguity of different entry types with the same text."""

    def get_text(self) -> str:
        """Get the complete text of the entry."""
        # TODO: Support data
        if self.data is not None:
            raise RuntimeError("Entry 'data' field is not yet supported.")
        result = self.text
        return result

    # TODO: Restore abstract when implemented for all entries
    def run_generate(self) -> None:
        """Generate or regenerate the proposed value."""
        raise UserError(f"Propose handler is not yet implemented for {type(self).__name__}.")

    def run_reset(self) -> None:
        """Clear all output fields and the verification flag."""
        if self.verified:
            raise UserError(
                f"Entry {self.entry_id} is marked as verified, run Unmark Verified before running Reset."
                f"This is a safety feature to prevent overwriting verified entries. "
            )

        # Create a record of the same type but copy the base class fields except entry_type and verified
        record_type = type(self)
        result = record_type(text=self.text, locale=self.locale, data=self.data)  # noqa
        result.init()

        # Save to replace the current record
        Context.current().save_one(result)

    def run_mark_verified(self) -> None:
        """Mark verified."""
        self.verified = True
        Context.current().save_one(self)

    def run_unmark_verified(self) -> None:
        """Unmark verified."""
        self.verified = False
        Context.current().save_one(self)
