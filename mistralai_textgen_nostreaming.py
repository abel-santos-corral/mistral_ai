"""
Script for generating text using Mistral AI's chat completion API.
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

MODEL = "mistral-large-latest"
client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)
