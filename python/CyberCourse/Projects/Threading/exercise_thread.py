import threading

counter = 0

def func():
    global counter
    for i in range(100000):
        counter += 1

def func2():
    global counter
    for i in range(100000):
        counter -= 1

my_thread = threading.Thread(target=func)
my_thread2 = threading.Thread(target=func2)

my_thread.start()
my_thread2.start()

my_thread.join()
my_thread2.join()
print("Final counter value:", counter)