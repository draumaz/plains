import os
import time
import mm2
import configparser
import textwrap
import inventory

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
    inventory.invDisplay()
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
    print('BACK [3]')

    while True:
        try:
            talkSelect = int(input('\nACTION >> '))
            if talkSelect == 1:
                if var6 == 1 and var8 == 0:
                    talkSel1E()
                else:
                    talkSel1()
            if talkSelect == 2:
                talkSel2()
            if talkSelect == 3:
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

def talkSel1a():
    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')
    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    if var7 == 0 or var8 == 1:
        os.system('cls||clear')
        inventory.invDisplay()
        print("Your friends ask you why you didn't use any of your tools to contact them.\n")
        print('UH... [1]')
        print('BACK [2]')
        while True:
            try:
                talkSel1Select = int(input('\nACTION >> '))
                if talkSel1Select == 1:
                    print("\nYour friends tell you to not to worry about it.")
                    time.sleep(2)
                    talk()
                if talkSel1Select == 2:
                    print("\nYou pretend that you're getting a call on your phone to avoid this awkward conversation.")
                    time.sleep(5)
                    talk()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel1()
    if var7 == 1 and var8 == 0:
        talkSel1B()

def talkSel1B():
    print('\nYour friends ask you a question.')
    time.sleep(2)
    print('"Liam, is everything alright?"\n')
    time.sleep(2)
    print('EXPLAIN [1]')
    print('BACK [2]')
    while True:
        try:
            talkSel1ESelect2 = int(input('\nACTION >> '))
            if talkSel1ESelect2 == 1:
                print("\nYou explain to them that you're just feeling off.")
                time.sleep(3)
                print("\n:)")
                time.sleep(0.10)
                talkSel1EG()
            if talkSel1ESelect2 == 2:
                print("\nThey wouldn't get it.")
                time.sleep(5)
                talk()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talkSel1B()

def talkSel1E():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('cls||clear')
    inventory.invDisplay()
    if var6 == 1:
        print('Your friends barely stammer out a question.')
        time.sleep(2)
        print('"Liam, why are you covered in blood?"\n')
        time.sleep(2)
        print('EXPLAIN [1]')
        print('RUN AWAY [2]')
        while True:
            try:
                talkSel1ESelect = int(input('\nACTION >> '))
                if talkSel1ESelect == 1:
                    print('\nYou explain to your friends that it was self-defense.')
                    time.sleep(2)
                    print('They understand, and help you clean off.')
                    time.sleep(2)
                    print('They seriously bought that?')
                    time.sleep(0.5)
                    talkSel1EG()
                if talkSel1ESelect == 2:
                    print("\nYou can't face them.")
                    time.sleep(2)
                    mm2.mainMenu2()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel1E()
    if var6 == 0:
        talk()

def talkSel1EG():
    config = configparser.ConfigParser()
    config['okay'] = {'var8': '1'}
    with open('save/config8.ini', 'w') as configfile:
        config.write(configfile)
    talk()

def talkSel1():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')
    config = configparser.ConfigParser()
    config.read('save/config7.ini')
    var7 = config.getint('lizardext', 'var7')
    config = configparser.ConfigParser()
    config.read('save/config8.ini')
    var8 = config.getint('okay', 'var8')

    if var3 == 1:
        if var7 == 0 or var8 == 1:
            print('')
            print(textwrap.fill("Your friends mentioned that they heard your scanner signal, and knew to come find you.", 75))
            time.sleep(5)
            talk()
        if var7 == 1 and var8 == 0:
            talkSel1B()
    if var3 == 0:
        talkSel1a()

def talkSel2():
        os.system('cls||clear')
        inventory.invDisplay()
        print("You just...stare at them. They look bewildered.\n")
        print('KEEP STARING [1]')
        print('GO BACK [2]')
        while True:
            try:
                talkSel2Select = int(input('\nACTION >> '))
                if talkSel2Select == 1:
                    print('')
                    print(textwrap.fill("Your unblinking eyes eventually cause them to wonder if there's something seriously wrong with you.", 75))
                    time.sleep(5)
                    talk()
                if talkSel2Select == 2:
                    print("\nYeah, this is pretty bizarre.")
                    time.sleep(1.5)
                    talk()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel2()

def talkSel3():
        os.system('cls||clear')
        inventory.invDisplay()
        print("talkSel3 PH.\n")
        print('OPT1 [1]')
        print('BACK [2]')
        while True:
            try:
                talkSel3Select = int(input('\nACTION >> '))
                if talkSel3Select == 1:
                    print("\nOPT1.")
                    time.sleep(5)
                    talk()
                if talkSel3Select == 2:
                    print("\nBACK.")
                    time.sleep(5)
                    talk()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel3()
