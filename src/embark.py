import os
import time
import mm2
import configparser
import textwrap

def emb2End():
    print('\nYou decide to depart anyways, and your journey comes to an end.')
    time.sleep(3)
    os.system('cls||clear')
    print('\n\nTHANK YOU SO MUCH FOR PLAYING!')
    time.sleep(4)
    config = configparser.ConfigParser()
    config['gameover'] = {'var14': '1'}
    with open('save/config14.ini', 'w') as configfile:
        config.write(configfile)
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
            embSelect2 = int(input('\nACTION >> '))

            if embSelect2 == 1:
                emb2End()
            if embSelect2 == 2:
                print('\nYour friends have a point. You decide to stick around.')
                time.sleep(3)
                mm2.mainMenu2()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            Embark2()

def Embark1():
    print('')
    print(textwrap.fill('Blood still dripping from your clothes, you lock the doors and take off, leaving your friends behind.', 75))
    time.sleep(6)
    os.system('cls||clear')
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
    config = configparser.ConfigParser()
    config['badend'] = {'var9': '1'}
    with open('save/config9.ini', 'w') as configfile:
           config.write(configfile)
    os.system('cls||clear')
    quit()

def Embark():

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    if var6 == 1 and var8 == 0:
        print('Ignoring your friends, you make your way to their spaceship and lock the doors.')
    if var6 == 0 or var8 == 1:
        print("You walk to your friends' ship.")
    print('\nACTION1 [1]')
    print('SET OFF [2]')
    print('BACK [3]')

    while True:
        try:
            embSelect = int(input('\nACTION >> '))

            if embSelect == 2:
                if var6 == 1 and var8 == 0:
                    Embark1()
                else:
                    Embark2()
            if embSelect == 3:
                print("\nYou decide against leaving quite yet.")
                mm2.mainMenu2()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            Embark()
