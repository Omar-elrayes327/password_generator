import json
import os
from config import PASSWORD_FILE

def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_passwords(data):
    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)