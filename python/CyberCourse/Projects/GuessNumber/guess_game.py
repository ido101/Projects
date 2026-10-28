import random
num = random.randint(1, 100)
guess = int(input("guess num: "))
attempts = 1
while guess != num:
    if guess > num:
        print("go lower")
    else:
        print("go higher")
    guess = int(input("guess num: "))
    attempts += 1
print("good job, you did it in " + str(attempts) + " attempts.")