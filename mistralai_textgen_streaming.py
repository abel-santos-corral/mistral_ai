import yaml
from mistralai import Mistral

# Chemin vers le fichier settings.yml
file_path = 'data/input/settings.yml'

# Lire le fichier YAML
with open(file_path, 'r') as file:
    settings = yaml.safe_load(file)

api_key = settings.get('MISTRAL_API_KEY')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

stream_response = client.chat.stream(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

for chunk in stream_response:
    print(chunk.data.choices[0].delta.content)