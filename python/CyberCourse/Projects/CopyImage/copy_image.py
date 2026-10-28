import os

name = input("Enter Image file name: ")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(name, "rb") as img:
    data = img.read()

new_name = "Copy" + name
with open(new_name, "wb") as img:
    img.write(data)