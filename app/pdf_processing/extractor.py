from loguru import logger
import os
import yaml
from typing import List, Dict
import json

def load_prompt_config(config_path: str) -> str:
    """Load the prompt from settings.yml."""
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config['prompts']['prompt_extract_sections']

def process_pdf(pdf_path: str, prompt: str) -> Dict:
    """Simulate sending PDF to Mistral API and extracting sections."""
    # In a real implementation, you would:
    # 1. Extract text from PDF (e.g., using PyPDF2)
    # 2. Send text + prompt to Mistral API
    # 3. Parse the response
    # For now, return a mock response
    logger.info(f"Processing PDF: {pdf_path}")
    return {
        "name": os.path.basename(pdf_path),
        "sections": [
            {"title": "Introduction", "content": "Sample content..."},
            {"title": "Methodology", "content": "Sample content..."}
        ]
    }

def save_analysis(output_dir: str, analysis: Dict):
    """Save the analysis as a JSON file."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "section_analysis.json")
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(analysis, file, indent=4)
    logger.info(f"Saved analysis to: {output_path}")
