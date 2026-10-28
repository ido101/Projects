import requests
import socket
r = requests.get("http://127.0.0.1:5000")
print(r.text)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
