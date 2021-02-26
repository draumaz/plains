import os
import time
import configparser
import mm1
import mm2
import mainalt
import mainext
import reset
import textwrap

def preSplash():
    config = configparser.ConfigParser()
    config.read('save/config11.ini')
    var11 = config.getint('splashskip', 'var11')

    if var11 == 0:
        os.system('cls||clear')
        print('')
        print(textwrap.fill("A MESSAGE FROM THE DEVELOPER:", 75))
        time.sleep(1)
        print('')
        print(textwrap.fill("Thank you for trying out The Plains! This is a major labor of love, and it happens to be my first long-form programming pursuit. The contents in this build are subject to change, as it is a beta build.", 75))
        time.sleep(10)
        print('')
        print(textwrap.fill("Regardless, I hope you enjoy the game!", 75))
        time.sleep(1)
        print('')
        print(textwrap.fill("-draumaz"))
        time.sleep(4)
        config = configparser.ConfigParser()
        config['splashskip'] = {'var11': '1'}
        with open('save/config11.ini', 'w') as configfile:
            config.write(configfile)
        os.system('cls||clear')
        time.sleep(1)
        splashScreen()
    if var11 == 1:
        splashScreen()

def splashScreen():

    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')

    config = configparser.ConfigParser()
    config.read('save/config10.ini')
    var10 = config.getint('badendext', 'var10')

    if var10 == 1:
        mainalt.mainAlt2()
    if var9 == 1:
        mainext.mainExt()

    if var9 == 0:
        os.system('cls||clear')
        print('\n==THE PLAINS==')
        print('==MADE BY DRAUMAZ IN 2021==')
        print('==WRITTEN IN PYTHON==')
        print('==CHARACTER BY BRYCE CANO==')
        time.sleep(2)
        splashScreen2()

def splashScreen2():
    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')

    if var9 == 1:
        mainext.mainExt()

    if var9 == 0:
        os.system('cls||clear')
        print('\n==THE PLAINS==')
        print('==MADE BY DRAUMAZ IN 2021==')
        print('==WRITTEN IN PYTHON==')
        print('==CHARACTER BY BRYCE CANO==')
        print('\nPLAY [1]')
        print('RESET [2]')

        config = configparser.ConfigParser()
        config.read('save/config.ini')
        var1 = config.getint('ch1endflag', 'var1')

        config = configparser.ConfigParser()
        config.read('save/config2.ini')
        var2 = config.getint('chaptflagger', 'var2')

        config = configparser.ConfigParser()
        config.read('save/config6.ini')
        var6 = config.getint('lizard', 'var6')

        while True:
            try:
                bsSel1 = int(input('\nACTION >> '))

                while bsSel1 < 1 or bsSel1 > 2:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    splashScreen2()

                if bsSel1 == 1: #Chapter Save Director (expandable)
                    print('\nScanning save...')
                    time.sleep(0.5)
                    if var2 == 0:
                        print('Save loaded.')
                        time.sleep(0.5)
                        mm1.mainMenu1()
                    if var2 == 1:
                        print('Save loaded.')
                        time.sleep(0.5)
                        mm2.mainMenu2()

                if bsSel1 == 2: #Reset
                    reset.resetter()

            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                splashScreen2()

preSplash()
