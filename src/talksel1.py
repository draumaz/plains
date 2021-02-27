import os
import time
import talk
import talksel1b
import configparser
import textwrap

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
            print(textwrap.fill("\nYour friends mentioned that they heard your scanner signal, and knew to come find you.", 75))
            time.sleep(5)
            talk.talk()

        if var7 == 1 and var8 == 0:
            talksel1b.talkSel1B()

    if var3 == 0:

        if var7 == 0 or var8 == 1:
            os.system('cls||clear')
            print('\nThe Plains v0.19\n')
            print("Your friends ask you why you didn't use any of your tools to contact them.\n")
            print('UH... [1]')
            print('BACK [2]')

            while True:
                try:
                    talkSel1Select = int(input('\nACTION >> '))

                    while talkSel1Select < 1 or talkSel1Select > 2:
                        print('\nDid you mean something else?')
                        time.sleep(0.5)
                        talkSel1()

                    if talkSel1Select == 1:
                        print("\nYour friends tell you to not to worry about it.")
                        time.sleep(5)
                        talk.talk()

                    if talkSel1Select == 2:
                        print("\nYou pretend that you're getting a call on your phone to avoid this awkward conversation.")
                        time.sleep(5)
                        talk.talk()
                except ValueError:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    talkSel1()

        if var7 == 1 and var8 == 0:
            talksel1b.talkSel1B()
