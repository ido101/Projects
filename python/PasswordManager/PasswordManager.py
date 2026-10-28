import os
from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
password = "Admin_pass"

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

os.chdir(os.path.dirname(os.path.abspath(__file__)))
key = load_key()
fer = Fernet(key)


def view():
    while True:
        guess = input("Whats the password manager's password? ")
        if guess == password:
            break
        else:
            print("Wrong")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: " + user + ", Password: " + fer.decrypt(passw.encode()).decode())
            print()


def add():
    username = input("account name: ")
    password = input("password:")

    with open("passwords.txt", "a") as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("would like to add a new password or view existing one? (view, add)\n"
                 "press q to quit\n>").lower().strip()
    if mode == "q":
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")