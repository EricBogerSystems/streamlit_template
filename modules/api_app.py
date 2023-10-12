
import threading
import subprocess
import zmq
import json
from time import sleep

class API_APP:
    _app_name = None
    _gui_name = None
    _zmq_context = None
    _zmq_socket = None

    def __init__(self):
        self._app_filename = None
        self._gui_filename = None
        self._process_streamlit = None
        self._zmq_context = zmq.Context()
        self._zmq_socket = self._zmq_context.socket(zmq.REP)

    def run(self, args):
        self._app_filename = args.prog
        self._gui_filename = args.prog.replace('.py', '_gui.py')
        gui_thread = threading.Thread(target=self._thread_gui, daemon=True) 
        gui_thread.start()
        ipc_thread = threading.Thread(target=self._thread_ipc, daemon=True)
        ipc_thread.start()
        self._zmq_socket.bind('tcp://*:5555') 
        return True

    def close(self):
        if self._process_streamlit != None:
            self._process_streamlit.kill()
        return True

    def _thread_gui(self):
        cmd = 'streamlit run ' + self._gui_filename
        self._process_streamlit = subprocess.Popen(cmd, shell=True)
       
    def _thread_ipc(self):
        cnt = 0
        txmsg = { }
        txmsg['CMD'] = {'ACK':True, 'CNT':0}

        while True:
            sleep(0.01)

            # receive request message (from GUI)
            rxmsg = json.loads(self._zmq_socket.recv_string())
            print(rxmsg)
            
            # send response (to GUI)
            cnt += 1
            txmsg['CMD']['CNT'] = cnt
            self._zmq_socket.send_string(json.dumps(txmsg))

