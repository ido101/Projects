import random


def play():
    c_wins = 0
    p_wins = 0
    options = ["rock", "paper", "scissors"]
    while True:
        p_choice = input("What is your choice: Rock(R), Paper(P), Scissors(S), Show current score(C) or Quit(Q)?").lower().strip()
        c_choice = random.choice(options)
        if p_choice == "q":
            break
        elif p_choice == "c":
            print(f"Score:\nComputer - {c_wins}\nPlayer - {p_wins}")
        elif p_choice == c_choice[0]:
            print("We picked the same! No point to anybody")
        elif (p_choice == "r" and c_choice == "scissors") or (p_choice == "s" and c_choice == "paper") or (p_choice == "p" and c_choice == "rock"):
            print(f"You won! computer guessed {c_choice}")
            p_wins += 1
        elif (c_choice == "rock" and p_choice == "s") or (c_choice == "scissors" and p_choice == "p") or (c_choice == "paper" and p_choice == "r"):
            print(f"Computer won:( he guessed {c_choice}")
            c_wins += 1
    print(f"Final Score:\nComputer - {c_wins}\nPlayer - {p_wins}")


play()
