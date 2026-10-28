import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 8000))
print("client has connected to server on port 8000...")

with open("sender.txt", "r") as f:
    data = f.read()

filesize = os.path.getsize("sender.txt")
s.send(filesize.to_bytes(4, byteorder="big"))
s.sendall(data.encode())

