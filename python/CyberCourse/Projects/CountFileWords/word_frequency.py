import sys
import os

def read_file_content(file_path):
    with open(file_path, "r") as f:
        d = {}
        for line in f:
            words = line.split()
            for word in words:
                if word.strip(".,") in d:
                    d[word.strip(".,")] += 1
                else:
                    d[word.strip(".,")] = 1
        return d

def sort_words(d, n):
    l = sorted(d.items(), key=lambda items:items[1], reverse=True)
    l = l[:n]
    l = dict(l)
    return l



if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        raise Exception("please enter N as sys argument")
    file_path = "textFile.txt"
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    d = read_file_content(file_path)
    d = sort_words(d, n)
    for key, value in d.items():
        print("Word: " + key + " appears " + str(value) + " times.")