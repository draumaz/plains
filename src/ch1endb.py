import os
import time
import configparser
import mm2

def ch1EndB():
    config = configparser.ConfigParser()
    config['chaptflagger'] = {'var2': '1'}
    with open('save/config2.ini', 'w') as configfile:
            config.write(configfile)
    time.sleep(0.5)
    print('Saved.')
    time.sleep(1)
    mm2.mainMenu2()
