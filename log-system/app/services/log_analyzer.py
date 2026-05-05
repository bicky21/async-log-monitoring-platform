def analyze_log(message: str, level: str):
    severity = "LOW"

    if level.lower() == "error":
        severity = "HIGH"
    elif level.lower() == "warning":
        severity = "MEDIUM"

    keywords = ["failed", "exception", "timeout", "critical"]

    for word in keywords:
        if word in message.lower():
            severity = "HIGH"
            break

    return {"severity": severity}
def process_log(log_id: int):
    from app.core.database import SessionLocal
    from app.models.log import Log
    import time

    db = SessionLocal()
    log = db.query(Log).filter(Log.id == log_id).first()

    if not log:
        return

    time.sleep(2)

    analysis = analyze_log(log.message, log.level)
    log.severity = analysis["severity"]

    db.commit()

    # Trigger alert
    send_alert(log)

    db.close()