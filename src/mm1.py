import os
import time
import configparser
from hill import hill
from cave import cave
from tool import tool
from ch1end import ch1End

config = configparser.ConfigParser()
config.read('config.ini')
var1 = config.getint('ch1endflag', 'var1')

def mainMenu1():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('You are Liam. An astronaut by trade, you took a bad turn on the Space Belt and landed on a strange planet.')
    print('You awaken, laying in a field of grass. You see hills, a cave, and strange flora.\n')
    print('HILL [1]')
    print('CAVE [2]')
    print('TOOL [3]')
    if var1 == 0:
        print('QUIT [4]')
    if var1 == 1:
        print('SOUND [4]')
    if var1 == 1:
        print('EXIT [5]')

    mainmenuSelect1 = int(input('\nACTION >> '))

    if mainmenuSelect1 == 1:
        hill()

    if mainmenuSelect1 == 2:
        cave()

    if mainmenuSelect1 == 3:
        tool()

    if mainmenuSelect1 == 4:
        if var1 == 0:
            print('\nThanks for playing!')
            time.sleep(0.5)
            quit()
        if var1 == 1:
            ch1End()

    if mainmenuSelect1 == 5:
        if var1 == 1:
            print('\nThanks for playing!')
            time.sleep(0.5)
            quit()
        if var1 == 0:
            mainMenu1()
