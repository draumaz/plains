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
    headers.splash_header()
    opt = [1, 3]
    readers.option_reader(opt[0], opt[1], "PLAY", "RESET", "QUIT")
    i = user_input(opt[0], opt[1], False)
    if i == 1:
        x = save.read()[0]
        if x == 0:
            if intro_main() == True:
                intro_travel()
            else:
                superblade()
        elif x == 1:
                intro_travel()
        elif x == 2:
            if reset() == 0:
                superblade()
            else:
                sleep(1)
                exit()
        elif x == 3:
            headers.exit_header()
            exit()
