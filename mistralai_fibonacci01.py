import yaml
from mistralai import Mistral

# Chemin vers le fichier settings.yml
file_path = 'data/input/settings.yml'

# Lire le fichier YAML
with open(file_path, 'r') as file:
    settings = yaml.safe_load(file)

api_key = settings.get('MISTRAL_API_KEY')
client = Mistral(api_key=api_key)

model = "codestral-latest"
prompt = "def fibonacci(n: int):"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.fim.complete(
    model=model,
    prompt=prompt,
    suffix=suffix,
    temperature=0,
    top_p=1,
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
{suffix}
"""
)