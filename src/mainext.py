import os
import time
import mainalt
import configparser

def mainExt():
    os.system('cls')
    print('\n==AAAAAAAAAA==')
    print('==AAAAAAAA AAAAAAA AAAAAAA==')
    print('==KILLER KILLER KILLER==')
    print('==KILLER KILLER==')
    time.sleep(0.20)
    os.system('cls')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    time.sleep(4)
    print('\n[3]')
    extSel = int(input('\nACTION >> '))
    while extSel < 3 or extSel > 3:
        mainExt3()
    if extSel == 3:
        mainalt.mainAlt()

def mainExt3():
    os.system('cls')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    print('\n[3]')
    extSel = int(input('\nACTION >> '))
    while extSel < 3 or extSel > 3:
        mainExt3()
    if extSel == 3:
        mainalt.mainAlt()
