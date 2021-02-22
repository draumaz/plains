import time
import os
import talk
import configparser

def talkSel1EG():
    config = configparser.ConfigParser()
    config['okay'] = {'var8': '1'}
    with open('save/config8.ini', 'w') as configfile:
        config.write(configfile)
    talk.talk()
