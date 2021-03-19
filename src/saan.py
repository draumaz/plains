import os
import time
import mm2
import configparser
import textwrap
import inventory

def friendFlagger3(): #Neutral Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '3'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    saan()
def friendFlagger2(): #Rude Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '1'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    mm2.mainMenu2()
def friendFlagger1(): #Flirty Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '2'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    saan()
def flowerFlag(): #Gave Flower Flag
    config = configparser.ConfigParser()
    config['flower'] = {'var16': '3'}
    with open('save/config16.ini', 'w') as configfile:
        config.write(configfile)
    saan()

def saan():
    config = configparser.ConfigParser()
    config.read('save/config4.ini')
    var4 = config.getint('friendflag', 'var4')
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')
    config = configparser.ConfigParser()
    config.read('save/config16.ini')
    var16 = config.getint('flower', 'var16')

    if var8 == 0 and var6 == 1:
        os.system('cls||clear')
        print('\nThe Plains v0.21\n')
        inventory.invDisplay()
        print("Saan won't even look you in the eye.")
        time.sleep(4)
        mm2.mainMenu2()

    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    if var4 == 1:
        print('Saan seems distant.\n')
    if var4 != 1:
        print('Saan seems excited to talk to you.\n')
    print('WHERE ARE WE? [1]')
    print('FLIRT WITH HIM [2]')
    #print(' [3]')
    if var16 == 1:
        print('GIVE FLOWER [3]')
        print('BACK [4]')
    if var16 == 0 or var16 == 2 or var16 == 3:
        print('BACK [3]')
    saan2()

def saan2():
    config = configparser.ConfigParser()
    config.read('save/config4.ini')
    var4 = config.getint('friendflag', 'var4')
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')
    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')
    config = configparser.ConfigParser()
    config.read('save/config16.ini')
    var16 = config.getint('flower', 'var16')
    while True:
        try:
            friendSelect1 = int(input('\nACTION >> '))
            if friendSelect1 == 1:
                print('')
                print(textwrap.fill("Saan explains how far away you ended up. This planet is light years away from home..."))
                time.sleep(5)
                friendFlagger3()
            if friendSelect1 == 2:
                if var4 == 2:
                    print('')
                    print(textwrap.fill("You keep telling him how cute he is. He looks happy.", 75))
                    time.sleep(2)
                    saan()
                if var4 == 1:
                    print('\nHe seems busy right now.')
                    time.sleep(2)
                    saan()
                if var4 == 0 or 3:
                    print('\nYou tell Saan that he has cute eyes.')
                    time.sleep(3)
                    print("You're making him blush!")
                    time.sleep(2)
                    friendFlagger1()
            if friendSelect1 == 3:
                if var16 == 0 and var4 == 2:
                    print('\nSaan follows you back to where you started, looking happy.')
                    time.sleep(3)
                    mm2.mainMenu2()
                if var16 == 0 and var4 == 0:
                    print('\nSaan follows you back to where you started.')
                    time.sleep(3)
                    mm2.mainMenu2()
                if var16 == 1 and var4 == 1: #flower, rude
                    print('\nSaan reluctantly takes the flower. He looks confused.')
                    time.sleep(3)
                    flowerFlag()
                if var16 == 1 and var4 == 2: #flower, flirty
                    print("\nSaan looks borderline embarassed, you've made him blush quite a bit.")
                    time.sleep(3)
                    flowerFlag()
                if var16 == 1 and var4 == 3 or var16 == 1 and var4 == 0: #flower, neutral
                    print("\nSaan appreciates the flower. He admires its petals and form.")
                    time.sleep(3)
                    flowerFlag()
                if var16 == 3 or var16 == 2:
                    print("\nSaan follows you back to where you started, looking at the flower all the way.")
                    time.sleep(3)
                    mm2.mainMenu2()
                else:
                    print("\nYou and Saan head back.")
                    time.sleep(3)
                    mm2.mainMenu2()
            if friendSelect1 == 4:
                if var4 <= 1:
                    print('\nYou walk back without talking...how rude.')
                    time.sleep(2)
                    friendFlagger2()
                if var4 == 2:
                    print('')
                    print(textwrap.fill('You head back to the rest of your friends, Saan still blushing.', 75))
                    time.sleep(2)
                    mm2.mainMenu2()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            saan()
