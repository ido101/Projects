wrong = False
while True:
    if not wrong:
        weight = float(input("whats your weight? "))
    pork = input("(L)bs or (K)g: ").lower().strip()
    if pork == "k":
        wrong = False
        weight /= 0.45
        print(f'you are {weight} pounds')
    elif pork == "l":
        wrong = False
        weight *= 0.45
        print(f'you are {weight} kilos')
    else:
        wrong = True
        print("type l or k please")
        continue
    again = input("do you want to do it again?(y) or quit\n").lower().strip()
    if again == "y":
        pass
    else:
        quit()
