import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables from .env
load_dotenv()

# Get the Mistral API key from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("Mistral API key not found in environment variables.")

model = "mistral-large-latest"
client = Mistral(api_key=api_key)

stream_response = client.chat.stream(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

for chunk in stream_response:
    print(chunk.data.choices[0].delta.content, end="", flush=True)
