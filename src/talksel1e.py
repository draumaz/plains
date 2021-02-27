import os
import time
import talk
import configparser
import mm2
import talksel1eg

def talkSel1E():
    config = configparser.ConfigParser()
    config.read('save/config5.ini')
    var5 = config.getint('reset', 'var5')

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('cls||clear')
    print('\nThe Plains v0.19\n')

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

                while talkSel1ESelect < 1 or talkSel1ESelect > 2:
                    print('\nDid you mean something else?')
                    time.sleep(0.5)
                    talkSel1E()
                if talkSel1ESelect == 1:
                    print('\nYou explain to your friends that it was self-defense.')
                    time.sleep(2)
                    print('They understand, and help you clean off.')
                    time.sleep(2)
                    print('They seriously bought that?')
                    time.sleep(0.5)
                    talksel1eg.talkSel1EG()
                if talkSel1ESelect == 2:
                    print("\nYou can't face them.")
                    time.sleep(2)
                    mm2.mainMenu2()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel1E()

    if var6 == 0:
        talk.talk()
