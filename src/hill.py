import os
import time
import mm1
import textwrap
import hillsel1
import hillsel2
import hillsel3
import configparser

def hill():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')
    config = configparser.ConfigParser()
    config.read('save/config12.ini')
    var12 = config.getint('lizarddx', 'var12')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    if var6 == 0 and var1 == 0:
        print(textwrap.fill('That hill looks pretty strange. It juts out of the landscape in an unrealistic way.', 75))
    if var6 == 0 and var1 == 1:
        print(textwrap.fill("Having stood there, you hear a strange noise in the sky. Perhaps heading back to where you started will reveal the source.", 75))
    if var6 == 1 and var1 == 0:
        print('You should stand still.')
    if var6 == 1 and var1 == 1:
        print("They're coming. Go back.")
    if var6 == 0 and var12 == 0:
        print('In the distance, you can see a creature moving about.\n')
        print('GO TOWARDS THE CREATURE [1]')
    if var12 == 1:
        print('')
    if var6 == 1:
        print('')
        print('GO FORWARDS [1]')
    if var1 == 0:
        print('STAND STILL [2]')
    print('TAKE A BREAK [3]')
    print('BACK [4]')

    while True:
        try:
            hillSelect = int(input('\nACTION >> '))

            if hillSelect == 1:
                if var12 == 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hill()
                if var12 == 0:
                    hillsel1.hillSel1()
            if hillSelect == 2:
                if var1 == 0:
                    hillsel2.hillSel2()
                if var1 == 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hill()
            if hillSelect == 3:
                hillsel3.hillSel3()
            if hillSelect == 4:
                if var6 == 0:
                    print('\nBest to head back.')
                    time.sleep(2)
                    mm1.mainMenu1()
                if var6 == 1:
                    mm1.mainMenu1()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hill()
