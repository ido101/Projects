car_has_started = False
while True:
    command = input("> ").lower().strip()
    if command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif command == "start" and not car_has_started:
        print("Car started - ready to go!")
        car_has_started = True
    elif command == "start" and car_has_started:
        print("Car has already started.")
    elif command == "stop" and car_has_started:
        print("Car stopped.")
        car_has_started = False
    elif command == "stop" and not car_has_started:
        print("Car has already stopped.")
    elif command == "quit":
        quit()
    else:
        print("unknown command")
