from time import sleep
from sys import exit
from save import save
from visuals import headers
from reader import readers
from tools import user_input, reset, clear
from intro import intro_main, intro_travel

def superblade():
    clear()
    save.exists()
    x = save.read()[0]
    headers.splash_header()
    readers.option_reader(1, 3, "PLAY", "RESET", "QUIT")
    i = user_input(1, 3, False)
    if i == 1:
        if x == 0:
            if intro_main() == True:
                intro_travel()
            else:
                superblade()
        elif x == 1:
                intro_travel()
    elif i == 2:
        reset()
        superblade()
    elif i == 3:
        headers.exit_header()
        exit()
