
import threading
import os


class API_App:
    app_name = None
    gui_name = None

    def __init__(self):
        self.app_filename = None
        self.gui_filename = None

    def run(self, args):
        self.app_filename = args.prog
        self.gui_filename = args.prog.replace('.py', '_gui.py')
        gui_thread = threading.Thread(target=self._thread_gui, daemon=True) 
        gui_thread.start()
        return True

    def close(self):
        return

    def _thread_gui(self):
        os.system('streamlit run ' + self.gui_filename)
        
