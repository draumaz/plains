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
    match user_input(opt[0], opt[1], False):
        case 1:
            match save.read()[0]:
                case 0:
                    if intro_main() == True:
                        intro_travel()
                    else:
                        superblade()
                case 1:
                    intro_travel()
        case 2:
            if reset() == 0:
                superblade()
            else:
                sleep(1)
                exit()
        case 3:
            headers.exit_header()
            exit()
