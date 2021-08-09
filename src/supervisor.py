from time import sleep
from sys import exit
from save import exists
from visuals import splash_header, exit_header
from tools import option_reader, user_input, reset, clear
from intro import intro_main

def superblade():
    clear()
    exists()
    splash_header()
    option_reader(1, 3, "PLAY", "RESET", "QUIT")
    i = user_input(1, 3, False)
    if i == 1:
        intro_main()
    elif i == 2:
        if reset() == 0:
            superblade()
        else:
            sleep(1)
            exit()
    elif i == 3:
        exit_header()
        exit()
