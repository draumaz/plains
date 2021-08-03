import os

def exists():
    if (os.path.exists("data.txt")):
        pass
    else:
        open("data.txt", "w+").write(20*"0\n")

def read():
    return open("data.txt", "r").readlines()

def write(line, state):
    i = read()
    i[line] = str(state) + "\n"
    open("data.txt", "w+").writelines(i)
