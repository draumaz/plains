import os
import time
import configparser
import mm1
import mm2
import mainalt
import reset

def splashScreen():

    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')

    if var9 == 0:
        os.system('clear')
        print('\n==THE PLAINS==')
        print('==MADE BY DRAUMAZ IN 2021==')
        print('==WRITTEN IN PYTHON==')
        print('==CHARACTER BY BRYCE CANO==')
        time.sleep(1.5)
        print('\nPLAY [1]')
        print('RESET [2]')
    if var9 == 1:
        os.system('clear')
        print('\n==AAAAAAAAAA==')
        print('==AAAAAAAA AAAAAAA AAAAAAA==')
        print('==KILLER KILLER KILLER==')
        print('==KILLER KILLER==')
        time.sleep(0.5)
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
        print('\nP̴̵̷͓̪̟͓͔̰̟̺͇̲̜͇̘L̜̰̼̮̺̤̞͚̜̭̙͓̙͠A̫̞̦̭̲͓͚̻̣͇͈̣̤̜̹̕͘ͅY̶̶͍͓̹͖̟̭͉͘͢͡ [1]')
        print('R̷̸̫̰͓̳E̺̰͚̥͇̲͙̦̲̥̟̻Ş̛͎̗̖̩̹͎̱̰̼́͞E̡͟͏̧͍͓̻̪̤̝̖̪͉T̸̡͇͚̦͓̣͎̜͘͟͠ [2]')
        print('\n\n\n')
        print('REPENT [3]')

    bsSel1 = int(input('\nACTION >> '))

    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')

    config = configparser.ConfigParser()
    config.read('save/config2.ini')
    var2 = config.getint('chaptflagger', 'var2')

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    while bsSel1 < 1 or bsSel1 > 3:
        print('Did you mean something else?')
        time.sleep(0.5)
        splashScreen()

    if bsSel1 == 1: #Chapter Save Director (expandable)
        if var9 == 1:
            splashScreen()
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
        if var9 == 1:
            splashScreen()
        reset.resetter()
    if bsSel1 == 3:
        if var9 == 0:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            splashScreen()
        if var9 == 1:
            mainalt.mainAlt()

splashScreen()