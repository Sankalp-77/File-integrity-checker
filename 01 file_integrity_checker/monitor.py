import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hash_utils import calculate_hash
from logger import log_event
from email_alert import send_email_alert

DB_FILE = "database.json"

def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, algorithm):
        self.db = load_db()
        self.algorithm = algorithm

    def process(self, file_path):
        if not os.path.isfile(file_path):
            return

        new_hash = calculate_hash(file_path, self.algorithm)
        old_hash = self.db.get(file_path)

        if old_hash:
            if new_hash != old_hash:
                msg = f"MODIFIED: {file_path}"
                print(msg)
                log_event(msg)
                send_email_alert(msg)
        else:
            msg = f"NEW FILE: {file_path}"
            print(msg)
            log_event(msg)

        self.db[file_path] = new_hash
        save_db(self.db)

    def on_modified(self, event):
        self.process(event.src_path)

    def on_created(self, event):
        self.process(event.src_path)

def start_monitoring(path, algorithm):
    event_handler = FileMonitorHandler(algorithm)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"[+] Monitoring started on {path} using {algorithm}")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()