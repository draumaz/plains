import os
import time
import hill
import mm1
import hillsel1ext
import configparser

def hillSel1():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config5.ini')
    var5 = config.getint('reset', 'var5')

    os.system('clear')
    print('\nThe Plains v0.16\n')
    if var6 == 1:
        if var5 == 0:
            print('You killed him.')
            time.sleep(5)
            mm1.mainMenu1()
        if var5 == 1:
            print('You know what you did.')
            time.sleep(5)
            mm1.mainMenu1()
    if var6 == 0:
        hillsel1ext.hillSel1Ext()
