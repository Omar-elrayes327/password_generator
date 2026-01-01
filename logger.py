import os
from datetime import datetime
from config import LOG_FILE

def log_action(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {message}\n")