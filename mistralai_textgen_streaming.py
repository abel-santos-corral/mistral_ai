"""
Mistral AI streaming text generation module.
This module demonstrates how to use the Mistral AI API for streaming chat responses.
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

stream_response = client.chat.stream(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

for chunk in stream_response:
    print(chunk.data.choices[0].delta.content, end="", flush=True)
