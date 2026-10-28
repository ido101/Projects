import random
guess = 0
num = 0


def wants_to_play(greeting_message):
    want_to_play = input(greeting_message+"('y' for yes, 'n' for no)\n").lower().strip()
    if want_to_play == "y":
        pass
    elif want_to_play == ' n':
        print("Bye")
        quit()
    else:
        while want_to_play not in ['y', 'n']:
            want_to_play = input("Please pick an option!\n").lower().strip()
            if want_to_play == 'n':
                print("Bye")
                quit()


wants_to_play("Do you want to play?")

while True:
    num = random.randint(1, 100)
    while guess != num:
        guess = int(input("Guess a number between 1-100\n"))
        while guess not in list(range(1, 101)):
            guess = int(input("Please enter a valid number\n"))
        if guess > num:
            print("the number is lower")
        elif guess < num:
            print("the number is higher")
    print("Good job!")
    wants_to_play("Do you want to play again?")
