from tools import clear, array_reader, option_reader, user_input
from visuals import headers
from save import save
from time import sleep

def intro_strings(i):
    if i == 0:
        s = ["Esakul", 0.05, 2]
    elif i == 1:
        s = ["ELI", 0.025, 1]
    elif i == 2:
        s = ["hey man,", 0.035, 0]
    elif i == 3:
        s = [" whats up?", 0.045, 0.005]
    elif i == 4:
        s = ["..." , 0.04, 1]
    elif i == 5:
        s = ["classic.", 0.05, 1]
    elif i == 6:
        s = ["anyways, ", 0.075, 0.75]
    elif i == 7:
        s = ["i'm currently stuck at this old base...", 0.008, 1]
    elif i == 8:
        s = ["mind swingin' by and pickin' me up?", 0.01, 1]
    elif i == 9:
        s = ["thanks man!!", 0.008, 1]
    elif i == 10:
        s = ["lol see you soon man", 0.008, 1]
    elif i == 11:
        s = ["513:486 JKZ", 0.35, 1]
    return list(s)

def intro_main():
    eli_prompt = "\n" + intro_strings(1)[0] + ": "
    clear()
    headers.version_header()
    print("")
    sleep(1)
    for i in range (0, 9):
        x = None
        if i == 0:
            x = "Establishing connection to: "
        elif i == 1:
            x = "\n\nIncoming chat from:         "
        elif i == 2 or i == 6 or i == 8:
            x = "\n" + eli_prompt
        if x is not None:
            print(x, end="", flush=True)
        sleep(0.8)
        if i == 4:
            print("\n")
            user_input(0,0,True)
            print(eli_prompt, end="", flush=True)
        array_reader(intro_strings(i)[0], intro_strings(i)[1])
        sleep(intro_strings(i)[2])
        if i == 8:
            print("\n")
            option_reader(1, 2, "I'LL GET YA", "NO WAY")
            if user_input(1, 2, False) == 1:
                print(eli_prompt, end="", flush=True)
                array_reader(intro_strings(9)[0], intro_strings(9)[1])
                sleep(intro_strings(9)[2])
            else:
                print(eli_prompt, end="", flush=True)
                array_reader(intro_strings(10)[0], intro_strings(10)[1])
                sleep(intro_strings(10)[2])
            save.write(0, 1)
            return True

def intro_travel():
    pass