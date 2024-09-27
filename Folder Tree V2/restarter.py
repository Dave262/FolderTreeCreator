import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gui import App  # Import your existing app

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, app_file):
        self.app_file = app_file

    def on_modified(self, event):
        if event.src_path.endswith(self.app_file):
            print(f"Detected modification in {self.app_file}, reloading app...")
            os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    # Watch gui.py since that's where the app logic is
    app_file = "gui.py"  # Specify the app file explicitly

    observer = Observer()
    handler = ReloadHandler(app_file)

    # Monitor the directory where gui.py is located
    observer.schedule(handler, path=os.path.dirname(os.path.abspath(app_file)), recursive=False)
    observer.start()

    try:
        app = App()  # Run your app from gui.py
        app.mainloop()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

