import requests
import os


# Importing the function to load environment variables
from dotenv import load_dotenv  

# Load environment variables from .env file
load_dotenv()

# Fetching base URL and API key from environment variables
url = os.getenv('BASE_URL') + '/chat/completions'
key = os.getenv('API_KEY')

# Setting up request headers with API key
headers = {"Authorization": f"Bearer {key}"}

# Data payload for the API request
data = {
    'model': 'Meta-Llama-3-8B-Instruct',
    'messages': [{"role": "user", "content": "write an email in tamil"}],
    'temperature': 0,
    'max_tokens': 52,
    'stop': ["agent"],
    'logprobs': True,
    'top_logprobs': 5,
    'use_beam_search': True,
    'best_of': 6
}

# Making a POST request to the Krutrim API with headers and data
response = requests.post(url, headers=headers, json=data)

# Printing the response status code
print('#'*80)
print('Response Status Code', response.status_code)

# Printing the response from the Model
print('#'*80)
print('Model Response:', response.json()['choices'][0], sep = '\n')
print('#'*80)