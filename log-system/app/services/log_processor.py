from app.core.database import SessionLocal
from app.models.log import Log
from app.services.log_analyzer import analyze_log
from app.services.alert_service import send_alert
import time
from app.services.bug_service import create_bug_from_log

def process_log(log_id: int):
    db = SessionLocal()

    log = db.query(Log).filter(Log.id == log_id).first()

    if not log:
        return

    # simulate delay
    time.sleep(2)

    analysis = analyze_log(log.message, log.level)
    log.severity = analysis["severity"]

    db.commit()
    create_bug_from_log(log, db)
    send_alert(log)

    send_alert(log)

    db.close()