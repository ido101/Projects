import turtle
from turtle import *
wn = Screen()
moveSpeed = 30
posit = [0, 0]


def go_fd():
    setheading(90)
    fd(moveSpeed)


def go_bk():
    setheading(270)
    fd(moveSpeed)


def go_rt():
    setheading(360)
    fd(moveSpeed)


def go_lt():
    setheading(180)
    fd(moveSpeed)


def cls():
    clearscreen()
    showturtle()
    shape(shape_inp)
    color(turtle_color)
    speed(3)
    pensize(5)
    if shape_inp == "classic" or shape_inp == "turtle":
        shapesize(1.5)
    else:
        shapesize(0.75)
    onkey(go_fd, "w")
    onkey(go_fd, "Up")
    onkey(go_lt, "a")
    onkey(go_lt, "Left")
    onkey(go_rt, "d")
    onkey(go_rt, "Right")
    onkey(go_bk, "s")
    onkey(go_bk, "Down")
    onkey(cls, "c")
    listen()


shape_inp = input("What shape do you want the player to be?(square, circle, arrow, turtle, triangle or classic)\n").lower().strip()
while shape_inp not in ['square', 'circle', 'arrow', 'turtle', 'triangle', 'classic']:
    shape_inp = input("You must pick one of the options!\n").lower().strip()
turtle_color = input("What color do you want your turtle?(red, yellow, blue, green, black, pink, purple or gray)\n")
while turtle_color not in ['red', 'yellow', 'blue', 'green', 'pink', 'black', 'purple', 'gray']:
    turtle_color = input("You must pick one of the options!\n").lower().strip()
if shape_inp == "classic" or shape_inp == "turtle":
    shapesize(1.5)
else:
    shapesize(0.75)
print("Have fun!\nDon't forget to press 'c' to clear the screen")
cls()
done()
