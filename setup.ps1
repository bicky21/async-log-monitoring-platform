# setup.ps1

Write-Host "Setting up Log Monitoring System..."

# Create project structure
mkdir app, app\api, app\core, app\models, app\schemas, app\services

# Create __init__.py files
New-Item app\__init__.py
New-Item app\api\__init__.py
New-Item app\core\__init__.py
New-Item app\models\__init__.py
New-Item app\schemas\__init__.py
New-Item app\services\__init__.py

# Install uv if not installed
pip install uv

# Create virtual environment
uv venv

# Install dependencies
uv pip install fastapi uvicorn sqlalchemy python-dotenv prometheus-client requests

# Create main.py
@"
from fastapi import FastAPI
from app.api.routes import router
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def root():
    return {"status": "running"}
"@ | Out-File -Encoding utf8 app\main.py

# Create database.py
@"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./logs.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
"@ | Out-File -Encoding utf8 app\core\database.py

# Create minimal routes.py
@"
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}
"@ | Out-File -Encoding utf8 app\api\routes.py

Write-Host "✅ Setup complete!"
Write-Host "👉 Run server with:"
Write-Host "uv run uvicorn app.main:app --reload"