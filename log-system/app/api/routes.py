from fastapi import APIRouter, Depends
from app.services.log_analyzer import analyze_log
from sqlalchemy.orm import Session
from app.schemas.log import LogCreate
from app.models.log import Log
from app.api.deps import get_db
from fastapi import BackgroundTasks
from app.services.log_analyzer import analyze_log
from app.services.alert_service import send_alert
from app.services.log_processor import process_log
from app.models.bug import Bug
from app.core.queue import queue

router = APIRouter()

@router.post("/logs")
def create_log(
    log: LogCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    # Step 1: Store initial log (without severity)
    new_log = Log(
        service=log.service,
        level=log.level,
        message=log.message,
        severity="LOW"
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    # Step 2: Background processing
    queue.enqueue(process_log, new_log.id)

    return new_log

@router.get("/logs/{service}")
def get_logs_by_service(service: str, db: Session = Depends(get_db)):
    return db.query(Log).filter(Log.service == service).all()
    
@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(Log).all()

@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    logs = db.query(Log).all()

    total_logs = len(logs)
    high = len([l for l in logs if l.severity == "HIGH"])
    medium = len([l for l in logs if l.severity == "MEDIUM"])
    low = len([l for l in logs if l.severity == "LOW"])

    return {
        "total_logs": total_logs,
        "high_severity": high,
        "medium_severity": medium,
        "low_severity": low
    }

@router.get("/bugs")
def get_bugs(db: Session = Depends(get_db)):
    return db.query(Bug).all()

@router.put("/bugs/{bug_id}")
def update_bug(bug_id: int, status: str, db: Session = Depends(get_db)):
    bug = db.query(Bug).filter(Bug.id == bug_id).first()

    if not bug:
        return {"error": "Bug not found"}

    bug.status = status
    db.commit()

    return bug