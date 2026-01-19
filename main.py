import os
from dotenv import load_dotenv
from google import genai
import sys
from typing import Tuple

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    real = False
    if len(sys.argv) > 1:
        print(sys.argv[1])
        if "real" in sys.argv[1]:
            real = True

    print("Hello from jarvis!")

    get_llm_result(real)


def get_llm_client():
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in .env")

    return genai.Client(api_key=api_key)


def get_llm_result(real=False):
    user_prompt = "2+2=?\nNumerical response only."
    if real:
        client = get_llm_client()
        result = call_model(client, user_prompt)
    else:
        result = mock_call_model(user_prompt)
    print_llm_result(user_prompt, *result)


def mock_call_model(user_prompt: str) -> Tuple[int, int, str]:
    print("Log: mock_call_model")
    return (10, 1, f"{user_prompt}? Wow! That's crazy!")


def call_model(client, user_prompt: str) -> Tuple[int, int, str]:
    try:
        result = client.models.generate_content(
            model="gemini-2.5-flash", contents=user_prompt
        )

        if result is None or result.usage_metadata is None:
            raise RuntimeError("Usage metadata missing from LLM response", result)

        um = result.usage_metadata

        if um.prompt_token_count is None or um.candidates_token_count is None:
            raise RuntimeError("Token counts missing from usage_metadata", result)

        if result.text is None:
            raise Exception("text missing from LLM response", result)

        return (um.prompt_token_count, um.candidates_token_count, result.text)
    except Exception as e:
        raise RuntimeError("Unknown error calling model", e)


def print_llm_result(
    user_prompt: str,
    prompt_tokens: int,
    response_tokens: int,
    response: str,
):
    template = f"""User prompt: {user_prompt}
Prompt tokens: {prompt_tokens}
Response tokens: {response_tokens}
Response:
{response}
"""
    print(template)


if __name__ == "__main__":
    main()
