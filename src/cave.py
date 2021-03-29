import os
import time
import mm1
import textwrap
import handig

def cave():
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill('You make your way towards a deep, dark cave. You can barely see anything past the entrance.\n', 75))
    print('\nCONTINUE [1]')
    print('LOOK AROUND [2]')
    print('LISTEN [3]')
    print('BACK [4]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                caveSel1()
            if choose == 2:
                caveSel2()
            if choose == 3:
                caveSel3()
            if choose == 4:
                print('\nSeems pretty forboding...best to head back.')
                time.sleep(3)
                mm1.mainMenu1()
            if choose > 4 or choose < 0:
                handig.inpErrorHandler()
                cave()
        except ValueError:
            handig.inpErrorHandler()
            cave()

def caveSel1():
    save = handig.savePull()
    var15 = save[14]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    if var15 == 0:
        print("You continue deeper down the cave. There's a small box sitting near the wall.\n")
        print('OPEN [1]')
    if var15 == 1:
        print("Just a dingy old cave.\n")
        print("PUT KNIFE BACK [1]")
    if var15 == 2:
        print("You're deep into the cave. There's that box with the knife you put back.\n")
        print('TAKE [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var15 == 0:
                    cs1Knife()
                if var15 == 1:
                    cs1KnifeBack()
                if var15 == 2:
                    cs1Knife2()
            if choose == 2:
                if var15 == 0:
                    print("\nContinuing in a cave this dark is just asking for trouble.")
                    time.sleep(3)
                cave()
            if choose > 2 or choose < 0:
                handig.inpErrorHandler()
                caveSel1()
        except ValueError:
            handig.inpErrorHandler()
            caveSel1()

def cs1Knife():
    print('\nYou open the box and find a knife. You put it in your pocket.')
    line_ext = 14
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    time.sleep(3)
    caveSel1()

def cs1Knife2():
    print('\nYou take the knife back.')
    line_ext = 14
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    time.sleep(3)
    caveSel1()

def cs1KnifeBack():
    print('\nYou open the box and put the knife back.')
    line_ext = 14
    state_ext = 2
    handig.saveWriter(line_ext, state_ext)
    time.sleep(3)
    caveSel1()

def caveSel2():
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    print("Up against the entrance is a sign. It's written in a strange, alien system.\n")
    print('DECIPHER [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))

            if choose == 1:
                print('\nYou pull out your phone, and attempt to translate the symbols.')
                time.sleep(4)
                print('...looks like it says "Abandon all hope, ye who enter here".')
                time.sleep(4)
                print('\nBetter safe than sorry.')
                time.sleep(2)
                cave()
            if choose == 2:
                print("\nToo much work, anyways.")
                time.sleep(2)
                cave()
            if choose > 2 or choose < 0:
                handig.inpErrorHandler()
                caveSel2()
        except ValueError:
            handig.inpErrorHandler()
            caveSel2()

def caveSel3():
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    print("You focus your listening on the cave. You can hear a faint rumbling noise coming from within.\n")
    print('DISCERN [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                print('\nYou listen as hard as you can, in an attempt to discern words.')
                time.sleep(4)
                print("...that's certainly not any language you know.")
                time.sleep(2)
                cave()
            if choose == 2:
                print("\nYou figure that the rumbling is probably just natural noises.")
                time.sleep(2)
                cave()
            if choose > 2 or choose < 0:
                handig.inpErrorHandler()
                caveSel3()
        except ValueError:
            handig.inpErrorHandler()
            caveSel3()
