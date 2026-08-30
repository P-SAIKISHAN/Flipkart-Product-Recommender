import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY not found in .env file.")
    exit(1)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
    if response.status_code == 200:
        models = response.json().get("data", [])
        print("\nAvailable Groq Models:")
        for model in models:
            print(f"- {model.get('id')}")
    else:
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"Failed to fetch models: {e}")
