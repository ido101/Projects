import socket


s = socket.socket()
s.connect(("127.0.0.1", 12716))
print(s.recv(1024))
