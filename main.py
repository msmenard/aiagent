import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



def main():
    if len(sys.argv) < 2:
        print("Please provide a prompt for the AI Agent to process.\nuv run main.py <prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]
    if len(sys.argv) == 3:
        verbose_flag = sys.argv[2]
    else:
        verbose_flag = None
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
#    print("Hello from aiagent!")

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(response.text)

    if verbose_flag == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
