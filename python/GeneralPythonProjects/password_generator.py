import random
import pyperclip
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()?"
password = ""
valid = False
big_enough = False
all_char = [lower, upper, numbers, symbols]
while True:
    valid = False
    big_enough = False
    # setting the password to nothing, so we can create a new one
    password = ""
    # Length is a string because we need to check if he is actually a number first
    Length = input("What length do you want your password?\n")
    # checks if the number is an int and not a string or a float
    while not valid:
        # for loop between 0 and the length of the variable, so we can check each character of the variable individually
        for i in range(0, len(Length)):
            # we check if the current character in Length is not a number using
            # the ascii table
            if ord(Length[i]) < 48 or ord(Length[i]) > 57:
                # if the character is not a number we ask the user to enter another number
                Length = input("Please enter a valid number!\n")
                # after we do that we break and start the for loop again
                break
            # we set valid to true only in the end when we checked all the characters, and they were all numbers
            if i == len(Length)-1:
                valid = True
    # in this while loop we check if the length is big enough
    while not big_enough:
        # we check if the length is lower than 4
        if int(Length) < 4:
            # if it does we ask the user to input another password
            Length = input("Your password must be at least 4 characters!\n")
            # we set valid to false and as we did in the last section we check if the password is valid - which means
            # she has no letters in it
            valid = False
            while not valid:
                for i in range(0, len(Length)):
                    if ord(Length[i]) < 48 or ord(Length[i]) > 57:
                        Length = input("Please enter a valid number!\n")
                        break
                    if i == len(Length) - 1:
                        valid = True
        # then we set big_enough to true which means
        # we are ending the loop only if the length is bigger or equal to than 4
        # if not, we will go through all of this process again
        if int(Length) >= 4:
            big_enough = True
    # at the end we set the length to an int
    Length = int(Length)
    # then we go through 1 - to the length we picked + 1 because the last number in range is exclusive
    for i in range(1, Length + 1):
        # we pick a random number between 0-3 to tell if
        # the next character is from set lower-case, upper-case, number or a symbol
        ran_char = random.randint(0, 3)
        # we add random character from the set we picked at random to the password
        password += all_char[ran_char][random.randint(0, len(all_char[ran_char])-1)]
    print(password)
    copy = input('Do you want to copy it to clipboard?\n').strip().lower()
    if copy == "yes" or copy == "y":
        pyperclip.copy(password)
        print("Your password has been copied")

    another = input("Do you want another password?\n").strip().lower()
    if another == "no" or another == "n":
        quit("hope you enjoyed!")
    elif another == "yes" or another == "y":
        pass
    else:
        while another not in ['y', 'yes', 'n', 'no']:
            print("invalid answer")
            another = input("Do you want another password?\n").strip().lower()
        if another == "no" or another == "n":
            quit("hope you enjoyed!")
