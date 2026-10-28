import math
import os
import time
num = 145
# print even if num is even and odd if it's odd
print("even" if num % 2 == 0 else "odd")
# makes a tab space
print("\tTab")
# if we put r before the text \n and \t will not work
print(r'\t this is text \n next line')
# the sleep method makes python wait as many seconds as you put in the brackets
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
# the os.system("cls") command clears the screen
# in windows but in mac/linux instead of cls use clear
os.system("cls")
course = "pyThon For BeginNers"
print(course)
# returns the length of the string(but it starts from 1 and not 0)
print(len(course))
# makes the first letter upper-case and the rest lower-case
print(course.capitalize())
# makes all the letters upper-case
print(course.upper())
# makes all the letters lower-case
print(course.lower())
# the find method finds the index of the character or a sequence of characters
# if the character isn't in the string it returns -1
print(course.find("o"))
# replaces a character or a sequence of characters
# if there is more than one character you're replacing ,and
# you type a number after that like 1 it will
# only replace one character like it
print(course.replace("o", "y", 1))
# checks if there is a sequence of characters in the string and returns true or false
print("Python" in course)
print("pyThon" in course)
# returns the string but with every word the first letter
# is capitalized and all the others are low-cased
print(course.title())
string = ""
# removes all the spaces in a string with one word
print(string.strip())
world = "weld"
print(f"hello {world}")
x = 2.45
# the round function rounds a number
print(round(x))
neg = -5
# the abs function return the absolute value(positive value)
print(abs(neg))
# rounds the number to the top
print(math.ceil(2.1))
# rounds the number to the bottom
print(math.floor(2.9))
# returns the square root of the number
print(math.sqrt(9))



