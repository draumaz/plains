import os
import time
import hill
import configparser

def standFlagger():
        config = configparser.ConfigParser()
        config['ch1endflag'] = {'var1': '1'}
        with open('save/config.ini', 'w') as configfile:
               config.write(configfile)
        hill.hill()

def hs2Sub2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    if var6 == 0:
        print("\nStanding there motionless, it gives you the feeling that everything's going to be alright.\n")
    if var6 == 1:
        print("\nThey're coming.")
    time.sleep(5)
    standFlagger()

def hs2Sub():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print("\nThey're coming.")
    time.sleep(5)
    standFlagger()

def hillSel2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('cls||clear')
    print('\nThe Plains v0.20\n')
    print('Despite the massive mountain ahead of you, you decide to simply stand still.')
    if var6 == 1:
        hs2Sub()
    if var6 == 0:
        time.sleep(2)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('Seems like a bit of a waste of time.')
        time.sleep(2)
        print('\nKEEP STANDING [1]')
        print('GO BACK [2]')

        while True:
            try:
                hillSel2Select = int(input('\nACTION >> '))
                if hillSel2Select == 1:
                    hs2Sub2()
                if hillSel2Select == 2:
                    print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
                    time.sleep(5)
                    hill.hill()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                hillSel2()
