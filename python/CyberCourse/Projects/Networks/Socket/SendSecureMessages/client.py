import socket
import ssl

def start_echo_client(server_host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = ssl.wrap_socket(s)
    ssl_socket.connect((server_host, server_port))
    print(f"Client has connected to {server_host}:{server_port}")
    while True:
        message = input("Enter a message to send to the server: ")
        if message.lower() == "exit":
            print("Exiting the client.")
            break

        ssl_socket.sendall(message.encode('utf-8'))
        print("Waiting for a response from the server...")
        data = ssl_socket.recv(1024)
        print(f"Received data from server:{data.decode('utf-8')}")
    ssl_socket.close()

if __name__ == "__main__":
    start_echo_client("127.0.0.1", 8000)