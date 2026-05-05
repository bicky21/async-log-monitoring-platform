from fastapi import FastAPI
from app.api.routes import router
from app.core.database import Base, engine
from app.models import bug
from prometheus_client import Counter
from fastapi import Request
from prometheus_client import generate_latest
from fastapi.responses import Response


# 1. CREATE APP FIRST
app = FastAPI()

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API Requests",
    ["method", "endpoint"]
)

@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()
    return response


# 2. INIT DATABASE
Base.metadata.create_all(bind=engine)

# 3. REGISTER ROUTES
app.include_router(router)

# 4. OPTIONAL ROOT
@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")