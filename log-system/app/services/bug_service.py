from app.models.bug import Bug

def create_bug_from_log(log, db):
    if log.severity != "HIGH":
        return None

    bug = Bug(
        title=f"Issue in {log.service}",
        description=log.message,
        severity=log.severity
    )

    db.add(bug)
    db.commit()
    db.refresh(bug)

    return bug