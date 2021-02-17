import os
import time
import talk
import configparser

def talkSel1():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')

    if var3 == 1:
        print("\nYour friends mentioned that they heard your scanner signal, and knew to come find you.")
        time.sleep(5)
        talk.talk()
    if var3 == 0:
        os.system('clear')
        print('\nThe Plains v0.14\n')
        print("Your friends ask you why you didn't use any of your tools to contact them.\n")
        print('UH... [1]')
        print('BACK [2]')

        talkSel1Select = int(input('\nACTION >> '))

        while talkSel1Select < 1 or talkSel1Select > 2:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talkSel1()

        if talkSel1Select == 1:
            print("\nYour friends let you know not to worry about it, but to remember to do so next time.")
            time.sleep(5)
            talk.talk()

        if talkSel1Select == 2:
            print("\nYou pretend that you're getting a call on your phone to avoid this awkward conversation.")
            time.sleep(5)
            talk.talk()
