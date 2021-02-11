import json
import random
import socket
import time


class SocketClient:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        self.socket.connect((self.host, self.port))

    def start_sending(self, number_sending=-1, time_laps=5):
        i = 0
        try:
            while True:
                data = generate_data()
                self.socket.send(json.dumps(data).encode())
                print(f"data send: {data}")
                time.sleep(time_laps)
                i += 1
                if number_sending > 0:
                    if i == number_sending:
                        break
        except KeyboardInterrupt:
            print("[!] Keyboard Interrupted!")
            pass

        self.socket.close()


def generate_data():
    mac = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255))

    rssi = str(random.randint(-100, 0))

    return {
        "mac": mac,
        "rssi": rssi
    }
