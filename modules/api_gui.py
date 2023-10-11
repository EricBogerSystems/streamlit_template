
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
        gui_thread = threading.Thread(target=self._thread_ipc, daemon=True) 
        gui_thread.start()
        return True

    def close(self):
        return

    def _thread_ipc(self):
        while True:

            sleep(0.01)
        

"""
#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send_string("Hello")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
"""