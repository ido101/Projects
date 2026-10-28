import hashlib
import os

os.chdir("BruteForceFile")
hashed_pass = "0d107d09f5bbe40cade3de5c71e9e9b7"
with open("famousPass.txt", "r") as f:
    for line in f:
        guess = hashlib.md5(line.strip().encode()).hexdigest()
        print(f"{line.strip()} : {guess}")
        if hashed_pass == guess:
            psw = line.strip()
            print(f"Admin password found: {psw}")
            break
print(f"Rotated password: {psw[::-1]}")