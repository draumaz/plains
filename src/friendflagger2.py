import os
import time
import configparser
import mm2

def friendFlagger2():
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '1'}
    with open('config4.ini', 'w') as configfile:
        config.write(configfile)
    mm2.mainMenu2()
