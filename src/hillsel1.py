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
    print('\nThe Plains v0.18\n')

    if var6 == 1:
        print('Nothing to see here but the remains of that reptilian you killed.\n')
        print('BACK [1]')

        while True:
            try:
                HS = int(input('\nACTION >> '))

                while HS < 1 or HS > 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hillSel1()
                    
                if HS == 1:
                    hill.hill()
            except ValueError:
                print("\nDid you mean something else?")
                time.sleep(0.5)
                hillSel1()
    else:
        hillsel1ext.hillSel1Ext()
