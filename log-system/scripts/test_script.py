import requests
import time
import random

URL = "http://127.0.0.1:8000/logs"

messages = [
    "user login success",
    "payment failed due to timeout",
    "database connection error",
    "service unavailable",
    "request processed"
]

levels = ["info", "warning", "error"]

for i in range(50):
    data = {
        "service": "load-test",
        "level": random.choice(levels),
        "message": random.choice(messages)
    }

    response = requests.post(URL, json=data)
    print(f"Request {i} -> {response.status_code}")

    time.sleep(0.2)