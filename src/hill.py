import os
import time
import mm1
import textwrap
import handig

def hill():
    save = handig.savePull()
    var1 = save[0]
    var6 = save[5]
    var12 = save[11]
    var16 = save[15]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    if var6 == 0 and var1 == 0:
        print(textwrap.fill('That hill looks pretty strange. It juts out of the landscape in an unrealistic way.', 75))
    if var6 == 0 and var1 == 1:
        print(textwrap.fill("Having stood there, you hear a strange noise in the sky. Perhaps heading back to where you started will reveal the source.", 75))
    if var6 == 1 and var1 == 0:
        print('You should stand still.')
    if var6 == 1 and var1 == 1:
        print("They're coming. Go back.")
    if var6 == 0 and var12 == 0 and var16 != 2:
        print('In the distance, you can see a creature moving about.\n')
        print('GO TOWARDS THE CREATURE [1]')
    if var16 == 2:
        print('You can see the lizard sitting down, enjoying the sun.\n')
        print('VISIT HIM [1]')
    if var12 == 1:
        print('')
    if var6 == 1:
        print('')
        print('GO FORWARDS [1]')
    if var1 == 0:
        print('STAND STILL [2]')
    print('TAKE A BREAK [3]')
    print('BACK [4]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var12 == 1:
                    handig.inpErrorHandler()
                    hill()
                if var12 == 0:
                    hillSel1()
            if choose == 2:
                if var1 == 0:
                    hillSel2()
                if var1 == 1:
                    handig.inpErrorHandler()
                    hill()
            if choose == 3:
                hillSel3()
            if choose == 4:
                if var6 == 0:
                    print('\nBest to head back.')
                    time.sleep(2)
                    mm1.mainMenu1()
                if var6 == 1:
                    mm1.mainMenu1()
            if choose > 4 or choose < 0:
                handig.inpErrorHandler()
                hill()
        except ValueError:
            handig.inpErrorHandler()
            hill()

def hs1e1():
    line_ext = line[11]
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    print('\nThe reptilian man seems untrusting of you, and leaves the area pretty quickly.')
    time.sleep(5)
    hill()

def hs1e2():
    print('\nThe reptilian comes to you, and gives you some information.')
    time.sleep(2)
    print("You're far from home, aren'tcha?")
    time.sleep(2)
    print("...not really helpful. But he means well.")
    time.sleep(3)
    hill()

def hs1e3():
    print('')
    print(textwrap.fill('The reptilian tells you that everyone seems to be scared of him, except for you.', 75))
    time.sleep(3)
    print('He looks really happy.')
    time.sleep(2)
    hill()

def hillSel1Ext():
    save = handig.savePull()
    var7 = save[6]
    var15 = save[14]
    var16 = save[15]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    if var16 != 2:
        print('The huge reptilian sees you, and approaches.')
    if var16 == 2:
        print('The reptilian waves and smiles at you.')
    if var7 == 0:
        print('')
    if var7 == 1:
        time.sleep(2)
        print("Looks like he's having a sense of déjà vu.\n")
        time.sleep(3)
    if var15 == 1:
        print('KILL [1]')
    print('TALK [2]')
    if var16 == 0:
        print('BACK [3]')
    if var16 == 1:
        print('GIVE FLOWER [3]')
        print('BACK [4]')
    if var16 == 2:
        print('BACK [3]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var16 == 2 and var15 == 1:
                    print('\nI genuinely do not have the heart to program a scenario for this.')
                    time.sleep(2)
                    print('Sorry!')
                    time.sleep(0.25)
                    print('-draumaz')
                    time.sleep(2)
                    hill()
                if var15 == 1:
                    line_ext = 5
                    state_ext = 1
                    handig.saveWriter(line_ext, state_ext)
                    line_ext = 6
                    state_ext = 1
                    handig.saveWriter(line_ext, state_ext)
                    print('\nYou run up to the lizard and stab him to death.')
                    time.sleep(3)
                    print('Blood stains your uniform.')
                    time.sleep(6)
                    hill()
                if var15 == 0:
                    handig.inpErrorHandler()
                    hillSel1Ext()
            if choose == 2:
                if var7 == 0 and var16 == 2:
                    hs1e3()
                if var7 == 1:
                    hs1e1()
                if var7 == 0:
                    hs1e2()
            if choose == 3:
                if var16 == 0:
                    print('\nUpon seeing the towering lizard, you decide to head back.')
                    time.sleep(2)
                    hill()
                if var16 == 1:
                    print('\nYou give the lizard man the flower. He smiles at you.')
                    line_ext = 15
                    state_ext = 2
                    handig.saveWriter(line_ext, state_ext)
                    time.sleep(3)
                    hillSel1Ext()
                if var16 == 2:
                    print('')
                    print(textwrap.fill("That lizard looks like nobody's shown him kindness before this in a long while...", 75))
                    time.sleep(4)
                    hill()
            if choose == 4:
                if var16 == 0:
                    handig.inpErrorHandler()
                    hillSel1Ext()
                if var16 == 1:
                    print('\nUpon seeing the towering lizard, you decide to head back.')
                    time.sleep(2)
                    hill()
            if choose > 4 or choose < 0:
                handig.inpErrorHandler()
                hillSel1Ext()
        except ValueError:
            handig.inpErrorHandler()
            hillSel1Ext()

def hillSel1():
    save = handig.savePull()
    var5 = save[4]
    var6 = save[5]
    var16 = save[15]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    if var6 == 1:
        print('Silence fills the air.\n')
        if var16 == 1:
            print('FLOWER [1]')
        print('BACK [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    if var16 == 1:
                        line_ext = 15
                        state_ext = 4
                        handig.saveWriter(line_ext, state_ext)
                        print('')
                        print(textwrap.fill('You lay the flower down next to his lifeless corpse.', 75))
                        time.sleep(3)
                        hill()
                    if var16 == 4:
                        hillSel1()
                if choose == 2:
                    hill()
                if choose > 2 or choose < 0:
                    handig.inpErrorHandler()
                    hillSel1()
            except ValueError:
                handig.inpErrorHandler()
                hillSel1()
    hillSel1Ext()

def hs2Sub2():
    save = handig.savePull()
    var6 = save[5]
    line_ext = 0
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    print('...')
    time.sleep(3)
    print("\nYou're completely motionless.")
    time.sleep(2)
    print(textwrap.fill("And then suddenly, you hear a sound. Perhaps heading back will reveal its source.", 75))
    time.sleep(5)
    hill()

def hs2Sub():
    line_ext = 0
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print("\nThey're coming.")
    time.sleep(5)

def hillSel2():
    save = handig.savePull()
    var6 = save[5]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    if var6 == 0:
        print('Despite the massive mountain ahead of you, you decide to simply stand still.')
    if var6 == 1:
        hs2Sub()
    if var6 == 0:
        time.sleep(2)
        print('...')
        time.sleep(2.5)
        print('Seems like a bit of a waste of time.')
        time.sleep(2)
        print('\nKEEP STANDING [1]')
        print('GO BACK [2]')
        while True:
            try:
                choose = int(input('\nACTION >> '))
                if choose == 1:
                    hs2Sub2()
                if choose == 2:
                    print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
                    time.sleep(5)
                    hill()
                if choose > 2 or choose < 0:
                    handig.inpErrorHandler()
                    hillSel2()
            except ValueError:
                handig.inpErrorHandler()
                hillSel2()

def hillSel3():
    save = handig.savePull()
    var16 = save[15]
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill("You sit down in the grassy plains and take a look around.", 75))
    if var16 == 0:
         print("There's a beautiful flower sitting there.")
    if var16 == 0:
        print('\nPICK [1]')
    if var16 == 1:
        print('')
    print('LAY DOWN [2]')
    print('BACK [3]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                print('')
                print(textwrap.fill('The flower comes off its root without hesitation.', 75))
                print(textwrap.fill('You put it in your pocket.', 75))
                line_ext = 15
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                time.sleep(3)
                hillSel3()
            if choose == 2:
                print('\nLaying down on the grass, it makes you feel truly refreshed.')
                time.sleep(3)
                hill()
            if choose == 3:
                print('\nYou decide that you have more important things to be doing.')
                time.sleep(2)
                hill()
            if choose > 3 or choose < 0:
                handig.inpErrorHandler()
                hillSel3()
        except ValueError:
            handig.inpErrorHandler()
            hillSel3()
