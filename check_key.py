"""One Gemini call that proves GEMINI_API_KEY works."""

import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

# gemini-3.8-flash is listed for this key, and it is the model the SDK docs use.
# On 16 November 2026 it returned 503 (high demand) and then 504 (deadline).
# gemini-3.5-flash answered, so the rest of the project calls this id.
MODEL = "gemini-3.5-flash"


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY is missing. Put it in .env in this directory.")

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=60_000),
    )
    response = client.models.generate_content(
        model=MODEL,
        contents="Reply with one short sentence confirming you can read this.",
    )
    print(response.text)
    usage = response.usage_metadata
    print(
        f"model={MODEL} "
        f"prompt_tokens={usage.prompt_token_count} "
        f"output_tokens={usage.candidates_token_count} "
        f"thoughts_tokens={usage.thoughts_token_count} "
        f"total_tokens={usage.total_token_count}"
    )


if __name__ == "__main__":
    main()
