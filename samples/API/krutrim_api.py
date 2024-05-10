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
    'model': os.getenv('MODEL'),
    'messages': [{"role": "user", "content": "Write an email to your Manager asking for a leave of one day"}],
    'max_tokens': 256,
    'temperature': 0.1,
    'stop': ['agent'],
    'logprobs': True,
    'top_logprobs': 1,
    'logit_bias': {2435:-100, 640:-100},
}


# Making a POST request to the Krutrim API with headers and data
print('\nRequesting Model...')
print('#'*80)
response = requests.post(url, headers=headers, json=data)
try:
    print('Model Response:', response.json()['choices'][0], sep = '\n')
except:
    print(f'Error in response: [{response.status_code}] {response.content}')
print('#'*80)
