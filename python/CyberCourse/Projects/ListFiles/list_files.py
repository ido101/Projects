import os

def print_dir_files(path):
    items = os.listdir(path)
    for item in items:
        item_path = path+"/"+item
        if(os.path.isdir(item_path)):
            print_dir_files(item_path)
        else:
            print("this is a file: " +  item_path)


print_dir_files("C:/Users/IDO123/Desktop/English project evacuees")