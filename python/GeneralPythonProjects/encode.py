from cryptography.fernet import Fernet
password = "Ido123!"
pwd = input("what is the password?\n")
if pwd != password:
    print("you dont know it! get out!")
    quit()


def get_key():
    file = open("/Users/IDO123/History/revolution", "rb")
    pass_key = file.read()
    file.close()
    return pass_key


key = get_key()
fer = Fernet(key)


def geturl():
    with open('/Users/IDO123/History/coded', 'r') as file:
        x = 0
        for line in file.readlines():
            x += 1
            data = line.rstrip()
            data = data.strip("123456789. ")
            contents_decrypted = fer.decrypt(data.encode()).decode()
            print(str(x) + ". " + contents_decrypted)
        print("\n")


def add_url():
    url = input("what url:\n")
    with open('/Users/IDO123/History/coded', 'r+') as file:
        lines = file.readlines()
        contents_encrypted = fer.encrypt(url.encode()).decode() + "\n"
        file.write(str(len(lines)+1) + ". " + contents_encrypted)


def delete_url():
    num = int(input("what url number do you want to delete:\n"))
    with open('/Users/IDO123/History/coded', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        x = 0
        for i in lines:
            x += 1
            if x != num:
                file.write(i)
        file.truncate()


while True:
    action = input("what do you want to do?\n-view\n-add\n-quit\n-delete\n>").lower().strip()
    if action == "add":
        add_url()
    elif action == "view":
        geturl()
    elif action == "quit":
        quit()
    elif action == "delete":
        delete_url()
