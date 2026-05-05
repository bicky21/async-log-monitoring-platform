import requests
import time
import random
import threading

URL = "http://127.0.0.1:8000/logs"

MESSAGES = [
    "user login success",
    "payment failed due to timeout",
    "database connection error",
    "service unavailable",
    "request processed",
    "disk failure detected",
    "cache miss error",
    "timeout occurred"
]

LEVELS = ["info", "warning", "error"]

THREADS = 5
REQUEST_TIMEOUT = 5
MAX_RETRIES = 3

request_count = 0
lock = threading.Lock()


def send_request(data):
    for _ in range(MAX_RETRIES):
        try:
            response = requests.post(URL, json=data, timeout=REQUEST_TIMEOUT)
            return response.status_code
        except requests.exceptions.RequestException:
            time.sleep(0.2)
    return "FAILED"


def worker(thread_id):
    global request_count

    while True:
        data = {
            "service": f"service-{thread_id}",
            "level": random.choice(LEVELS),
            "message": random.choice(MESSAGES)
        }

        status = send_request(data)

        with lock:
            request_count += 1
            count = request_count

        print(f"[T{thread_id}] Request {count} -> {status}")

        time.sleep(random.uniform(0.1, 0.4))


def burst_mode():
    while True:
        time.sleep(random.randint(10, 20))

        for _ in range(50):
            data = {
                "service": "burst",
                "level": "error",
                "message": "burst failure"
            }
            send_request(data)


def main():
    threads = []

    for i in range(THREADS):
        t = threading.Thread(target=worker, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)

    burst_thread = threading.Thread(target=burst_mode)
    burst_thread.daemon = True
    burst_thread.start()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()