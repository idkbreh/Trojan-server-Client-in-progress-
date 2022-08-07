from http import server
from pydoc import cli
import socket
import os
import threading

HOST = '192.168.1.38'
PORT = 1111
ADDR = (HOST,PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

conn, addr = server.accept()

while True:
    print(f"Connected {addr}")
    cmd = input("enter cmd : ")
    conn.send(cmd.encode("uft-8"))
