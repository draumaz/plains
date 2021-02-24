import os
import time
import configparser
import hill

def standFlagger():
        config = configparser.ConfigParser()
        config['ch1endflag'] = {'var1': '1'}
        with open('save/config.ini', 'w') as configfile:
               config.write(configfile)
        hill.hill()
