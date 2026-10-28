import socket
import pathlib


def receive_file(file_name, server_host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_host, server_port))
    s.listen(1)

    print(f"Server is listening on {server_host}:{server_port}...")
    client_socket, client_adress = s.accept()
    print(f"Connection established with {client_adress}") 

    file_path = str(pathlib.Path(__file__).parent.resolve()) + f"\{file_name}"
    with open(file_path, 'wb') as f:
        while True:
            print("Waiting for data...")
            data = client_socket.recv(1024)
            if not data:
                print("file transfer complete.")
                break
            print(f"Received {len(data)} bytes of data.")
            f.write(data)
    s.close()

if __name__ == "__main__":
    file_name = input("Enter the name of the new file: ")
    receive_file(file_name, "127.0.0.1", 8000)