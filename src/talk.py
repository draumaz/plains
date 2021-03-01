import os
import time
import mm2
import talksel1
import talksel2
import talksel3
import configparser

def talk():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')

    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')

    if var6 == 0 or var7 == 0 or var8 == 1: #Normal/post-explain
        print("Your friends are relieved that you're alright.\n")

    if var6 == 1 and var8 == 0: #Murder, pre-explain
        print('Your friends look at you with horrified expressions.\n')

    if var7 == 1 and var6 == 0 and var8 == 0: #Murdered before reset
            print('...they seem worried.\n')

    if var6 == 0 or var8 == 1: #Normal/post-explain
        print('CHIT-CHAT [1]')

    if var6 == 1 and var8 == 0 and var7 == 1: #Murder
        print("WHAT'S WITH THAT LOOK? [1]")

    print('STARE [2]')
    #print('TALK ABOUT PH [3]')
    print('BACK [4]')

    while True:
        try:
            talkSelect = int(input('\nACTION >> '))

            while talkSelect < 1 or talkSelect > 4:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talk()

            if talkSelect == 1:
                if var6 == 1 and var8 == 0:
                    talksel1.talkSel1E()
                else:
                    talksel1.talkSel1()

            if talkSelect == 2:
                talksel2.talkSel2()

            if talkSelect == 3:
                talk()
                #talksel3.talkSel3()

            if talkSelect == 4:
                if var6 == 1:
                    mm2.mainMenu2()
                if var6 == 0:
                    print('\nYou tell your friends you need a minute.')
                    time.sleep(2)
                    mm2.mainMenu2()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talk()
