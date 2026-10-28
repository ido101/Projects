import random


def r(n):
    l = []
    t = 1
    for i in range(1, len(str(n)) + 1):
        t *= i
    num = ""
    for i in range(t):
        letter_list = list(str(n))
        num = ""
        for j in range(len(str(n))):
            choice = random.choice(letter_list)
            num += choice
            letter_list.remove(choice)
        while num in l:
            letter_list = list(str(n))
            num = ""
            for j in range(len(str(n))):
                choice = random.choice(letter_list)
                num += choice
                letter_list.remove(choice)
        l.sort()
        l.append(num)
    return l


print(r(1234))