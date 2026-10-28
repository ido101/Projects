import time


# fibonacci series up to n
def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


# a new number from fibonacci series every second
def fibo():
    a = 0
    b = 1
    while True:
        print(a, end=' ')
        a, b = b, a + b
        input("press enter to continue")

if __name__ == "__main__":
    fibo()
    