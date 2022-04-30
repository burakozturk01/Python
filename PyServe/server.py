import socket
import threading
import time as t

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONN_MSG = "!DISCONN"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conns = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        t.sleep(0.01)
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONN_MSG:
                connected = False
                print(f"[{addr}] Disconnected\n")
            else:
                print(f"[{addr}] {msg}\n")
    
    conns.remove(conn)
    conn.close()


def start():
    server.listen()
    print(f"[WAITING] Server IP is {SERVER}\n")
    threading.Thread(target=send, args=()).start()
    while 1:
        t.sleep(0.01)
        conn, addr = server.accept()
        conns.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] There are {threading.activeCount() - 1} connection(s)\n")


def send():
    while 1:
        t.sleep(0.01)
        if len(conns) > 0:
            ind = input("Index: \n")
            ind = int(ind)
            if ind < len(conns):
                inp = input("Message: \n")
                if inp == "/kick":
                    to_kick = conns[ind]
                    conns.remove(to_kick)
                    to_kick.close()
                else:
                    conns[ind].send(inp.encode(FORMAT))


print("[STARTING]...")
start()
