import os

def PrintDirFiles(path, num=0): 
    if not os.path.isdir(path):
        print("this is a file: " + path)
        return
    items = os.listdir(path)
    for item in items:
        space = "   " * num
        print(space + item)
        item_path = path+"/"+item
        if(os.path.isdir(item_path)):
            PrintDirFiles(item_path, num + 1)

PrintDirFiles("C:/Users/IDO123/Desktop/English project evacuees")