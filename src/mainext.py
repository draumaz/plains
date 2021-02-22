import os
import time
import mainalt
import configparser

def mainExt():
    os.system('clear')
    print('\n==AAAAAAAAAA==')
    print('==AAAAAAAA AAAAAAA AAAAAAA==')
    print('==KILLER KILLER KILLER==')
    print('==KILLER KILLER==')
    time.sleep(0.20)
    os.system('clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    time.sleep(4)
    print('\nREPENT [1]')
    print('RESET [2]')
    time.sleep(0.15)
    os.system('clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    print('\n[3]')

    extSel = int(input('\nACTION >> '))
    while extSel < 3 or extSel > 3:
        mainExt()
    if extSel == 3:
        mainalt.mainAlt()
