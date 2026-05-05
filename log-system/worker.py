from rq import SimpleWorker
from app.core.queue import redis_conn

if __name__ == "__main__":
    worker = SimpleWorker(["default"], connection=redis_conn)
    worker.work()