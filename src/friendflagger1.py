import os
import time
import configparser
import friend1

def friendFlagger1(): #Rude Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '2'}
    with open('config4.ini', 'w') as configfile:
        config.write(configfile)
    friend1.friend1()
