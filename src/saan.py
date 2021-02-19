import os
import time
import mm2
import friendflagger1
import friendflagger2
import configparser

def saan():
    config = configparser.ConfigParser()
    config.read('save/config4.ini')
    var4 = config.getint('friendflag', 'var4')

    os.system('clear')
    print('\nThe Plains v0.16\n')
    print('Saan seems excited to talk to you.\n')
    print('SPECIFICS [1]')
    print('FLIRT [2]')
    print('SOMETHING [3]')
    print('BACK [4]')

    friendSelect1 = int(input('\nACTION >> '))

    while friendSelect1 < 1 or friendSelect1 > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        friend1()

    if friendSelect1 == 1:
        print('Placeholder1')
        time.sleep(0.5)
        friend1()

    if friendSelect1 == 2:
        if var4 == 2:
            print('Your friend appreciates the complements.')
            time.sleep(2)
            friend1()
        if var4 == 1:
            print('Your friend looks busy right now.')
            time.sleep(2)
            friend1()
        if var4 == 0:
            print('\nYou tell your friend he has nice eyes.')
            time.sleep(3)
            print('He seems happy.')
            time.sleep(2)
            friendflagger1.friendFlagger1()

    if friendSelect1 == 3:
        print('Placeholder3')
        time.sleep(0.5)
        friend1()

    if friendSelect1 == 4:
        if var4 <= 1:
            print('\nYou walk back without talking...how rude.')
            time.sleep(2)
            friendflagger2.friendFlagger2()
        if var4 == 2:
            print('\nYou walk back, your friend still blushing.')
            time.sleep(2)
            mm2.mainMenu2()
