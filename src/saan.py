import os
import time
import mm2
import friendflagger1
import friendflagger2
import configparser
import textwrap

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
    if var8 == 0 and var6 == 1:
        os.system('cls||clear')
        print('\nThe Plains v0.18\n')
        print("Saan won't even look you in the eye.")
        time.sleep(4)
        mm2.mainMenu2()
    else:
        os.system('cls||clear')
        print('\nThe Plains v0.18\n')
        print('Saan seems excited to talk to you.\n')
        #print('SPECIFICS [1]')
        print('FLIRT [2]')
        #print('SOMETHING [3]')
        print('BACK [4]')

        friendSelect1 = int(input('\nACTION >> '))

        while friendSelect1 < 1 or friendSelect1 > 4:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            saan()

        if friendSelect1 == 1:
            #print('Placeholder1')
            #time.sleep(0.5)
            saan()

        if friendSelect1 == 2:
            if var4 == 2:
                print('')
                print(textwrap.fill("You keep telling him how cute he is. He looks happy.", 75))
                time.sleep(2)
                saan()

            if var4 == 1:
                print('He seems busy right now.')
                time.sleep(2)
                saan()

            if var4 == 0:
                print('\nYou tell Saan that he has cute eyes.')
                time.sleep(3)
                print("You're making him blush!")
                time.sleep(2)
                friendflagger1.friendFlagger1()

        if friendSelect1 == 3:
            #print('Placeholder3')
            #time.sleep(0.5)
            saan()

        if friendSelect1 == 4:
            if var4 <= 1:
                print('\nYou walk back without talking...how rude.')
                time.sleep(2)
                friendflagger2.friendFlagger2()
            if var4 == 2:
                print('')
                print(textwrap.fill('You head back to the rest of your friends, Saan still blushing.', 75))
                time.sleep(2)
                mm2.mainMenu2()
