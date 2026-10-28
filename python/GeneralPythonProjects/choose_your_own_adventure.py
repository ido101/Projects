import time

name = input("Type your name: ")
print("Welcome " + name + " to this adventure.")

answer = input("You're on a road. It has come to an "
               "end and you can go left or right. Which way do you want to go? ").lower().strip()
if answer not in ["left", "right"]:
    print("Please pick a way.")
    while True:
        answer = input().lower().strip()
        if answer not in ["left", "right"]:
            print("Please pick a way.")
        else:
            break

if answer == "left":
    answer = input("You've come to a river, you can walk around it or swim "
                   "across.\nType walk to walk around and swim to swim across: ").lower().strip()

    if answer not in ["swim", "walk"]:
        print("Please pick an option.")
        while True:
            answer = input().lower().strip()
            if answer not in ["swim", "walk"]:
                print("Please pick an option.")
            else:
                break

    if answer == "swim":
        print("You swam across, got eaten by an alligator and lost the game.Goodbye!")
        time.sleep(3)
        quit()
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game. Goodbye!")
        time.sleep(3)
        quit()

elif answer == "right":
    answer = input("You've come to a bridge. It looks wobbly, do you want to cross it or head back?\n"
                   " Type cross to cross it and head to head back.").lower().strip()

    if answer not in ["cross", "head"]:
        print("Please pick an option.")
        while True:
            answer = input().lower().strip()
            if answer not in ["cross", "head"]:
                print("Please pick an option.")
            else:
                break

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them?\n"
                       "Type yes or no: ").lower().strip()
        if answer not in ["yes", "no"]:
            print("Please pick an option.")
            while True:
                answer = input().lower().strip()
                if answer not in ["yes", "no"]:
                    print("Please pick an option.")
                else:
                    break

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger, they are offended and you lose. Goodbye!")
            time.sleep(3)

    elif answer == "head":
        print("You go back and lose. Goodbye!")
        time.sleep(3)
        quit()
