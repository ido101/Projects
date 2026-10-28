import random


def pick_word(topic):
    word = ""
    animals = ["dog", "cat", "fish", "bird", "hamster", "rabbit", "turtle", "snake", "lizard", "parrot", "goldfish", "mouse", "frog"]
    sports = ["basketball", "soccer", "tennis", "baseball", "football", "golf", "swimming", "volleyball", "hockey", "cricket", "table tennis", "badminton", "cycling", "running", "boxing", "wrestling", "skateboarding", "surfing", "snowboarding", "martial Arts"]
    instruments = ["guitar", "piano", "violin", "cello", "bass", "banjo", "mandolin", "ukulele", "harp", "electric guitar", "acoustic guitar"]
    fruits = ["apple", "banana", "orange", "grapes", "strawberry", "pineapple", "watermelon", "mango", "kiwi", "peach", "cherry", "blueberry", "raspberry", "avocado", "coconut", "papaya", "lemon"]
    food = ["pizza", "burger", "pasta", "salad", "sushi", "steak", "chicken", "sandwich", "tacos", "soup", "burrito", "rice", "shrimp", "lasagna", "omelette", "pancake", "cheese", "bread", "chocolate"]
    if topic == "random":
        topic = random.choice(["animals", "sports", "instruments", "fruits", "food"])
    if topic == "animals":
        word = random.choice(animals)
    elif topic == "sports":
        word = random.choice(sports)
    elif topic == "instruments":
        word = random.choice(instruments)
    elif topic == "fruits":
        word = random.choice(fruits)
    elif topic == "food":
        word = random.choice(food)
    return word, topic


def word_guessed(word, gl):
    for x in gl:
        if x in word:
            word = word.replace(x, "")
    if word.strip() == "":
        return True
    else:
        return False


def turn_gl(gl):
    r = ""
    for x in gl:
        r += " " + x.upper()
    return r


def turn_word(word, gl):
    r = ""
    for x in word:
        if x in gl:
            r += " " + x.upper()
        elif x == " ":
            r += "  "
        else:
            r += " -"
    return r


def play(ls):
    while True:
        t = input("Which topic would you like: animals, sports, instruments, fruits, food or a random topic(type random)?\n").lower().strip()
        while t not in ["animals", "sports", "instruments", "fruits", "food", "random"]:
            t = input("Please pick a valid topic! ")
        w, t = pick_word(t)
        guessed_letters = []
        lives = ls
        print(f"You have {lives} lives. The topic is {t}. Go!")
        while not word_guessed(w, guessed_letters):
            guess = input("Guess a letter: ").lower().strip()
            while len(guess) > 1 or guess.isdigit() or guess.strip() == "":
                guess = input("Please enter a valid letter: ").lower().strip()
            guessed_letters += guess
            if guess in w:
                print(f"Your letter, {guess}, was in the word\nYou have {lives} lives and you used these letters:{turn_gl(guessed_letters)}\nCurrent word: {turn_word(w, guessed_letters)}")
            else:
                lives -= 1
                print(f"Your letter, {guess}, wasn't in the word\nYou have {lives} lives and you used these letters:{turn_gl(guessed_letters)}\nCurrent word: {turn_word(w, guessed_letters)}")
            if lives == 0:
                print(f"You ran out of lives! The word was {w}. Better luck next time.")
                kp = input("Do you want to keep playing?(y or n)").lower().strip()
                if kp == "n":
                    quit("Bye")
                break
        else:
            print(f"You guessed the word!!")
            k = input("Do you want to keep playing?(y or n)").lower().strip()
            if k == "n":
                quit("Bye")

lives = int(input("Welcome to Hangman! How many lives would you like to have? (1-10) "))
while lives < 1 or lives > 10:
    lives = int(input("Please enter a valid number of lives (1-10): "))
play(lives)
