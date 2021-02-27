import os
import time
import reset
import configparser

def settings1():
    config = configparser.ConfigParser() #Fetch var13 setting
    config.read('save/config13.ini')
    var13 = config.getint('splashskip2', 'var13')

    if var13 == 1:
        config = configparser.ConfigParser()
        config['splashskip2'] = {'var13': '0'}
        with open('save/config13.ini', 'w') as configfile:
            config.write(configfile)
        print('\nSplash screen enabled.')
        time.sleep(1)
        settingsMain()
    if var13 == 0:
        config = configparser.ConfigParser()
        config['splashskip2'] = {'var13': '1'}
        with open('save/config13.ini', 'w') as configfile:
            config.write(configfile)
        print('\nSplash screen disabled.')
        time.sleep(1)
        settingsMain()

def settingsMain():

    os.system('cls||clear')
    print('\nThe Plains v0.19')
    print('\nTOGGLE SPLASH SCREEN [1]')
    print('RESET [2]')
    print('QUIT [3]')
    while True:
        try:
            setSel = int(input('\nACTION >> '))
            if setSel == 1:
                settings1()
            if setSel == 2:
                os.system('clear||cls')
                reset.resetter()
            if setSel == 3:
                os.system('clear||cls')
                quit()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            settingsMain()
