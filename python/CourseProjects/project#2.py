import random


def guess(limit):
    Guesses = 0
    rightNum = random.randint(1, limit)
    while True:
        num = int(input(f"Guess a number between 1 and {limit}: "))
        if num < rightNum:
            print("Wrong: too low")
            Guesses += 1
        elif num > rightNum:
            print("Wrong: too high")
            Guesses +=1
        elif num == rightNum:
            Guesses +=1
            break
    print(f"Correct!!!!\nOnly took you {Guesses} tries.")


guess(100)
