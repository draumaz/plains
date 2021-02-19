import os
import time
import configparser
import hill
import cave
import tool
import ch1end

def mainMenu1():
    os.system('clear')
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')
    print('\nThe Plains v0.16\n')
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

    while mainmenuSelect1 < 1 or mainmenuSelect1 > 5:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        mainMenu1()

    if mainmenuSelect1 == 1:
        hill.hill()

    if mainmenuSelect1 == 2:
        cave.cave()

    if mainmenuSelect1 == 3:
        tool.tool()

    if mainmenuSelect1 == 4:
        if var1 == 0:
            os.system('clear')
            print('\nThanks for playing!')
            time.sleep(0.5)
            quit()
        if var1 == 1:
            ch1end.ch1End()

    if mainmenuSelect1 == 5:
        if var1 == 1:
            print('\nThanks for playing!')
            time.sleep(0.5)
            quit()
        if var1 == 0:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu1()
