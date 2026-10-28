while True:
    print("Measurement Unit Converter")
    ans = input("Which measurement topic do you want to convert?\n-height\n-mass\n-time\n").lower()
    while ans not in ["height", "mass", "time"]:
        ans = input("Please pick a valid topic: ").lower()
    if ans == "height":
        af, uf = input("Choose unit and amount you want to convert from('amount' 'unit'), these are your options:\n1.millimeter\n2.centimeter\n3.meter\n4.kilometer\n").split(" ")
        ut = input("Choose unit you want to convert to('unit'):")
        rut = ut
        mil = 1
        cent = 10
        meter = 1000
        kilo = 1000000
        if uf == "millimeter" or uf == "millimeter":
            uf = mil
        elif uf == "centimeter" or uf == "centimeters":
            uf = cent
        elif uf == "meter" or uf == "meters":
            uf = meter
        else:
            uf = kilo
        if ut == "millimeter" or ut == "millimeters":
            ut = mil
        elif ut == "centimeter" or ut == "centimeters":
            ut = cent
        elif ut == "meter" or ut == "meters":
            ut = meter
        else:
            ut = kilo
        af = int(af)
        total = af * (uf/ut)
        print(str(total) + " " + rut)
    elif ans == "mass":
        af, uf = input("Choose unit and amount you want to convert from('amount' 'unit'), these are your options:\n1.gram\n2.kilogram\n3.ton\n").split(" ")
        ut = input("Choose unit you want to convert to('unit'):")
        rut = ut
        gram = 1
        kg = 1000
        ton = 1000000
        if uf == "gram" or uf == "grams":
            uf = gram
        elif uf == "kilogram" or uf == "kilograms":
            uf = kg
        elif uf == "ton" or uf == "tons":
            uf = ton
        if ut == "gram" or ut == "grams":
            ut = gram
        elif ut == "kilogram" or ut == "kilograms":
            ut = kg
        elif ut == "ton" or ut == "tons":
            ut = ton
        af = int(af)
        total = af * (uf / ut)
        print(str(total) + " " + rut)
    elif ans == "time":
        af, uf = input("Choose unit and amount you want to convert from('amount' 'unit'), these are your options:\n1.second\n2.minute\n3.hour\n4.day\n5.year\n").split(" ")
        ut = input("Choose unit you want to convert to('unit'):")
        rut = ut
        sec = 1
        minute = 60
        hour = 3600
        day = 3600 * 24
        year = 3600 * 24 * 365
        if uf == "second" or uf == "seconds":
            uf = sec
        elif uf == "minute" or uf == "minutes":
            uf = minute
        elif uf == "hour" or uf == "hours":
            uf = hour
        elif uf == "day" or uf == "days":
            uf = day
        else:
            uf = year
        if ut == "second" or ut == "seconds":
            ut = sec
        elif ut == "minute" or ut == "minutes":
            ut = minute
        elif ut == "hour" or ut == "hours":
            ut = hour
        elif ut == "day" or ut == "days":
            ut = day
        else:
            ut = year
        af = int(af)
        total = af * (uf / ut)
        print(str(total) + " " + rut)
    ag = input("Do you wanna try again?(y or n)").lower()
    if ag == "n":
        quit("Bye")
