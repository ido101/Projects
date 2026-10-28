import random
score = 0
while True:
    number = random.randint(1, 5)
    usrnum = input("guess a number between 1-5:\n")
    if usrnum.isdigit():
        usrnum = int(usrnum)
        if usrnum > 5 or usrnum < 1:
            print("please type a number between 1-5")
            continue
    else:
        print("please type a number")
        continue
    if number == usrnum:
        print("you got it correct!")
        score += 1
    else:
        print("you got it wrong noob\n" + "the correct answer is " + str(number))
    print("you got " + str(score) + " guesses correct so far")
    play_again = input("do you want to try again with a new number?\n")
    if play_again.lower().strip() != "yes":
        print("bye")
        quit()
