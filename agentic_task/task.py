import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Configure the library with your API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# 2. Read the task file
try:
    with open('tasks.txt', 'r') as f:
        tasks = f.read()
except FileNotFoundError:
    print("Error: tasks.txt not found in the current directory.")
    exit()

# 3. Generate the content
try:
    # Get the generative model (Corrected to a valid model name)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Define a prompt that requests simple text output
    prompt = f"""
Categorize the following list of tasks into three priority levels.
Provide the output as clean, simple text. Do not use any markdown formatting like '#' or '*'.

TASKS:
---
{tasks}
---

Use this exact format for your response:

High Priority:
  - Task description | Reason
  - Another task description

Medium Priority:
  - Task description | Reason

Low Priority:
  - Task description | Reason
"""

    # Make the API call
    response = model.generate_content(prompt)

    # Print the result
    print("\n\n--- Task Priorities ---")
    print("_"*90)
    print(response.text)

except Exception as e:
    print(f"An error occurred during content generation: {e}")
