import os
import time
import configparser
import saan

def friendFlagger1(): #Flirty Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '2'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    saan.saan()
