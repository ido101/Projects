import socket

def start_echo_server(server_host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_host, server_port))
    s.listen(1)

    print(f"Server is listening on {server_host}:{server_port}...")

    client_socket, client_adress = s.accept()
    print(f"Connection established with {client_adress}")  
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data from client:{data.decode('utf-8')}")
        message = input("Enter a message to send back to the client: ")
        client_socket.sendall(message.encode('utf-8'))
        print("Waiting for the next message from the client...")
    print("Closing the connection.")
    s.close()

if __name__ == "__main__":
    start_echo_server("127.0.0.1", 8000)