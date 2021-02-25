import os
import time
import mainalt
import configparser

def mainExt():
    os.system('cls||clear')
    print('\n==AAAAAAAAAA==')
    print('==AAAAAAAA AAAAAAA AAAAAAA==')
    print('==KILLER KILLER KILLER==')
    print('==KILLER KILLER==')
    time.sleep(0.05)
    mainExt2()

def mainExt2():
    os.system('cls||clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    time.sleep(5)
    mainExt3()

def mainExt3():
    os.system('cls||clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    print('\n[3]')
    while True:
        try:
            extSel = int(input('\nACTION >> '))
            while extSel < 3 or extSel > 3:
                mainExt3()
            if extSel == 3:
                mainalt.mainAlt()
        except ValueError:
            mainExt3()
        except KeyboardInterrupt: #;)
            mainExt3()
