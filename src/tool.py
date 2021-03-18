import os
import time
import mm1
import textwrap
import configparser
import inventory

def toolEx():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')

    if var3 == 0:
        print('')
        print(textwrap.fill("You decide that checking your tools isn't worth your time or effort.", 75))
        time.sleep(3)
        mm1.mainMenu1()
    if var3 == 1:
        print('')
        print("With your friends contacted, you decide to head back.")
        time.sleep(2)
        print(textwrap.fill("Seems like a good time to stand in front of a hill for a while.", 75))
        time.sleep(4)
        print(";)")
        time.sleep(0.05)
        mm1.mainMenu1()

def tool():
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print(textwrap.fill('Seeming to be completely stranded, you decide to use the tools at your disposal.\n', 75))
    print('\nPHONE [1]')
    print('RADAR [2]')
    print('SCANNER [3]')
    print('BACK [4]')

    while True:
        try:
            toolSelect = int(input('\nACTION >> '))

            if toolSelect == 1:
                toolSel1()
            if toolSelect == 2:
                toolSel2()
            if toolSelect == 3:
                toolSel3()
            if toolSelect == 4:
                toolEx()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            tool()

def toolSel1():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print('You pull out your phone. Unsurprisingly, the signal is rather weak.\n')
    print('MESSAGE A FRIEND [1]')
    print('BACK [2]')

    while True:
        try:
            toolSelect1 = int(input('\nACTION >> '))

            if toolSelect1 == 1:
                if var3 == 0:
                    print("\nThe message won't even go through...")
                    time.sleep(4)
                    toolFlagger()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if toolSelect1 == 2:
                if var3 == 0:
                    print("\nWhat good's a phone without service?")
                    time.sleep(3)
                    tool()
                if var3 == 1:
                    tool()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            toolSel1()

def toolSel2():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print('Using your radar, you can attempt to establish contact.\n')
    print('SCAN [1]')
    print('BACK [2]')

    while True:
        try:
            toolSelect2 = int(input('\nACTION >> '))

            if toolSelect2 == 1:
                if var3 == 0:
                    print('\nYou try establishing contact...your radar just shuts off.')
                    time.sleep(4)
                    toolFlagger()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if toolSelect2 == 2:
                if var3 == 0:
                    print("\nProbably wouldn't work, anyway.")
                    time.sleep(2)
                    tool()
                if var3 == 1:
                    tool()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            toolSel2()

def toolSel3():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print('Looks like your scanner is functioning just fine.\n')
    print('SIGNAL [1]')
    print('BACK [2]')

    while True:
        try:
            toolSelect3 = int(input('\nACTION >> '))

            if toolSelect3 == 1:
                if var3 == 0:
                    print('\nYou try to send out a signal, and it looks like it was received!\n')
                    time.sleep(4)
                    toolFlagger()
                if var3 == 1:
                    print("\nYou've already made contact.")
                    time.sleep(2)
                    tool()
            if toolSelect3 == 2:
                if var3 == 0:
                    print("\nProbably wouldn't work, anyway.")
                    time.sleep(2)
                    tool()
                if var3 == 1:
                    tool()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            toolSel3()

def toolFlagger():
	config = configparser.ConfigParser()
	config['toolflag'] = {'var3': '1'}
	with open('save/config3.ini', 'w') as configfile:
		config.write(configfile)
	tool()
