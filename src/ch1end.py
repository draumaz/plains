import os
import time
import mm2
import configparser
from configparser import NoSectionError
from configparser import NoOptionError
import textwrap
import handig

def ch1EndBHandler():
    while True:
        try:
            print('Save failed.')
            time.sleep(1)
            print('\nCONTINUE [1]')
            print('QUIT [2]\n')
            ch1EndSel = int(input('ACTION >> '))
            if ch1EndSel == 1:
                mm2.mainMenu2()
            if ch1EndSel == 2:
                quit()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            ch1EndBHandler()

def ch1EndB():
    while True:
        try:
            print('\nSaving...')
            config = configparser.ConfigParser()
            config['chaptflagger'] = {'var2': '1'}
            with open('save/config2.ini', 'w') as configfile:
                    config.write(configfile)
            mm2.mainMenu2()
        except (NoSectionError, NoOptionError):
            ch1EndBHandler()

def ch1End():
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill("You didn't notice it at first, but alongside a strange noise, you see a black disc in the sky.\n", 75))
    print('\nLOOK [1]')
    while True:
        try:
            ch1EndSelect = int(input('\nACTION >> '))
            if ch1EndSelect == 1:
                print('')
                print(textwrap.fill('The spacecraft descends from the sky, and lands safely. A hatch opens, and your friends walk out.', 75))
                time.sleep(5)
                ch1EndB()
            if ch1EndSelect > 1 or ch1EndSelect < 0:
                ch1End()
        except ValueError:
            ch1End()
