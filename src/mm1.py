import os
import time
import textwrap
import hill
import cave
import tool
import ch1end
import scripts

def mainMenu1():
    save = scripts.savePull()
    var1 = save[0]
    var6 = save[5]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
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
            choose = int(input('\nACTION >> '))
            if choose == 1:
                hill.hill()
            if choose == 2:
                cave.cave()
            if choose == 3:
                tool.tool()
            if choose == 4:
                if var1 == 0:
                    scripts.quitHandler()
                if var1 == 1:
                    ch1end.ch1End()
            if choose == 5:
                if var1 == 1:
                    scripts.quitHandler()
                if var1 == 0:
                    scripts.inpErrorHandler()
            if choose > 5 or choose < 0:
                scripts.inpErrorHandler()
                mainMenu1()
        except ValueError:
            scripts.inpErrorHandler()
            mainMenu1()
