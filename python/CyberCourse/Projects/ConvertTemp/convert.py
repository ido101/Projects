def CtoF(deg):
    return deg * (9 / 5) + 32
def FtoC(deg):
    return (deg - 32) * (5 / 9)

while True:
    conv = int(input("Which would you like to perform? \n1: Celsius to Fahrenheit\n2: Fahrenheit to Celsius\n3: Exit\n> "))
    if conv == 1:
        print(f"{CtoF(int(input('Enter the temperature in Celsius: ')))}°F")
    elif conv == 2:
        print(f"{FtoC(int(input('Enter the temperature in Fahrenheit: ')))}°C")
    elif conv == 3:
        break