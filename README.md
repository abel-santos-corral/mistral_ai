# Mistral AI
Mistral AI repository is used to make testing developments in python for Mistral.

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

> ``` 
> You are a Python coding assistant that only outputs Python code without any explanations or comments.
> 
> Return one Python function for the given query and one test case using assertion.
> 
> Return Python code with two sections:
> 
> ## Python function
> 
> ## Test case
> 
> ```

After we create the agent, we will retrieve the Agents ID from the UI where we created the agent

For now calling the funciton and test:

```
python3 mistralai_basic_agent.py "How can I remove duplicates from a list"
python3 mistralai_basic_agent.py "How can I sort a list of words and add the word love to each of word"
python3 mistralai_basic_agent.py "How can calculate Fibonacci"
```

# Add Mistral key

Copy .env.example to .env (if you provide an example).
Add their Mistral API key to .env.