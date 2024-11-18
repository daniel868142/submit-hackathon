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
import fireworks.client  # noqa
from cl.runtime.context.context_util import ContextUtil
from cl.runtime.log.exceptions.user_error import UserError
from cl.convince.llms.llama.llama_llm import LlamaLlm
from cl.convince.settings.fireworks_settings import FireworksSettings


@dataclass(slots=True, kw_only=True)
class FireworksLlamaLlm(LlamaLlm):
    """Implements LLAMA API running in the Fireworks cloud."""

    model_name: str | None = None
    """Model name in Fireworks format including version if any, defaults to 'llm_id'."""

    max_tokens: int = 4096
    """Maximum number of tokens the model will generate in response to the query."""

    temperature: float | None = None
    """
    The sampling temperature between 0 and 1 (optional, passed as 'temperature' to OpenAI SDK).

    Notes:
        Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it
        more focused  and deterministic. If set to 0, the model will use log probability to automatically
        increase the temperature until certain thresholds are hit.
    """

    def uncached_completion(self, request_id: str, query: str) -> str:
        """Perform completion without CompletionCache lookup, call completion instead."""

        # Prefix a unique RequestID to the model for audit log purposes and
        # to stop model provider from caching the results
        query_with_request_id = f"RequestID: {request_id}\n\n{query}"

        model_name = self.model_name if self.model_name is not None else self.llm_id
        prompt = f"""<|begin_of_text|><|start_header_id|>user<|end_header_id|>

{query_with_request_id}<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>"""

        # Try loading API key from context.secrets first and then from settings
        api_key = ContextUtil.decrypt_secret("FIREWORKS_API_KEY") or FireworksSettings.instance().api_key
        if api_key is None:
            raise UserError("Provide FIREWORKS_API_KEY in Account > My Keys (users) or using Dynaconf (developers).")
        fireworks.client.api_key = api_key

        response = fireworks.client.Completion.create(
            model=f"accounts/fireworks/models/{model_name}",
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        result = response.choices[0].text
        return result
