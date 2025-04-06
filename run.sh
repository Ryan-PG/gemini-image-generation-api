#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define project directory and venv path
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

# Step 1: Create .venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Step 2: Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Step 3: Install required packages
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r "$PROJECT_DIR/requirements.txt"

# Step 4: Check if .env file exists
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo ".env file not found. Please create one with your GEMINI_API_KEY."
    exit 1
fi

# Step 5: Run the Python script
python "$PROJECT_DIR/generate_image.py"
