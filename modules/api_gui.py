
import threading
import zmq
import json
from time import sleep

class API_GUI:
    app_name = None
    gui_name = None

    def __init__(self):
        self.app_filename = None
        self.gui_filename = None
        self._zmq_context = zmq.Context()
        self._zmq_socket = self._zmq_context.socket(zmq.REQ)

    def run(self, args):
        gui_thread = threading.Thread(target=self._thread_ipc, daemon=True) 
        gui_thread.start()
        self._zmq_socket.connect("tcp://localhost:5555")
        return True

    def close(self):
        return True

    def _thread_ipc(self):
        cnt = 0
        txmsg = { }
        txmsg['CMD'] = {'UPDATE':True, 'CNT':0}

        while True:
            sleep(1.0)
            
            # send request (to APP)
            cnt += 1
            txmsg['CMD']['CNT'] = cnt
            self._zmq_socket.send_string(json.dumps(txmsg))

            # receive response (from APP)
            rxmsg = json.loads(self._zmq_socket.recv_string())
            print(rxmsg)
            
