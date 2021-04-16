import os
import time
import mm1
import mm2
import mm3
import reset
import textwrap
import scripts

def breakTest():
    while True:
        try:
            file = open('e.txt', 'r')
            file.close()
            scripts.screenClear()
            print('\nFATAL ERROR OCCURRED\n')
            time.sleep(1)
            reset.resetter()
            quit()
        except FileNotFoundError:
            fileTest()

def fileTest():
    while True:
        try:
            saves = scripts.savePull()
            splashScreen()
        except (NameError, IndexError):
            scripts.saveGenerator()
            fileTest()

def splashDisp():
    print('\n==THE PLAINS===============')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON!=======')
    print('==CHARACTER BY BRYCE CANO==')

def splashScreen(): #Main menu
    save = scripts.savePull()
    var9 = save[8]
    var10 = save[9]
    var14 = save[13]
    if var10 == 1:
        mainAlt2()
    if var9 == 1:
        mainExt()
    if var9 == 0:
        scripts.screenClear()
        splashDisp()
        if var14 == 0:
            print('\nPLAY [1]')
        if var14 == 1:
            print('\nPLAY [1] ★')
        print('RESET [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    saveLoader()
                if choose == 2:
                    scripts.screenClear()
                    reset.resetter()
                    splashScreen()
                if choose < 1 or choose > 2:
                    scripts.inpErrorHandler()
                    splashScreen()
            except ValueError:
                scripts.inpErrorHandler()
                splashScreen()

def saveLoader():
    save = scripts.savePull()
    var2 = save[1]
    var14 = save[13]
    if var14 == 0:
        if var2 == 0: #Chapter 1
            mm1.mainMenu1()
        if var2 == 1: #Chapter 2
            mm2.mainMenu2()
        if var2 == 2: #Chapter 3
            print('')
            print(textwrap.fill('WARNING: This chapter is NOT ready! Only proceed if you are prepared for some seriously in-progress work...', 75))
            time.sleep(4)
            mm3.mainMenu3()
    if var14 == 1:
        mm3.mainMenu3()

##BAD ENDING FUNCTIONS##

def mainExt():
    scripts.screenClear()
    print('\n==AAAAAAAAAA==')
    print('==AAAAAAAA AAAAAAA AAAAAAA==')
    print('==KILLER KILLER KILLER==')
    print('==KILLER KILLER==')
    time.sleep(0.08)
    scripts.screenClear()
    splashDisp()
    time.sleep(5)
    mainExt2()

def mainExt2():
    scripts.screenClear()
    splashDisp()
    print('\n[3]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 3:
                mainAlt()
        except ValueError:
            mainExt2()

def mainAlt():
    scripts.screenClear()
    print('\n...')
    time.sleep(5)
    print("\nYou killed him.")
    time.sleep(3)
    print("You abandoned your friends.")
    time.sleep(3)
    scripts.screenClear()
    print('\n...')
    time.sleep(2)
    mainAlt2()

def mainAlt2():
    save = scripts.savePull()
    var10 = save[9]
    scripts.screenClear()
    print("\nDo you regret it?")
    print('\nYES [1]')
    print('NO [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                mainAlt3()
            if choose == 2:
                if var10 == 1:
                    time.sleep(0.75)
                    print('\nError.')
                    time.sleep(0.5)
                    mainAlt2()
                if var10 == 0:
                    print("\nYou're proud of it.")
                    time.sleep(2)
                    print("Here's your chance.")
                    time.sleep(1)
                    reset.resetter()
        except ValueError:
            mainAlt2()

def mainAlt3():
    print('\nSo you regret what you have done.')
    time.sleep(2)
    print('You know, that changes nothing.')
    time.sleep(2)
    print("You killed him.")
    time.sleep(2)
    print(textwrap.fill("Think about what that means. You downloaded a game, just to kill an innocent creature.", 75))
    time.sleep(3)
    print("Does that make you feel good?")
    time.sleep(4)
    print("The ability to hurt others, without recourse?")
    time.sleep(4)
    scripts.screenClear()
    time.sleep(2)
    print('\nYou still have the chance to make things right.')
    time.sleep(2)
    print('You can go back there, do the right thing.')
    time.sleep(2)
    mainAlt4()

def mainAlt4():
    scripts.screenClear()
    print('\nWill you?')
    print('\nYES [1]')
    print('NO [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                line_ext = 8
                state_ext = 0
                scripts.saveWriter(line_ext, state_ext)
                line_ext = 9
                state_ext = 0
                scripts.saveWriter(line_ext, state_ext)
                time.sleep(2)
                reset.resetter()
            if choose == 2:
                mainAlt5()
        except ValueError:
            mainAlt4()

def mainAlt5():
    scripts.screenClear()
    line_ext = 9
    state_ext = 1
    scripts.saveWriter(line_ext, state_ext)
    time.sleep(5)
    print('\nFATAL ERROR ENCOUNTERED')
    time.sleep(2)
    dest = open('e.txt', 'w+')
    dest.write('EVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\n')
    dest.close()
    quit()

breakTest() #Execution call
