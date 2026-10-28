import time
print("What do you wanna do?\ns - start the clock\nq - quit")
started = False
while True:
    p = input(">").lower()
    if p == "q":
        quit("Bye")
    if p == "s" and not started:
        started = True
        start = time.time()
        print("The clock has started")
        input("Type anything when you want to stop it.\n-")
        end = time.time()
        t = round(end - start)
        print(f"{t} seconds")
        started = False