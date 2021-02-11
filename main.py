from socket_client import SocketClient

s = SocketClient('127.0.0.1', 65432)

s.connect()

s.start_sending(5)