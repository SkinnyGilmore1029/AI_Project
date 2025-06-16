import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_input = sys.argv[1]

if user_input:
    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                              contents =user_input)
else:
    print("Please provide a model name as a command-line argument.")
    sys.exit(1)

token_count = response.usage_metadata.prompt_token_count
cand_token_count = response.usage_metadata.candidates_token_count

print(f"{response.text}\nPrompt tokens: {token_count}\nResponse tokens: {cand_token_count}")