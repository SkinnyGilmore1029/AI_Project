import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


#check to make sure it has the right number of arguments
if len(sys.argv) < 2:
    print("Please provide a model name as a command-line argument.")
    sys.exit(1)

client = genai.Client(api_key=api_key)
user_input = sys.argv[1]

messages:list = types.Content(role="user",parts=[types.Part(text=user_input)])


response = client.models.generate_content(model="gemini-2.0-flash-001",
                                              contents = messages)

token_count = response.usage_metadata.prompt_token_count
cand_token_count = response.usage_metadata.candidates_token_count

if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(f"{response.text}\nPrompt tokens: {token_count}\nResponse tokens: {cand_token_count}")
else:
    print(response.text)