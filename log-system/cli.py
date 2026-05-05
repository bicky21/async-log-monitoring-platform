import requests

API_URL = "http://127.0.0.1:8000/logs"

data = {
    "service": "cli-tool",
    "level": "error",
    "message": "manual log injection from CLI"
}

response = requests.post(API_URL, json=data)

print(response.json())