# Krutrim API
The Krutrim inference services exposes Chat Completion endpoint that is fully compatible with the OpenAI standards. You can use the API either:

## Using `curl`

```bash
curl https://cloud.olakrutrim.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <KRUTRIM-API-KEY>" \
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
    "max_tokens": 256,
    "frequency_penalty": 0,
    "logit_bias": {"2435":-100, "640":-100},
    "logprobs": true,
    "top_logprobs": 1,
    "n": 1,
    "presence_penalty": 0,
    "response_format": { "type": "text" },
    "stop": null,
    "stream": false,
    "temperature": 0,
    "top_p": 1
  }'
```
## Using Python `requests`

```bash
python3 krutrim_api.py
```
