import os
import time

def version():
    return "0.01"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def snooze(ms):
    time.sleep(ms)

def array_reader(string, ms):
    for i in string:
        print(i, end='', flush=True)
        snooze(ms)
    return ""

def user_input(min, max):
    while True:
        try:
            raw_input = input(array_reader("ACTION >> ", 0.005))
            oops = "\nDid you mean something else?\n"
            if int(raw_input) < min or int(raw_input) > max:
                if int(raw_input) == 69 or int(raw_input) == 420:
                    print("\nNice.")
                    snooze(0.2)
                    continue
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