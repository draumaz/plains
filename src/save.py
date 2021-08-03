import os

def config(path):
    if path == 0:
        return "data.txt"
    elif path == 1:
        return 20

def exists():
    if (os.path.exists(config(0))):
        pass
    else:
        open(config(0), "w+").write(config(1)*"0\n")

def read():
    return list(map(int, open(config(0), "r").readlines()))
    
def write(line, state):
    i = read()
    i[line] = str(state) + "\n"
    open(config(0), "w+").writelines(i)

def destroy():
    if (os.path.exists(config(0))):
        os.remove(config(0))
        return 0
    else:
        return 1


