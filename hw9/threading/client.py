from queue import Queue
import socket
import sys
import time

HOST, PORT = "localhost", 8000
q = Queue()

def fetch():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    data = input("Client: ")
    if data == "q":
        exit()
    else:
        sock.sendall(bytes(data+"\n", 'utf-8'))
        rcv = str(sock.recv(1024), "utf-8")[1:]
        if rcv:
            q.put(rcv)
    sock.close()

# Create a socket (SOCK_STREAM means a TCP socket)
if __name__ == "__main__":
    fetch()
    while True:
        if q.not_empty:
            print(q.get())
        else: 
            break
