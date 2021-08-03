import os

def config(i):
    if i == 0:
        return "data.txt"

def exists():
    if (os.path.exists(config(0))):
        pass
    else:
        open(config(0), "w+").write(20*"0\n")

def destroy():
    if (os.path.exists(config(0))):
        os.remove(config(0))
        return 0
    else:
        return 1

def read():
    return open(config(0), "r").readlines()

def write(line, state):
    i = read()
    i[line] = str(state) + "\n"
    open(config(0), "w+").writelines(i)
