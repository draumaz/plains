import os
import time
import textwrap
import hill
import cave
import tool
import ch1end
import handig

def mainMenu1():
    save = handig.savePull()
    var1 = save[0]
    var6 = save[5]
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
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
        print('QUIT [5]')
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
                    handig.quitHandler()
                if var1 == 1:
                    ch1end.ch1End()
            if mainmenuSelect1 == 5:
                if var1 == 1:
                    handig.quitHandler()
                if var1 == 0:
                    handig.inpErrorHandler()
            if mainmenuSelect1 > 5 or mainmenuSelect1 < 0:
                handig.inpErrorHandler()
                mainMenu1()
        except ValueError:
            handig.inpErrorHandler()
            mainMenu1()
