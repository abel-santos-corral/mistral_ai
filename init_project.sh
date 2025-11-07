#!/usr/bin/env bash

# Exit immediately on error
set -e

# --- Step 1: Copy .env.dist -> .env if .env does not already exist ---
if [ ! -f ".env" ]; then
    cp .env.dist .env
    echo ".env created from .env.dist."
else
    echo ".env already exists. Skipping copy."
fi

# --- Step 2: Create Python virtual environment ---
python -m venv venv
echo "Virtual environment created."

# --- Step 3: Activate the virtual environment ---
# (Linux / Mac)
source venv/bin/activate
echo "Virtual environment activated."

# --- Step 4: Install dependencies if requirements.txt exists ---
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "Dependencies installed."
else
    echo "No requirements.txt found — skipping dependency installation."
fi

echo "✅ Project initialized. Environment ready."
