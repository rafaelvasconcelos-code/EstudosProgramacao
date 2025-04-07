import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.x.ai/v1/chat/completions"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer xai-GaQkiizgeY4QHKsJGdBE9g0RtTACBOzZOvSY7iWuhTutjKFZIl2FkEmuKSBXhDfQG1ti0GK3YhEOiyjS"

data = """
{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and nothing else."
    }
  ],
  "model": "grok-2-latest",
  "stream": false,
  "temperature": 0
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.text)