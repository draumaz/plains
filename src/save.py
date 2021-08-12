from os import path, remove

def config(path):
    if path == 0:
        return str("data.txt") # File name
    elif path == 1:
        return str(0) # Fill type
    elif path == 2:
        return int(20) # Zero count
    return 1

class save():
    def read():
        return list(map(int, open(config(0), "r").readlines()))
    def write(line, state):
        i = save.read()
        f = open(config(0), "w")
        for r in range (0,config(2)):
            if r == line:
                f.write(str(state)+"\n")
                continue
            f.write(str(i[r])+"\n")
    def exists():
        if (path.exists(config(0))):
            pass
        else:
            open(config(0), "w+").write(config(2)*(config(1)+"\n"))
    def destroy():
        if (path.exists(config(0))):
            remove(config(0))
            return 0
        else:
            return 1
