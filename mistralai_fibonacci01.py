"""
Module for generating Fibonacci function code using Mistral AI's FIM completion.
"""
import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables from .env
load_dotenv()

# Get the Mistral API key from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("Mistral API key not found in environment variables.")

client = Mistral(api_key=api_key)

MODEL = "codestral-latest"
PROMPT = "def fibonacci(n: int):"
SUFFIX = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.fim.complete(
    model=MODEL,
    prompt=PROMPT,
    suffix=SUFFIX,
    temperature=0,
    top_p=1,
)

print(
    f"""
{PROMPT}
{response.choices[0].message.content}
{SUFFIX}
"""
)
