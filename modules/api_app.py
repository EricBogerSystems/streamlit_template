
import threading
import os
import zmq
from time import sleep


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
        ipc_thread = threading.Thread(target=self._thread_ipc, daemon=True)
        ipc_thread.start()
        return True

    def close(self):
        return

    def _thread_gui(self):
        os.system('streamlit run ' + self.gui_filename)
        
    def _thread_ipc(self):
        while True:
            sleep(0.01)


"""
#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("World")
"""