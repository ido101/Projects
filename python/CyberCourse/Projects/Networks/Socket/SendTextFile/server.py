import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(1)
print("Server is listening on port 8000...")

client_socket, client_adress = s.accept()
print(f"Connection established with {client_adress}")

with open("receiver.txt", "w") as f:
    filesize = client_socket.recv(4)
    filesize = int.from_bytes(filesize, byteorder="big")
    received_size = 0
    while received_size < filesize:
        data = client_socket.recv(1024)
        received_size += len(data)
        f.write(data.decode())