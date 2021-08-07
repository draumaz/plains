import os
import save
import time

def version():
    return "v0.26"

def clear():
    if os_check() == 1:
        os.system("cls")
    else:
        os.system("clear")

def os_check():
    i = 0
    if os.name == "nt":
        i = 1
    return i

def snooze(ms):
    time.sleep(ms)

def array_reader(string, ms):
    for i in string:
        print(i, end="", flush=True)
        snooze(ms)
    return ""

def option_reader(*args):
    for i in range(2, len(args)):
        print(args[i] + " [" + str(i-1) + "]")
    print()

def user_input(min, max, strout):
    while True:
        try:
            if strout == True:
                return input(array_reader("YOU: ", 0.005))
            raw_input = input(array_reader("ACTION >> ", 0.005))
            oops = "\nDid you mean something else?\n"
            if int(raw_input) < min or int(raw_input) > max:
                if int(raw_input) == 69 or int(raw_input) == 420:
                    print("\nNice.")
                else:
                    print(oops)
                snooze(0.2)
                continue
            else:
                break
        except ValueError:
            print(oops)
            snooze(0.2)
            continue
    return int(raw_input)

def reset():
    print("\nYou sure you wanna reset?\n")
    option_reader(1, 2, "YES", "NO")
    if user_input(1, 2, False) == 1:
        if save.destroy() == 0:
            save.exists()
            print("\nSave reset.")
        else:
            print("\nDelete failed.")
        snooze(0.25)
    return 0