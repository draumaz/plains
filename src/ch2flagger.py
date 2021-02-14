import os
import time
import configparser
import hill

def ch2Flagger():
        config = configparser.ConfigParser()
        config['ch1endflag'] = {'var1': '1'}
        with open('config.ini', 'w') as configfile:
               config.write(configfile)
        hill.hill()
