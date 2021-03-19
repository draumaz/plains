import os
import time
import configparser
import textwrap
import hill
import cave
import tool
import ch1end
import inventory

def mainMenu1():
    os.system('cls||clear')
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    inventory.invDisplay()
    if var6 == 0:
        print(textwrap.fill('You are Liam. An astronaut by trade, you took a bad turn on the Space Belt and landed on a strange planet. You awaken, laying in a field of grass. You see hills, a cave, and strange flora.', 75))
    if var6 == 1:
        print(textwrap.fill("You're covered in the blood of the innocent reptilian man that you killed. The sky rumbles.", 75))
    print('\nHILL [1]')
    print('CAVE [2]')
    print('TOOL [3]')
    if var1 == 0:
        print('QUIT [4]')
    if var1 == 1:
        print('SOUND [4] <--')
    if var1 == 1:
        print('EXIT [5]')

    while True:
        try:
            mainmenuSelect1 = int(input('\nACTION >> '))
            if mainmenuSelect1 == 1:
                hill.hill()
            if mainmenuSelect1 == 2:
                cave.cave()
            if mainmenuSelect1 == 3:
                tool.tool()
            if mainmenuSelect1 == 4:
                if var1 == 0:
                    exitHandler()
                if var1 == 1:
                    ch1end.ch1End()
            if mainmenuSelect1 == 5:
                if var1 == 1:
                    exitHandler()
                if var1 == 0:
                    errorHandler()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu1()

def errorHandler():
    print('\nDid you mean something else?')
    time.sleep(0.5)
    mainMenu1()

def exitHandler():
    print('\nThanks for playing!')
    time.sleep(0.5)
    quit()
