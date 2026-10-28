print("welcome to my computer quiz!")
score = 0
playing = input("do you want to play? ")
if playing.lower() != "yes":
    exit()
print("Ok lets play")
answer = input("what does cpu stand for? \n")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect:(")


answer = input("what does gpu stand for? \n")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect:(")


answer = input("what does RAM stand for? \n")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect:(")


answer = input("what does PSU stand for? \n")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect:(")
print("your final score is:" + str(score))
print("you got "+ str(int(score / 4 * 100))+"%")