from os import system, name
from save import save
from time import sleep
from reader import readers

def version():
    return "v0.26"

def clear():
    if os_check() == 1:
        system("cls")
    else:
        system("clear")

def os_check():
    i = 0
    if name == "nt":
        i = 1
    return i

def user_input(min, max, strout):
    oops = "\nDid you mean something else?\n"
    while True:
        try:
            if strout == True:
                return input(readers.array_reader("YOU: ", 0.005))
            raw_input = input(readers.array_reader("ACTION >> ", 0.005))
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
    i = user_input(1, 2, False)
    if i == 1:
        if save.destroy() == 0:
            save.exists()
            print("\nSave reset.")
        else:
            print("\nDelete failed.\n")
            return 1
    sleep(0.25)
    return 0
