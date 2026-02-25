from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from sorter import sort_file
from pathlib import Path

class MiHandler(FileSystemEventHandler):
    def __init__(self, carpeta):
        self.carpeta = carpeta

    def on_created(self, event):
        if event.is_directory:
            pass
        else:
            sort_file(self.carpeta, Path(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            pass
        else:
            sort_file(self.carpeta, Path(event.src_path))

    def on_moved(self, event):
        if event.is_directory:
            pass
        else:
            sort_file(self.carpeta, Path(event.src_path))



    
    
