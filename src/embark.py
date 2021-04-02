import os
import time
import mm2
import mm3
import textwrap
import scripts

def emb2Handler():
    while True:
        try:
            print("Save failed.")
            print('\nCONTINUE [1]')
            print('QUIT [2]\n')
            choose = int(input('ACTION >> '))
            if choose == 1:
                mm3.mainMenu3()
            if choose == 2:
                quit()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                emb2Handler()
        except ValueError:
            scripts.inpErrorHandler()
            emb2Handler()

def emb2End():
    print('\nYou decide to depart anyways, and your journey comes to an end.')
    time.sleep(3)
    scripts.screenClear()
    print('\n\nTHANK YOU SO MUCH FOR PLAYING!')
    time.sleep(4)
    line_ext = 13
    state_ext = 1
    scripts.saveWriter()
    quit()

def Embark2():
    print("\nSaan mentions how beautiful this planet is.")
    time.sleep(2)
    print("Seems like they all want to stick around for a bit.")
    time.sleep(2)
    print('\nLEAVE [1]')
    print('STAY [2]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                emb2End()
            if choose == 2:
                print('\nYou and your friends disembark.')
                line_ext = 1
                state_ext = 2
                scripts.saveWriter(line_ext, state_ext)
                time.sleep(3)
                scripts.screenClear()
                time.sleep(1)
                print('\nChapter Two complete.')
                time.sleep(2)
                scripts.screenClear()
                time.sleep(1)
                mm3.mainMenu3()
            if choose > 2 or choose < 0:
                scripts.inpErrorHandler()
                Embark2()
        except ValueError:
            scripts.inpErrorHandler()
            Embark2()

def Embark1():
    line_ext = 8
    state_ext = 1
    scripts.saveWriter(line_ext, state_ext)
    print('')
    print(textwrap.fill('Blood still dripping from your clothes, you lock the doors and take off, leaving your friends behind.', 75))
    time.sleep(6)
    scripts.screenClear()
    time.sleep(5)
    print('\nMONSTER')
    time.sleep(0.05)
    print('MONSTER')
    time.sleep(0.05)
    print('MONSTER')
    time.sleep(0.05)
    print('MONSTER')
    time.sleep(0.05)
    print('MONSTER')
    time.sleep(0.15)
    scripts.screenClear()
    quit()

def Embark():
    save = scripts.savePull()
    var6 = save[5]
    var8 = save[7]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    if var6 == 1 and var8 == 0:
        print('Ignoring your friends, you make your way to their spaceship and lock the doors.')
    if var6 == 0 or var8 == 1:
        print("You walk to your friends' ship. Your friends follow along.")
    print('\nLOOK AROUND [1]')
    print('SET OFF [2]')
    print('BACK [3]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var6 == 0:
                    print('')
                    print(textwrap.fill("This ship is gorgeous. Complex, shiny white metal covers the interior.", 75))
                    time.sleep(5)
                    Embark()
                if var6 == 1:
                    print('')
                    print(textwrap.fill("The ship doesn't matter, it's a getaway vehicle.", 75))
                    time.sleep(3)
                    Embark()
            if choose == 2:
                if var6 == 1 and var8 == 0:
                    Embark1()
                else:
                    Embark2()
            if choose == 3:
                print("\nYou decide against leaving quite yet.")
                mm2.mainMenu2()
            if choose > 3 or choose < 0:
                scripts.inpErrorHandler()
                Embark()
        except ValueError:
            scripts.inpErrorHandler()
            Embark()
