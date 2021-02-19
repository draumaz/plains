import os
import time
import configparser

def resetter():
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

    time.sleep(0.5)

    print('Reset.')
    time.sleep(1)
    quit()
