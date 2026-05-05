from pydantic import BaseModel

class LogCreate(BaseModel):
    service: str
    level: str
    message: str