import os
import time
import configparser

def resetter():
    print('\nDoing this will reset everything. Are you sure?')
    print('\nRESET [1]')
    print('BACK [2]')
    reSel1 = int(input('\nACTION >> '))
    while reSel1 < 1 or reSel1 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        resetter()
    if reSel1 == 1:

        print('\nResetting...')

        config = configparser.ConfigParser()
        config['ch1endflag'] = {'var1': '0'}
        with open('save/config.ini', 'w') as configfile:
            config.write(configfile)

        config = configparser.ConfigParser()
        config['chaptflagger'] = {'var2': '0'}
        with open('save/config2.ini', 'w') as configfile:
            config.write(configfile)

        config = configparser.ConfigParser()
        config['toolflag'] = {'var3': '0'}
        with open('save/config3.ini', 'w') as configfile:
            config.write(configfile)

        config = configparser.ConfigParser()
        config['friendflag'] = {'var4': '0'}
        with open('save/config4.ini', 'w') as configfile:
            config.write(configfile)

        config = configparser.ConfigParser()
        config['reset'] = {'var5': '1'}
        with open('save/config5.ini', 'w') as configfile:
            config.write(configfile)

        config = configparser.ConfigParser()
        config['lizard'] = {'var6': '0'}
        with open('save/config6.ini', 'w') as configfile:
            config.write(configfile)

        time.sleep(0.5)

        print('Reset.')
        time.sleep(1)
        os.system('clear ')
        quit()
    if reSel1 == 2:
        print('\nThe game will now close. Your data was not altered.')
        time.sleep(2)
        quit()
