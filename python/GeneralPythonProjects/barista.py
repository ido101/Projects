print("Hello, welcome to NetworkChuck Coffee!")
name = input("What is your name?\n").lower().strip()
if name == "ben":
    is_evil = input("Are you evil?\n").lower().strip()
    if is_evil == "yes":
        print("We don't want you Ben, get out!!!")
        quit()
    else:
        print("Your one of the good Bens, thank you so much for coming in today.\n")
else:
    print("Hello " + name.capitalize() + ", thank you so much for coming in today.\n")
Menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"
order = input(name.capitalize() + ", This is what we are serving:\n" + Menu + "\nWhat would you like?\n").lower()
if order == "frappuccino":
    price = 13
elif order == "black coffee":
    price = 3
elif order == "latte":
    price = 9
elif order == "espresso":
    price = 4
elif order == "cappuccino":
    price = 10
else:
    print("Sorry, we don't have that here.")
quantity = input("How many coffees would you like?\n")
total = price * int(quantity)
print(f"Your total would be ${total}")
print(f"Sound good {name.capitalize()}, your {quantity} {order.capitalize()}s will be ready in a moment")

1555
9