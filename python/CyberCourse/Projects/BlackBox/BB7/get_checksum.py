import subprocess
import os, pathlib

p = pathlib.Path("C:/Users/IDO123/Downloads/blackbox7/secret2")
print(pathlib.Path.cwd())
os.chdir(p)
print(pathlib.Path.cwd())

def brute_force_checksum():
    for i in range(301):
        print(f"Trying Checksum:{i}")
        res = subprocess.run(["secret2.exe"], input=str(i), text=True, capture_output=True)
        res.stdout = res.stdout.strip()
        print(f"stdout:{res.stdout.strip()}")
        if "Wrong checksum!" not in res.stdout.strip():
            break

if __name__ == "__main__":
    brute_force_checksum()