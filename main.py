import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

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
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
        
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    function_call_part = response.function_calls or []

    if function_call_part:
        for call in function_call_part:
            print(f"Calling function: {function_call_part[0].name}({function_call_part[0].args})")
    else:
        print(response.text)

    if verbose_flag == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    


if __name__ == "__main__":
    main()
