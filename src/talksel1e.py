import os
import time
import talk
import configparser
import talksel1eg

def talkSel1E():
    config = configparser.ConfigParser()
    config.read('save/config5.ini')
    var5 = config.getint('reset', 'var5')

    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('clear')
    print('\nThe Plains v0.16\n')

    if var6 == 1:
        print('Your friends barely stammer out a question.')
        time.sleep(2)
        print('"Liam, why are you covered in blood?"\n')
        time.sleep(2)
        print('EXPLAIN [1]')

        talkSel1ESelect = int(input('\nACTION >> '))

        while talkSel1ESelect < 1 or talkSel1ESelect > 1:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talkSel1E()
            
        print('\nYou explain to your friends that it was self-defense.')
        time.sleep(2)
        print('They understand, and help you clean off.')
        time.sleep(2)
        talksel1eg.talkSel1EG()

    if var6 == 0:
        talk.talk()
