import os
import time
import talk
import saan
import embark
import configparser
import inventory

def mainMenu2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    os.system('clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print('A fancy, metallic ship lands a little ways from where you landed.')
    if var6 == 0:
        print('Your friends walk out, and approach you.\n')
    if var6 == 1:
        print('Your friends seem like they want to keep their distance.\n')
    print('TALK [1]')
    print('SAAN [2]')
    print('EMBARK [3]')
    print('QUIT [4]')

    while True:
        try:
            mainmenuSelect2 = int(input('\nACTION >> '))

            if mainmenuSelect2 == 1:
                talk.talk()
            if mainmenuSelect2 == 2:
                saan.saan()
            if mainmenuSelect2 == 3:
                embark.Embark()
            if mainmenuSelect2 == 4:
                os.system('cls||clear')
                print('\nThanks for playing!')
                time.sleep(0.5)
                quit()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu2()
