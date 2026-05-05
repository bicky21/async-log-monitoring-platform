def send_alert(log):
    if log.severity == "HIGH":
        print(f"[ALERT] High severity log detected: {log.message}")