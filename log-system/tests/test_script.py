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

request_count = 0

while True:
    try:
        data = {
            "service": random.choice(["auth", "payment", "db", "api"]),
            "level": random.choice(levels),
            "message": random.choice(messages)
        }

        response = requests.post(URL, json=data)

        request_count += 1
        print(f"Request {request_count} -> {response.status_code}")

        # Random delay (realistic traffic)
        time.sleep(random.uniform(0.05, 3))

    except KeyboardInterrupt:
        print("\nStopped by user")
        break

    except Exception as e:
        print(f"Error: {e}")