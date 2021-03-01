import os
import time
import tool
import configparser
import cave

def cs1Knife():
    print('\nYou decide to pick up the knife. Might come in handy later.')
    time.sleep(3)
    config = configparser.ConfigParser()
    config['blade'] = {'var15': '1'}
    with open('save/config15.ini', 'w') as configfile:
        config.write(configfile)
    caveSel1()

def caveSel1():
    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print("You continue deeper down the cave. Looks like there's a knife laying in here.\n")
    print('PICK UP [1]')
    print('BACK [2]')

    while True:
        try:
            caveSelect1 = int(input('\nACTION >> '))

            if caveSelect1 == 1:
                cs1Knife()

            if caveSelect1 == 2:
                print("\nContinuing in a cave this dark is just asking for trouble.")
                time.sleep(3)
                cave.cave()
                
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            caveSel1()
