import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    print("Hello from jarvis!")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in .env")

    client = genai.Client(api_key=api_key)
    result = client.models.generate_content(
        model="gemini-2.5-flash", contents="Why is the sky blue?"
    )

    print(result.text)


if __name__ == "__main__":
    main()
