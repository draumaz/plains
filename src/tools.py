from os import system, name
from save import save
from time import sleep
from reader import readers

def version():
    return "v0.26"

def clear():
    if is_win() == True:
        system("cls")
    else:
        system("clear")

def is_win():
    if name == "nt":
        return True
    else:
        return False

def user_input(min, max, strout):
    oops = "\nDid you mean something else?\n"
    while True:
        try:
            if strout == True:
                return input(readers.array_reader("YOU: ", 0.015))
            raw_input = input(readers.array_reader("ACTION >> ", 0.015))
            if int(raw_input) < min or int(raw_input) > max:
                if int(raw_input) == 69 or int(raw_input) == 420:
                    print("\nNice.")
                else:
                    print(oops)
                sleep(0.2)
                continue
            else:
                break
        except ValueError:
            print(oops)
            sleep(0.2)
            continue
    return int(raw_input)

def reset():
    print("\nYou sure you wanna reset?\n")
    readers.option_reader(1, 2, "YES", "NO")
    match user_input(1, 2, False):
        case 1:
            if save.destroy() == 0:
                print("\nSave reset.")
                v = 0
            else:
                print("\nFailed to delete save.")
                v = 1
        case 2:
            return
    sleep(0.25)    
    return v