import random
secret_number = random.randint(1, 5)
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Guess a number between 1-5: "))
    guess_count += 1
    if guess == secret_number:
        print("you got it!")
        answer = input("would you like to play again?(type 'y' for yes and 'n' for no)\n").strip().lower()
        if answer == "y":
            secret_number = random.randint(1, 5)
            guess_count = 1
        else:
            quit()
    else:
        print("wrong")
else:
    print(f"sorry you failed! the number was {secret_number}")
