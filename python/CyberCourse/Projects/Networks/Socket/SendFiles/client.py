import socket

def send_file(file_path, server_host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_host, server_port))
    print(f"Client has connected to {server_host}:{server_port}")
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                print("File transfer complete.")
                break
            print(f"Sending {len(data)} bytes...")
            s.sendall(data)
    s.close()
    print("Connection closed.")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to send: ")
    send_file(file_path, "127.0.0.1", 8000)