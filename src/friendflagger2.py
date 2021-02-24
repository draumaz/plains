import os
import time
import configparser
import mm2

def friendFlagger2(): #Rude Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '1'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    mm2.mainMenu2()
