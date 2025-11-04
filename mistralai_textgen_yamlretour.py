import os
import yaml
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

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": (
                "Peux-tu fournir une liste de pays européens exclusivement au format YAML ? "
                "Chaque pays doit avoir un champ 'langues' avec un tableau des langues officielles "
                "et un champ 'capitale' avec le nom de la capitale. Par exemple :\n"
                "```yaml\n"
                "France:\n"
                "  langues: ['Français']\n"
                "  capitale: 'Paris'\n"
                "Espagne:\n"
                "  langues: ['Espagnol']\n"
                "  capitale: 'Madrid'\n"
                "```"
            ),
        },
    ]
)

print(chat_response.choices[0].message.content)

# Récupérer la réponse
response_content = chat_response.choices[0].message.content

# Rechercher les délimiteurs YAML
start_marker = "```yaml"
end_marker = "```"
start_index = response_content.find(start_marker)
end_index = response_content.find(end_marker, start_index + len(start_marker))

if start_index != -1 and end_index != -1:
    # Extraire le contenu YAML
    yaml_content = response_content[start_index + len(start_marker):end_index].strip()
    try:
        # Vérifier si le contenu est un YAML valide
        yaml_data = yaml.safe_load(yaml_content)
        # Chemin pour enregistrer le fichier de sortie
        output_path = 'data/output/pays_europeens.yml'
        # Assurez-vous que le dossier de sortie existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # Enregistrer le contenu YAML dans un fichier
        with open(output_path, 'w') as output_file:
            yaml.dump(yaml_data, output_file, allow_unicode=True)
        print(f"Le fichier a été enregistré avec succès à {output_path}")
    except yaml.YAMLError as e:
        print("Le contenu extrait n'est pas un YAML valide:", e)
else:
    print("Aucun contenu YAML trouvé dans la réponse.")
