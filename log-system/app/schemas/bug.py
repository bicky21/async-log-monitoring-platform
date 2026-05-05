from pydantic import BaseModel

class BugCreate(BaseModel):
    title: str
    description: str
    severity: str