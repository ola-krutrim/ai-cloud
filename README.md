# Krutrim AI Cloud Inference Services

Welcome to the introduction to Krutrim OpenAI-Compatible Chat Completion APIs! This repository consists of sample code to interact with the Krutrim Chat Completion APIs.

## Supported Models

We provide a range of pre-trained AI models optimized for various inference tasks.

| Model Name | Max Model Length (tokens) |
|------|------|
| Meta-Llama-3-8B-Instruct | 8K |
| Mistral-7B-Instruct | 8K |
| Krutrim-spectre-v2 | 4K |

## Krutrim API Keys
Getting started with our AI Cloud Inference Services is easy! Follow these steps to quickly set up and start using our platform:

- **Sign up**: Register for an [account](https://cloud.olakrutrim.com) on our platform to get access to the AI Cloud Inference Services
- **API Keys**: Obtain API keys or credentials required for authentication.


## Prerequisites

Before you begin, ensure that you have the following:
- Python 3.10+ installed on your system
- A Krutrim API key

## Installation

### 1. **Clone the Repository** 

```bash
git clone <krutrim-repository>
```

### 2. **Install Dependencies**

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
Install the required Python packages:

```bash
pip3 install -r requirements.txt
```

## Configuration
To configure your application, you'll need to set up your Krutrim API key. 

You can do this by setting the `API_KEY` environment variable

-  In the [sample.env](./sample.env) and rename the file to `.env`:

**OR**

- Using `export`:

```bash
export API_KEY='your-api-key'
```



## Krutrim OpenAI SDK

The Krutrim OpenAI SDK demonstrates interaction with the krutrim hosted inference services using OpenAI SDK. To execute the sample, use the following command

```bash
python3 krutrim_openai_sdk.py
```

## Krutrim API
The Krutrim inference services exposes Chat Completion endpoint that is fully compatible with the OpenAI standards. You can use the API either:

### Using `curl`

```bash
curl https://cloud.olakrutrim.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <KRUTRIM_API_KEY>" \
  -d '{
    "model": "Krutrim-spectre-v2",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "frequency_penalty": 0,
    "logit_bias": {2435:-100, 640:-100},
    "logprobs": true,
    "top_logprobs": 2,
    "max_tokens": 256,
    "n": 1,
    "presence_penalty": 0,
    "response_format": { "type": "text" },
    "stop": null,
    "stream": false,
    "temperature": 0,
    "top_p": 1
  }'
```

### Using Python `requests`
```bash
python3 krutrim_api.py
```

## Krutrim-hosted Inference Services using `Langchain`
Krutrim APIs can be seamlessly integrated with Langchain. Please refer to the [Notebook](./krutrim_langchain.ipynb).
