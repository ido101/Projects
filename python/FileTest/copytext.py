import pyperclip


def find(letter, st):
    i = 0
    index = -1
    for char in st:
        if char == letter:
            index = i
            break
        i += 1
    return index


# pyperclip.copy("""this line is 1
# this line is 2
# this line is 3
# this line is 4
# this line is 5""")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s.Your current balance is $%s."
print(format_string % data)
string = "python hi"
print(find("t", string))

