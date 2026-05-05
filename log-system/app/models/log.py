from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, index=True)
    level = Column(String, index=True)
    message = Column(String)
    severity = Column(String, default="LOW") 
    timestamp = Column(DateTime, default=datetime.utcnow)