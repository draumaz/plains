import os
import time
import mm1
import textwrap
import scripts

def toolEx():
    save = scripts.savePull()
    var1 = save[0]
    var3 = save[2]
    if var3 == 0:
        print('')
        print(textwrap.fill("You decide that checking your tools isn't worth your time or effort.", 75))
        time.sleep(3)
        mm1.mainMenu1()
    if var3 == 1:
        print('')
        print("With your friends contacted, you decide to head back.")
        time.sleep(2)
        if var1 != 1:
            print(textwrap.fill("Seems like a good time to stand in front of a hill for a while.", 75))
        time.sleep(4)
        print(";)")
        time.sleep(0.05)
        mm1.mainMenu1()

def tool():
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    print(textwrap.fill('Seeming to be completely stranded, you decide to use the tools at your disposal.\n', 75))
    print('\nPHONE [1]')
    print('RADAR [2]')
    print('SCANNER [3]')
    print('BACK [4]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                toolSel1()
            if choose == 2:
                toolSel2()
            if choose == 3:
                toolSel3()
            if choose == 4:
                toolEx()
            if choose > 4 or choose < 0:
                scripts.inpErrorHandler()
                tool()
        except ValueError:
            scripts.inpErrorHandler()
            tool()

def toolSel1():
    save = scripts.savePull()
    var3 = save[2]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    print('You pull out your phone. Unsurprisingly, the signal is rather weak.\n')
    print('MESSAGE A FRIEND [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var3 == 0:
                    print("\nThe message won't even go through...")
                    time.sleep(4)
                    tool()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if choose == 2:
                if var3 == 0:
                    print("\nWhat good's a phone without service?")
                    time.sleep(3)
                    tool()
                if var3 == 1:
                    tool()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                toolSel1()
        except ValueError:
            scripts.inpErrorHandler()
            toolSel1()

def toolSel2():
    save = scripts.savePull()
    var3 = save[2]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    print('Using your radar, you can attempt to establish contact.\n')
    print('SCAN [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var3 == 0:
                    print('\nYou try establishing contact...your radar just shuts off.')
                    time.sleep(4)
                    tool()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if choose == 2:
                if var3 == 0:
                    print("\nProbably wouldn't work, anyway.")
                    time.sleep(2)
                    tool()
                if var3 == 1:
                    tool()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                toolSel2()
        except ValueError:
            scripts.inpErrorHandler()
            toolSel2()

def toolSel3():
    save = scripts.savePull()
    var3 = save[2]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    print('Looks like your scanner is functioning just fine.\n')
    print('SIGNAL [1]')
    print('BACK [2]')

    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var3 == 0:
                    line_ext = 2
                    state_ext = 1
                    scripts.saveWriter(line_ext, state_ext)
                    line_ext = 0
                    state_ext = 1
                    scripts.saveWriter(line_ext, state_ext)
                    print('\nYou try to send out a signal, and it looks like it was received!\n')
                    time.sleep(4)
                    tool()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if choose == 2:
                if var3 == 0:
                    print("\nProbably wouldn't work, anyway.")
                    time.sleep(2)
                    tool()
                if var3 == 1:
                    tool()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                toolSel3()
        except ValueError:
            scripts.inpErrorHandler()
            toolSel3()