import os
import time
import mm1
import textwrap
import configparser

def hill():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    config.read('save/config.ini')
    var1 = config.getint('ch1endflag', 'var1')
    config = configparser.ConfigParser()
    config.read('save/config12.ini')
    var12 = config.getint('lizarddx', 'var12')

    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    if var6 == 0 and var1 == 0:
        print(textwrap.fill('That hill looks pretty strange. It juts out of the landscape in an unrealistic way.', 75))
    if var6 == 0 and var1 == 1:
        print(textwrap.fill("Having stood there, you hear a strange noise in the sky. Perhaps heading back to where you started will reveal the source.", 75))
    if var6 == 1 and var1 == 0:
        print('You should stand still.')
    if var6 == 1 and var1 == 1:
        print("They're coming. Go back.")
    if var6 == 0 and var12 == 0:
        print('In the distance, you can see a creature moving about.\n')
        print('GO TOWARDS THE CREATURE [1]')
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
            hillSelect = int(input('\nACTION >> '))

            if hillSelect == 1:
                if var12 == 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hill()
                if var12 == 0:
                    hillSel1()
            if hillSelect == 2:
                if var1 == 0:
                    hillSel2()
                if var1 == 1:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hill()
            if hillSelect == 3:
                hillSel3()
            if hillSelect == 4:
                if var6 == 0:
                    print('\nBest to head back.')
                    time.sleep(2)
                    mm1.mainMenu1()
                if var6 == 1:
                    mm1.mainMenu1()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hill()

def hs1e1():
    config = configparser.ConfigParser()
    config['lizarddx'] = {'var12': '1'}
    with open('save/config12.ini', 'w') as configfile:
        config.write(configfile)
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

def hillSel1Ext():
    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')
    config = configparser.ConfigParser()
    config.read('save/config15.ini')
    var15 = config.getint('blade', 'var15')

    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    print('The huge reptilian sees you, and approaches.')
    if var7 == 0:
        print('')
    if var7 == 1:
        time.sleep(2)
        print("Looks like he's having a sense of déjà vu.\n")
        time.sleep(3)
    if var15 == 1:
        print('KILL [1]')
    print('TALK [2]')
    print('BACK [3]')

    while True:
        try:
            hillSel1ExtSel = int(input('\nACTION >> '))

            if hillSel1ExtSel == 1:
                if var15 == 1:
                    print('\nYou run up to the lizard and stab him to death.')
                    time.sleep(3)
                    print('Blood stains your uniform.')
                    time.sleep(6)
                    lizardMan()
                if var15 == 0:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    hillSel1Ext()
            if hillSel1ExtSel == 2:
                if var7 == 1:
                    hs1e1()
                if var7 == 0:
                    hs1e2()
            if hillSel1ExtSel == 3:
                print('\nUpon seeing the towering lizard, you decide to head back.')
                time.sleep(2)
                hill()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hillSel1Ext()

def lizardMan():
    config = configparser.ConfigParser() #Live
    config['lizard'] = {'var6': '1'}
    with open('save/config6.ini', 'w') as configfile:
        config.write(configfile)
    config = configparser.ConfigParser() #Persist
    config['lizardext'] = {'var7': '1'}
    with open('save/config7.ini', 'w') as configfile:
        config.write(configfile)
    hill()

def hillSel1():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config5.ini')
    var5 = config.getint('reset', 'var5')

    os.system('cls||clear')
    print('\nThe Plains v0.21\n')

    if var6 == 1:
        print('Silence fills the air.\n')
        print('BACK [1]')

        while True:
            try:
                HS = int(input('\nACTION >> '))

                if HS == 1:
                    hill()

            except ValueError:
                print("\nDid you mean something else?")
                time.sleep(0.5)
                hillSel1()
    else:
        hillSel1Ext()

def standFlagger():
        config = configparser.ConfigParser()
        config['ch1endflag'] = {'var1': '1'}
        with open('save/config.ini', 'w') as configfile:
               config.write(configfile)
        hill()

def hs2Sub2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    if var6 == 0:
        print("\nStanding there motionless, it gives you the feeling that everything's going to be alright.\n")
    if var6 == 1:
        print("They're coming.")
    time.sleep(5)
    standFlagger()

def hs2Sub():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print("\nThey're coming.")
    time.sleep(5)
    standFlagger()

def hillSel2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    print('Despite the massive mountain ahead of you, you decide to simply stand still.')
    if var6 == 1:
        hs2Sub()
    if var6 == 0:
        time.sleep(2)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('Seems like a bit of a waste of time.')
        time.sleep(2)
        print('\nKEEP STANDING [1]')
        print('GO BACK [2]')

        while True:
            try:
                hillSel2Select = int(input('\nACTION >> '))
                if hillSel2Select == 1:
                    hs2Sub2()
                if hillSel2Select == 2:
                    print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
                    time.sleep(5)
                    hill()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                hillSel2()

def hillSel3():
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    print('You sit down in the grassy plains and look at the sky. It is absolutely gorgeous.')
    print('\nEXAMINE [1]')
    print('BACK [2]')

    while True:
        try:
            hillSel3Select = int(input('\nACTION >> '))

            if hillSel3Select == 1:
                print('\nLaying down on the grass, it makes you feel truly refreshed.')
                time.sleep(3)
                hill()
            if hillSel3Select == 2:
                print('\nYou decide that you have more important things to be doing.')
                time.sleep(2)
                hill()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hillSel3()
