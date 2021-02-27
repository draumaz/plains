import os
import time
import hill
import lizardman
import mm1
import configparser

def hillSel1Ext():
    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print('The huge reptilian sees you, and approaches.')
    if var7 == 0:
        print('')
    if var7 == 1:
        time.sleep(2)
        print("Looks like he's having a sense of déjà vu.\n")
        time.sleep(3)
    print('KILL [1]')
    print('TALK [2]')
    print('BACK [3]')

    while True:
        try:
            hillSel1ExtSel = int(input('\nACTION >> '))

            while hillSel1ExtSel < 1 or hillSel1ExtSel > 3:
                print('Did you mean something else?')
                time.sleep(0.5)
                hillSel1Ext()

            if hillSel1ExtSel == 1:
                print('\nYou run up to the lizard and stab him to death.')
                time.sleep(3)
                print('Blood stains your uniform.')
                time.sleep(6)
                lizardman.lizardMan()

            if hillSel1ExtSel == 2:
                if var7 == 1:
                    config = configparser.ConfigParser()
                    config['lizarddx'] = {'var12': '1'}
                    with open('save/config12.ini', 'w') as configfile:
                        config.write(configfile)
                    print('\nThe reptilian man seems untrusting of you, and leaves the area pretty quickly.')
                    time.sleep(5)
                    hill.hill()
                if var7 == 0:
                    print('\nThe reptilian comes to you, and gives you some information.')
                    time.sleep(2)
                    print("You're far from home, aren'tcha?")
                    time.sleep(2)
                    print("...not really helpful. But he means well.")
                    time.sleep(3)
                    hill.hill()

            if hillSel1ExtSel == 3:
                print('\nUpon seeing the towering lizard, you decide to head back.')
                time.sleep(2)
                mm1.mainMenu1()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hillSel1Ext()
