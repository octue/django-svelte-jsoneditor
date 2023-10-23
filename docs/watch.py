import os
import subprocess
import time
from datetime import datetime
import throttle
from watchdog.events import FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer


MAX_CALLS = 1
MIN_PERIOD_BETWEEN_CALLS = 1


class MonitorFolder(FileSystemEventHandler):
    """Monitors a folder and issues the build-docs pre-commit command on any change"""

    def __init__(self, *args, path="default", **kwargs):
        self._build_docs(path, "Initial build (starting watcher)")
        super().__init__(*args, **kwargs)

    def on_any_event(self, event):
        if isinstance(event, FileModifiedEvent):
            self._build_docs(event.src_path, event.event_type)

    @throttle.wrap(MIN_PERIOD_BETWEEN_CALLS, MAX_CALLS)
    def _build_docs(self, path, event_type):
        print(
            f"""
=========================================
Re-building docs on file/dir change event
Time: {datetime.now().isoformat()}
Event path: {path}
Event type: {event_type}
=========================================
"""
        )

        subprocess.run(
            ["pre-commit", "run", "--all-files", "-vvv", "build-docs"],
            check=False,
        )


if __name__ == "__main__":
    src_path = os.path.join(os.path.dirname(__file__), "source")
    event_handler = MonitorFolder(path="src_path")
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    print(
        f"""
============================================
Started monitoring of {src_path}
============================================
"""
    )

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print(
            f"""
============================================
Stopped monitoring of {src_path}
============================================
"""
        )
