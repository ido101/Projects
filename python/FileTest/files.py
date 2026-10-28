import os
start_dir = os.getcwd()
os.chdir("../1st")
os.rename("new file", "new file")
os.chdir(start_dir)

with open("testfile", "r+") as f:
    # prints all the text in the file
    print(f.read())
    # returns the cursor to the start of the file, so you can read it again
    f.seek(0)
    # makes a variable with all the file's lines in it
    lines = f.readlines()
    # prints each line individually
    print(lines[0], end='')
    print(lines[1], end='')
    print(lines[2], end='')
    print(lines[3], end='')
    print(lines[4], end='\n\n')

    for line in lines[2:5]:
        print(line, end='')
    f.seek(0)
    # deletes everything in the file
    f.truncate()
    # if you want, you can enter a number in the parenthesis
    # and this is how many characters you want to keep in the text file




