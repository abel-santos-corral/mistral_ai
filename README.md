# Mistral AI
Mistral AI repository is used to make testing developments in python for Mistral.

## Table of Contents

# Mistral AI
Mistral AI repository is used to make testing developments in python for Mistral.

## Table of Contents

- [Mistral AI](#mistral-ai)
- [Overview](#overview)
- [VS Code Configuration](#vs-code-configuration)
- [Agent example](#agent-example)
- [Add Mistral key](#add-mistral-key)
- [Extract sections from PDF](#extract-sections-from-pdf)

# Overview

This package will hold all examples and code to connect to Mistral. To be used as a template for other packages.

# VS Code Configuration

To configure VS Code and get your environment ready, follow these steps.

1. **Create the virtual environment**:

  - First, go to the project folder and run:

# Overview

This package will hold all examples and code to connect to Mistral. To be used as a template for other packages.

# VS Code Configuration

To configure VS Code and get your environment ready, follow these steps.

1. **Create the virtual environment**:

  - First, go to the project folder and run:
    ```
    python -m venv venv
    ```

2. **Activate the virtual environment**:

   It depends on your operating system (OS).

      **Linux**

      ```
      source venv/bin/activate
      ```

      **Windows (PowerShell)**

      ```
      venv\Scripts\Activate.ps1
      ```

      **Windows (Command Prompt)**

      ```
      venv\Scripts\activate
      ```

Alternatively use the script:
```
chmod +x init_project.sh
./init_project.sh
```

# Agent example

For the example of the basic usage of an agent, this was used: 

- [Simple Python agent workflow](https://github.com/mistralai/cookbook/blob/main/mistral/agents/simple_Python_agent_workflow.ipynb)

In case the code is not avail, this is how it must be created:


You can create an Agent in [Mistral Agent console](https://console.mistral.ai/build/agents/new), for this notebook we will use mistral-large-2407 as the model powering our agents!

Here is the instruction provided to the Python agent we create:

``` 
You are a Python coding assistant that only outputs Python code without any explanations or comments.
 
Return one Python function for the given query and one test case using assertion.
 
Return Python code with two sections:

## Python function

## Test case
```

After we create the agent, we will retrieve the Agents ID from the UI where we created the agent

For now calling the function and test:

```
python3 mistralai_basic_agent.py "How can I remove duplicates from a list"
python3 mistralai_basic_agent.py "How can I sort a list of words and add the word love to each of word"
python3 mistralai_basic_agent.py "How can calculate Fibonacci"
```

# Add Mistral key

Copy .env.example to .env (if you provide an example).
Add their Mistral API key to .env.

## Setup and Dependencies

To install all required dependencies, run the following command in your project root directory:

```bash
pip install -r requirements.txt
```

# Extract sections from PDF

This program automates the extraction of structured sections (titles and content) from PDF files using Mistral AI, saving the results as JSON for further analysis.

## What it does
- Scans the `data/input/pdf/` directory for PDF files.
- Uses a configurable prompt (from `data/input/settings.yml`) to query Mistral AI for section extraction.
- Outputs a structured JSON file (`section_analysis_<filename>.json`) for each PDF in `data/output/analysis/pdf/`.
- Logs all actions for traceability.

## Prerequisites

Is needed an agent at Mistral console page, go to https://console.mistral.ai/build/agents

Create an agent with data:

- Name: CSV to JSON Converter
- Model: Mistral large
  - temperature: 0.7
  - max_tokens: 2048
  - top_p: 1
- Instructions:

  ```
  You are a CSV to JSON converter agent.
  1. The user will provide CSV content as text (not a file upload).
  2. The user will specify which fields to extract (e.g., "name, age, email").
  3. Use the 'Execute code tool' to run Python code that converts the CSV content to JSON, including only the specified fields.
  4. If the CSV is empty, return an empty JSON object: {"status": "empty", "data": {}}.
  5. If there is an error, return a JSON object with the error description: {"status": "error", "message": "Error details here"}.
  6. If successful, return the JSON data in this format: {"status": "success", "data": [{"field1": "value1", ...}]}.
  ```

Also get the agent's ID to be used in the program, otherwise when running it, an error will be risen.

## How to run

To run the program use the following instruction:

```
bash
python3 mistralai_extract_sections.py
```