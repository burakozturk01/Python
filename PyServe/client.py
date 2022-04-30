import socket
import time as t
import threading as thr

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONN_MSG = "!DISCONN"
EXIT_MSG = "Exit()"
SERVER = "192.168.0.10"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    msg = ""
    while not msg == DISCONN_MSG:
        msg = input()
        if msg == EXIT_MSG:
            msg = DISCONN_MSG
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)


def receive(client):
    coded_msg = 1
    while coded_msg:
        t.sleep(0.01)
        coded_msg = client.recv(2048)
        if coded_msg:
            print(coded_msg.decode(FORMAT))


thr.Thread(target=send, args=()).start()
thr.Thread(target=receive, args=(client,)).start()
