import os
import time
import mm2
import talksel1
import talksel2
import talksel3
import talksel1e
import configparser

def talk():
    os.system('clear')

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')

    print('\nThe Plains v0.16\n')
    if var6 == 0:
        if var7 == 0:
            print("Your friends seem relieved that you're alright.\n")
    if var6 == 1:
        #if var7 == 0:
            #print('Your friends look at you with horrified expressions.\n')
        #if var7 == 1:
        print('Your friends look at you with horrified expressions.\n')
    if var7 == 1:
        if var6 == 0:
            print('Your friends seem worried.\n')
    if var6 == 0:
        print('TALK TO FRIENDS [1]')
    if var6 == 1:
        print("WHAT'S WITH THAT LOOK? [1]")
    #print('TALK ABOUT LOCATION [2]')
    #print('TALK ABOUT PH [3]')
    print('BACK [4]')

    talkSelect = int(input('\nACTION >> '))

    while talkSelect < 1 or talkSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        talk()

    if talkSelect == 1:
        if var6 == 0:
            talksel1.talkSel1()
        if var6 == 1:
            talksel1e.talkSel1E()

    if talkSelect == 2:
        talk()
        #talksel2.talkSel2()

    if talkSelect == 3:
        talk()
        #talksel3.talkSel3()

    if talkSelect == 4:
        print('\nYou tell your friends you need a minute.')
        time.sleep(2)
        mm2.mainMenu2()
