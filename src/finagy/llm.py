import os
from typing import Optional, Any, Dict

try:
    # OpenAI official SDK
    from openai import OpenAI, APIConnectionError
except Exception:
    OpenAI = None
    APIConnectionError = Exception


def call_provider(
    provider: str,
    prompt: str,
    system_prompt: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Call the chosen LLM provider and return the raw response.

    Currently supports:
      - 'openai' : uses the `openai` Python package and the Chat Completions API.

    If `provider!='openai'`, raises NotImplementedError with guidance on how to
    add Anthropic/Claude support.

    This function centralizes provider selection so we can add Claude later
    without touching the rest of the codebase.
    """
    provider = (provider or os.getenv("LLM_PROVIDER") or "openai").lower()
    system_prompt = system_prompt or ""
    model = model or os.getenv("OPENAI_MODEL", "gpt-4.1")

    if provider == "openai":
        if OpenAI is None:
            raise RuntimeError("openai package is not available in the environment")

        client = OpenAI()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        try:
            resp = client.chat.completions.create(model=model, messages=messages)
            return {"provider": "openai", "response": resp}
        except APIConnectionError:
            raise

    # Placeholder for Anthropic support
    if provider in ("anthropic", "claude"):
        raise NotImplementedError(
            "Anthropic/Claude support not yet implemented. "
            "Install `langchain-anthropic` or the `anthropic` SDK and add an adapter in `finagy/llm.py`."
        )

    raise ValueError(f"Unknown LLM provider: {provider}")
