import os
import time
import mm2
import configparser

def Embark():

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    os.system('clear')
    print('\nThe Plains v0.17\n')
    if var6 == 1 and var8 == 0:
        print('Ignoring your friends, you make your way to their spaceship and sit inside.')
        time.sleep(3)
    if var6 == 0 or var8 == 1:
        print("You walk to your friends' ship. They soon join you.")
    print('\nACTION1 [1]')
    print('SET OFF [2]')
    print('ACTION3 [3]')

    embSelect = int(input('\nACTION >> '))

    while embSelect < 1 or embSelect > 3:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        Embark()

    if embSelect == 2:
        if var6 == 1 and var8 == 0:
            print('\nBlood still dripping from your clothes, you take off, leaving your friends behind.')
            time.sleep(6)
            os.system('clear')
            time.sleep(3)
            print('E')
            time.sleep(0.25)
            print('E')
            time.sleep(0.25)
            print('EEEEEEEEEE')
            config = configparser.ConfigParser()
            config['badend'] = {'var9': '1'}
            with open('save/config9.ini', 'w') as configfile:
                   config.write(configfile)
            time.sleep(2)
            quit()
        else:
            print('\nYou and your friends lift off from the ground, and fly away.')
            time.sleep(4)
            quit()
