import random


def guess(limit):
    guesses = 0
    low_limit = 1
    while True:
        num = random.randint(low_limit, limit)
        answer = input(f"Is {num} too low(L), too high(H), or correct(C)?").lower().strip()
        if answer == "l":
            low_limit = num + 1
            guesses += 1
        if answer == "h":
            guesses += 1
            limit = num - 1
        if answer == "c":
            guesses += 1
            break
    print(f"Yesss I did it. Only took me {guesses} tries")


guess(10000)
