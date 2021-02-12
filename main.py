import sys
import os
import socket

from socket_client import SocketClient

HOSTNAME = os.environ.get('HOSTNAME', None)
if HOSTNAME:
    HOST = socket.gethostbyname(HOSTNAME)
else:
    HOST = "127.0.0.1"
PORT = 65432

s = SocketClient(HOST, PORT)

connected = s.connect()
if not connected:
    sys.exit(0)


s.start_sending(5)
