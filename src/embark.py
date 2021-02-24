import os
import time
import mm2
import embark2
import configparser
import textwrap

def Embark():

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    if var6 == 1 and var8 == 0:
        print('Ignoring your friends, you make your way to their spaceship and sit inside.')
    if var6 == 0 or var8 == 1:
        print("You walk to your friends' ship.")
    print('\nACTION1 [1]')
    print('SET OFF [2]')
    print('BACK [3]')

    embSelect = int(input('\nACTION >> '))

    while embSelect < 1 or embSelect > 3:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        Embark()

    if embSelect == 2:
        if var6 == 1 and var8 == 0:
            print(textwrap.fill('\nBlood still dripping from your clothes, you lock the doors and take off, leaving your friends behind.', 75))
            time.sleep(6)
            os.system('cls||clear')
            time.sleep(5)
            print('\nMONSTER')
            time.sleep(0.05)
            print('MONSTER')
            time.sleep(0.05)
            print('MONSTER')
            time.sleep(0.5)
            config = configparser.ConfigParser()
            config['badend'] = {'var9': '1'}
            with open('save/config9.ini', 'w') as configfile:
                   config.write(configfile)
            os.system('cls||clear')
            quit()
        else:
            embark2.Embark2()

    if embSelect == 3:
        print("\nYou decide against leaving quite yet.")
        mm2.mainMenu2()
