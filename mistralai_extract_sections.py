from datetime import datetime
from loguru import logger
import os
from app.pdf_processing.extractor import load_prompt_config, process_pdf, save_analysis

# --- Logging Setup ---
os.makedirs("data/output/logs", exist_ok=True)
log_filename = datetime.now().strftime("logs_%d%m%Y_%H%M") + ".log"
log_path = os.path.join("data/output/logs", log_filename)
logger.add(
    log_path,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="1 day",
    compression="zip"
)
# --- End Logging Setup ---

def main():
    pdf_dir = "data/input/pdf"
    config_path = "data/input/settings.yml"
    output_dir = "data/output/analysis/pdf"

    prompt = load_prompt_config(config_path)

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            analysis = process_pdf(pdf_path, prompt)
            save_analysis(output_dir, analysis)

if __name__ == "__main__":
    logger.info("Starting PDF section extraction...")
    main()
    logger.info("Process completed.")
