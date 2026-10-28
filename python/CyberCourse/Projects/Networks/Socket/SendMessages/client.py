import socket

def start_echo_client(server_host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_host, server_port)) 
    print(f"Client has connected to {server_host}:{server_port}")
    while True:
        message = input("Enter a message to send to the server: ")
        if message.lower() == "exit":
            print("Exiting the client.")
            break

        s.sendall(message.encode('utf-8'))
        print("Waiting for a response from the server...")
        data = s.recv(1024)
        print(f"Received data from server:{data.decode('utf-8')}")
    s.close()

if __name__ == "__main__":
    start_echo_client("127.0.0.1", 8000)