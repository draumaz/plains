import tools
import visuals

def intro_pause(i): # soon to be deprecated
    if i == 0:
        return [0.03, 0.15]
    if i == 1:
        return [0.75, 0.02]
    if i == 2:
        return [1.50, 0.0015]
    if i == 3:
        return [0.75, 0.0020]
    if i == 4:
        return [0.70, 0.0075]
    if i == 5:
        return [0.70, 0.0040]
    if i == 6:
        return [0.50, 0.0040]
    if i == 7 or i == 8:
        return [1, 0.0035]
    if i == 9:
        return [1, 0.006]
    if i == 10:
        return [1, 0.002]
    if i == 11:
        return [0, 0.0035]
    if i == 12:
        return [1, 0.0045]
    if i == 13:
        return [0, 0.0008]

def intro_strings(i):
    if i == 0:
        s = ["Esakul Base 6", 0.006, 1]
    elif i == 1:
        s = ["LIAM", 0.015, 1]
    elif i == 2:
        s = ["hey man,", 0.035, 0.45]
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
    return list(s)

def intro_words(i): # soon to be deprecated
    if i == 0:
        i = "hey man,"
    elif i == 1:
        i = " what's up?"
    elif i == 2:
        i = "..."
    elif i == 3:
        i = "classic."
    elif i == 4:
        i = "anyways,"
    elif i == 5:
        i = " i'm currently stuck on a deserted planet..."
    elif i == 6:
        i = "mind swingin' by and grabbin' me?"
    elif i == 7:
        i = "thanks man!!"
    elif i == 8:
        i = "lol ok see you soon man"
    elif i == 9:
        i = "Esakul"
    elif i == 10:
        i = "513:486 JKZ"
    elif i == 11:
        i = "LIAM"
    elif i == 12:
        i = "Seems like you've found yourself in the same position as LIAM."
    return list(i)

def intro_main():
    tools.clear()
    visuals.header()
    print("")
    tools.snooze(1)
    for i in range (0, 9):
        x = None
        if i == 0:
            x = "Establishing connection to: "
        elif i == 1:
            x = "\n\nIncoming chat from:         "
        elif i == 2 or i == 6 or i == 8:
            x = "\n\nLIAM: "
        if x is not None:
            print(x, end="", flush=True)
        tools.snooze(0.8)
        if i == 4:
            print("\n")
            tools.user_input(0,0,True)
            print("\nLIAM: ", end="", flush=True)
        tools.array_reader(intro_strings(i)[0], intro_strings(i)[1])
        tools.snooze(intro_strings(i)[2])