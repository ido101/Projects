from random import randint

player_wins = 0
computer_wins = 0
while True:
    types = ["rock", "paper", "scissors"]
    comp_guess = types[randint(0, 2)]
    usrguess = input("type rock, paper or scissors or Q to quit:\n").lower().strip()
    if usrguess not in ["rock", "paper", "scissors", "q"]:
        print("please pick one of the options")
        continue
    elif usrguess == "q":
        quit()

    print("the computer chose " + comp_guess + "!")
    if usrguess == "rock" and comp_guess == "scissors":
        print("you win!")
        player_wins += 1
    elif usrguess == "rock" and comp_guess == "paper":
        print("you lose:(")
        computer_wins += 1
    elif usrguess == "scissors" and comp_guess == "paper":
        print("you win!")
        player_wins += 1
    elif usrguess == "scissors" and comp_guess == "rock":
        print("you lose:(")
        computer_wins += 1
    elif usrguess == "paper" and comp_guess == "scissors":
        print("you lose:(")
        computer_wins += 1
    elif usrguess == "paper" and comp_guess == "rock":
        print("you win!")
        player_wins += 1
    elif usrguess == "rock" and comp_guess == "rock":
        print("tie")
    elif usrguess == "paper" and comp_guess == "paper":
        print("tie")
    else:
        print("tie")
    print("* you won: " + str(player_wins) + " times \n* the computer won: " + str(computer_wins) + " times")
