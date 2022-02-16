import os
import time
import mm2
import textwrap
import scripts

def talk():
    save = scripts.savePull()
    var6 = save[5]
    var7 = save[6]
    var8 = save[7]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    if var6 == 0 or var7 == 0 or var8 == 1: #Normal/post-explain
        print("Your friends are relieved that you're alright.\n")
    if var6 == 1 and var8 == 0: #Murder, pre-explain
        print('Your friends look at you with horrified expressions.\n')
    if var7 == 1 and var6 == 0 and var8 == 0: #Murdered before reset
            print('...they seem worried.\n')
    if var6 == 0 or var8 == 1: #Normal/post-explain
        print('CHIT-CHAT [1]')
    if var6 == 1 and var8 == 0 and var7 == 1: #Murder
        print("WHAT'S WITH THAT LOOK? [1]")
    print('STARE [2]')
    print('BACK [3]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var6 == 1 and var8 == 0:
                    talkSel1C()
                else:
                    talkSel1()
            if choose == 2:
                talkSel2()
            if choose == 3:
                if var6 == 1:
                    mm2.mainMenu2()
                if var6 == 0:
                    print('\nYou tell your friends you need a minute.')
                    time.sleep(2)
                    mm2.mainMenu2()
            if choose > 4 or choose < 0:
                scripts.inpErrorHandler()
                talk()
        except ValueError:
            scripts.inpErrorHandler()
            talk()

def talkSel1A():
    save = scripts.savePull()
    var7 = save[6]
    var8 = save[7]
    if var7 == 0 or var8 == 1:
        scripts.screenClear()
        scripts.versionHeader()
        scripts.invDisplay()
        print("Your friends ask you why you didn't use any of your tools to contact them.\n")
        print('UH... [1]')
        print('BACK [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    print("\nYour friends tell you to not to worry about it.")
                    time.sleep(2)
                    talk()
                if choose == 2:
                    print("\nYou pretend that you're getting a call on your phone to avoid this awkward conversation.")
                    time.sleep(4)
                    talk()
                if choose > 2 or choose < 0:
                    scripts.inpErrorHandler()
                    talkSel1()
            except ValueError:
                scripts.inpErrorHandler()
                talkSel1()
    if var7 == 1 and var8 == 0:
        talkSel1B()

def talkSel1B():
    print('\nYour friends ask you a question.')
    time.sleep(2)
    print('"Liam, is everything alright?"\n')
    time.sleep(2)
    print('EXPLAIN [1]')
    print('BACK [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                line_ext = 7
                state_ext = 1
                scripts.saveWriter(line_ext, state_ext)
                talk()
                print("\nYou explain to them that you're just feeling off.")
                time.sleep(3)
                print("\n:)")
                talk()
            if choose == 2:
                print("\nThey wouldn't get it.")
                time.sleep(5)
                talk()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                talkSel1B()
        except ValueError:
            scripts.inpErrorHandler()
            talkSel1B()

def talkSel1C():
    save = scripts.savePull()
    var6 = save[5]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    if var6 == 1:
        print('Your friends barely stammer out a question.')
        time.sleep(2)
        print('"Liam, why are you covered in blood?"\n')
        time.sleep(2)
        print('EXPLAIN [1]')
        print('RUN AWAY [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    print('\nYou explain to your friends that it was self-defense.')
                    time.sleep(2)
                    print('They understand, and help you clean off.')
                    time.sleep(2)
                    print('They seriously bought that?')
                    time.sleep(0.5)
                    talkSel1CG()
                if choose == 2:
                    print("\nYou can't face them.")
                    time.sleep(2)
                    mm2.mainMenu2()
                if choose > 2 or choose < 0:
                    scripts.inpErrorHandler()
                    talkSel1C()
            except ValueError:
                scripts.inpErrorHandler()
                talkSel1C()
    if var6 == 0:
        talk()

def talkSel1():
    save = scripts.savePull()
    var3 = save[2]
    var7 = save[6]
    var8 = save[7]
    if var3 == 1:
        if var7 == 0 or var8 == 1:
            print('')
            print(textwrap.fill("Your friends mentioned that they heard your scanner signal, and knew to come find you.", 75))
            time.sleep(5)
            talk()
        if var7 == 1 and var8 == 0:
            talkSel1B()
    if var3 == 0:
        talkSel1A()

def talkSel2():
        scripts.screenClear()
        scripts.versionHeader()
        scripts.invDisplay()
        print("You just...stare at them. They look bewildered.\n")
        print('KEEP STARING [1]')
        print('GO BACK [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    print('')
                    print(textwrap.fill("Your unblinking eyes eventually cause them to wonder if there's something seriously wrong with you.", 75))
                    time.sleep(5)
                    talk()
                if choose == 2:
                    print("\nYeah, this is pretty bizarre.")
                    time.sleep(1.5)
                    talk()
                if choose > 2 or choose < 0:
                    scripts.inpErrorHandler()
                    talkSel2()
            except ValueError:
                scripts.inpErrorHandler()
                talkSel2()
