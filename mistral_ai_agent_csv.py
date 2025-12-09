import os
import json
import re
import argparse
import pandas as pd
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the Mistral API key from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("Mistral API key not found in environment variables.")

def extract_json_from_response(response):
    print(response)
    """
    Extracts the JSON from the agent's response, which is inside a Markdown code block.
    """
    for entry in response.outputs:
        if hasattr(entry, 'content') and '```json' in entry.content:
            # Extract the JSON between ```json and ```
            match = re.search(r'```json\n(.*?)\n```', entry.content, re.DOTALL)
            if match:
                json_str = match.group(1)
                try:
                    json_data = json.loads(json_str)
                    return json_data
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    return None
    return None

def send_to_agent(file_path, fields):
    """Send the CSV content to the Mistral agent."""
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("CSV file is empty.")
        csv_content = df.to_csv(index=False)
    except Exception as e:
        raise ValueError(f"Error reading CSV: {e}")

    client = Mistral(api_key=api_key)
    prompt = f"""
    Convert the following CSV content to JSON, extracting only these fields: {fields}.
    CSV content:
    {csv_content}
    """
    response = client.beta.conversations.start(
        agent_id="ag_019abc550b13703ba12c69cd4dbee2df",
        inputs=prompt,
    )
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a CSV file to a Mistral agent for conversion to JSON.")
    parser.add_argument("file_path", type=str, help="Path to the CSV file.")
    parser.add_argument("fields", type=str, help="Comma-separated list of fields to extract (e.g., 'name,age,email').")
    args = parser.parse_args()

    fields = args.fields.split(',')
    try:
        response = send_to_agent(args.file_path, fields)
        json_result = extract_json_from_response(response)
        if json_result:
            print(json.dumps(json_result, indent=4))
        else:
            print("No JSON result found in the response.")
    except Exception as e:
        print("Error:", e)
