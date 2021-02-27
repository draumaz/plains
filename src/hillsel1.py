import os
import time
import hill
import mm1
import hillsel1ext
import configparser

def hillSel1():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config5.ini')
    var5 = config.getint('reset', 'var5')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')

    if var6 == 1:
        print('Silence fills the air.\n')
        print('BACK [1]')

        while True:
            try:
                HS = int(input('\nACTION >> '))

                if HS == 1:
                    hill.hill()
                    
            except ValueError:
                print("\nDid you mean something else?")
                time.sleep(0.5)
                hillSel1()
    else:
        hillsel1ext.hillSel1Ext()
