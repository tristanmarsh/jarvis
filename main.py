import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from typing import Tuple
import argparse
from logger import Logger

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("user_prompt", type=str, help="user prompt for the llm")
parser.add_argument("-r", "--real", help="really call the llm model", action="store_true")
parser.add_argument("-v", "--verbose", help="print verbose output logs", action="store_true")
args = parser.parse_args()
logger = Logger(args.verbose)

def main():
    print("Hello from jarvis!")

    result = get_llm_result(args.user_prompt, args.real)

    print_llm_result(args.user_prompt, *result, args.verbose)


def get_llm_client():
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in .env")

    return genai.Client(api_key=api_key)


def get_llm_result(user_prompt, real=False):
    if real:
        client = get_llm_client()
        result = call_model(client, user_prompt)
    else:
        result = mock_call_model(user_prompt)
    return result

def mock_call_model(user_prompt: str) -> Tuple[int, int, str]:
    logger.log("mock_call_model")
    return (10, 1, f"{user_prompt}? Wow! That's crazy!")


def call_model(client, user_prompt: str) -> Tuple[int, int, str]:
    messages = types.Content(role="user", parts=[types.Part(text=user_prompt)])
    try:
        result = client.models.generate_content(
            model="gemini-2.5-flash", contents=messages
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
    verbose=False,
):
    template = f"Response:\n{response}"

    verbose_template = f"""User prompt: {user_prompt}
Prompt tokens: {prompt_tokens}
Response tokens: {response_tokens}
Response:
{response}
"""
    if verbose:
        print(verbose_template)
    else:
        print(template)


if __name__ == "__main__":
    main()
