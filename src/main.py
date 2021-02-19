import os
import time
import configparser
import mm1
import mm2
import reset

def splashScreen():
    os.system('clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    time.sleep(1.5)
    print('\nCONTINUE [1]')
    print('RESET [2]')

    bsSel1 = int(input('\nACTION >> '))
    while bsSel1 < 1 or bsSel1 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        splashScreen()

    if bsSel1 == 1: #Chapter Save Director
        print('\nScanning save...')
        config = configparser.ConfigParser()
        config.read('save/config2.ini')
        var2 = config.getint('chaptflagger', 'var2')
        time.sleep(0.5)

        if var2 == 0:
            print('Save loaded.')
            time.sleep(0.5)
            os.system('clear')
            mm1.mainMenu1()

        if var2 == 1:
            print('Save loaded.')
            time.sleep(0.5)
            os.system('clear')
            mm2.mainMenu2()

    if bsSel1 == 2:
        os.system('clear')
        print('\nDoing this will reset everything. Are you sure?')
        print('\nRESET [1]')
        print('BACK [2]')
        bsSel2 = int(input('\nACTION >> '))
        while bsSel2 < 1 or bsSel2 > 2:
            print('Did you mean something else?')
            time.sleep(0.5)
        if bsSel2 == 1:
            reset.resetter()
        if bsSel2 == 2:
            splashScreen()

splashScreen()
