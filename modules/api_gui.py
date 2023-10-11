
import threading
import os
from time import sleep

class API_App:
    app_name = None
    gui_name = None

    def __init__(self):
        self.app_filename = None
        self.gui_filename = None

    def run(self, args):
        gui_thread = threading.Thread(target=self._thread_ipc, daemon=True) 
        gui_thread.start()
        return True

    def close(self):
        return

    def _thread_ipc(self):
        while True:

            sleep(0.01)
        
