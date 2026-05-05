#!/bin/bash

echo " Setting up Log Monitoring System..."

# Create structure
mkdir -p app/{api,core,models,schemas,services}

# Init files
touch app/__init__.py
touch app/api/__init__.py
touch app/core/__init__.py
touch app/models/__init__.py
touch app/schemas/__init__.py
touch app/services/__init__.py

# Install uv
pip install uv

# Create virtual env
uv venv

# Install dependencies
uv pip install fastapi uvicorn sqlalchemy python-dotenv prometheus-client requests

# main.py
cat <<EOF > app/main.py
from fastapi import FastAPI
from app.api.routes import router
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def root():
    return {"status": "running"}
EOF

# database.py
cat <<EOF > app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./logs.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
EOF

# routes.py
cat <<EOF > app/api/routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}
EOF

echo "✅ Setup complete!"
echo "👉 Run server:"
echo "uv run uvicorn app.main:app --reload"