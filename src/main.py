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

    config = configparser.ConfigParser()
    config.read('save/config2.ini')
    var2 = config.getint('chaptflagger', 'var2')
    
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')

    time.sleep(1.5)

    if var1 == 1:
        print('\nCONTINUE [1]')
    if var1 == 0:
        print('\nNEW GAME [1]')
    if var2 == 1:
        if var1 == 0:
            print('\nNEW GAME [1]')
    if var1 == 1:
        print('RESET [2]')

    bsSel1 = int(input('\nACTION >> '))

    while bsSel1 < 1 or bsSel1 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        splashScreen()

    if bsSel1 == 1: #Chapter Save Director (expandable)
        if var1 == 1:
            print('\nScanning save...')
        if var1 == 0:
            print('\nInitializing save...')
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

    if bsSel1 == 2: #Resetter
        if var2 == 1:
            if var1 == 1:
                reset.resetter()
            if var1 == 0:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                splashScreen()
        if var2 == 0:
            if var1 == 1:
                reset.resetter()
            if var1 == 0:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                splashScreen()

splashScreen()
