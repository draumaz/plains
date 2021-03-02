import os
import time
import tool
import configparser
import cave

def cs1Knife():
    print('\nYou open the box and find a knife. You put it in your pocket.')
    config = configparser.ConfigParser()
    config['blade'] = {'var15': '1'}
    with open('save/config15.ini', 'w') as configfile:
        config.write(configfile)
    time.sleep(3)
    caveSel1()

def caveSel1():
    config = configparser.ConfigParser()
    config.read('save/config15.ini')
    var15 = config.getint('blade', 'var15')
    os.system('cls||clear')
    print('\nThe Plains v0.20\n')
    if var15 == 0:
        print("You continue deeper down the cave. There's a small box sitting near the wall.\n")
        print('OPEN [1]')
    if var15 == 1:
        print("Just a dingy old cave.\n")
    print('BACK [2]')

    while True:
        try:
            caveSelect1 = int(input('\nACTION >> '))

            if caveSelect1 == 1:
                if var15 == 0:
                    cs1Knife()
                if var15 == 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    caveSel1()

            if caveSelect1 == 2:
                if var15 == 0:
                    print("\nContinuing in a cave this dark is just asking for trouble.")
                    time.sleep(3)
                cave.cave()
                
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            caveSel1()