import time
from typing import Optional, Type, Any, List

from pydantic import BaseModel

from finagy.prompts import DEFAULT_SYSTEM_PROMPT
from finagy.llm import call_provider


def call_llm(
    prompt: str,
    system_prompt: Optional[str] = None,
    output_schema: Optional[Type[BaseModel]] = None,
    tools: Optional[List[Any]] = None,
) -> Any:
    """Provider-agnostic LLM call.

    This delegates to `finagy.llm.call_provider`, which currently implements
    an OpenAI-backed path. Anthropic/Claude can be added as an adapter in
    `finagy/llm.py` without changing this function signature.
    """
    final_system_prompt = system_prompt if system_prompt else DEFAULT_SYSTEM_PROMPT

    # Simple retry logic for transient errors
    for attempt in range(3):
        try:
            result = call_provider(
                provider=None,  # call_provider will read LLM_PROVIDER or default
                prompt=prompt,
                system_prompt=final_system_prompt,
            )
            return result
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(0.5 * (2 ** attempt))
