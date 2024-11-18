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
import google.generativeai as gemini  # noqa
from cl.runtime.context.context_util import ContextUtil
from cl.runtime.log.exceptions.user_error import UserError
from cl.convince.llms.llm import Llm
from cl.convince.settings.google_settings import GoogleSettings


@dataclass(slots=True, kw_only=True)
class GeminiLlm(Llm):
    """Implements Gemini LLM API."""

    model_name: str | None = None
    """Model name in Gemini format including version if any, defaults to 'llm_id'."""

    def uncached_completion(self, request_id: str, query: str) -> str:
        """Perform completion without CompletionCache lookup, call completion instead."""

        # Prefix a unique RequestID to the model for audit log purposes and
        # to stop model provider from caching the results
        query_with_request_id = f"RequestID: {request_id}\n\n{query}"

        model_name = self.model_name if self.model_name is not None else self.llm_id

        # Try loading API key from context.secrets first and then from settings
        api_key = ContextUtil.decrypt_secret("GOOGLE_API_KEY") or GoogleSettings.instance().api_key
        if api_key is None:
            raise UserError("Provide GOOGLE_API_KEY in Account > My Keys (users) or using Dynaconf (developers).")
        gemini.configure(api_key=api_key)

        model = gemini.GenerativeModel(model_name=model_name)
        response = model.generate_content(query)

        result = response.text
        return result

    @classmethod
    def create_prompt_from_messages(cls, messages: list[dict]) -> list[dict[str, str]]:
        """
        Having a list of messages in the following format:
        [
            {"role": "system", "content": "System Prompt"},
            {"role": "user", "content": "What is 2 + 2?"},
            {"role": "assistant", "content": "2+2 is equals to 4"},
            {"role": "user", "content": "Answer only with resulting number"},
        ]
        Returns:
        [
            {"role": "system", "parts": ["System Prompt"]},
            {"role": "user", "parts": ["What is 2 + 2?"]},
            {"role": "assistant", "parts": ["2+2 is equals to 4"]},
            {"role": "user", "parts": ["Answer only with resulting number"]},
        ]
        """
        return [{"role": message.role.name, "parts": [message.content]} for message in messages]
