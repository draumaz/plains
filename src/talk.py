import os
import time
import mm2
import talksel1
import talksel2
import talksel3

def talk():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('Your friends seem to be excited to talk to you.\n')
    print('TALK ABOUT TOOLS [1]')
    print('TALK ABOUT LOCATION [2]')
    print('TALK ABOUT PH [3]')
    print('BACK [4]')

    talkSelect = int(input('\nACTION >> '))

    while talkSelect < 1 or talkSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        talk()

    if talkSelect == 1:
        talksel1.talkSel1()

    if talkSelect == 2:
        talksel2.talkSel2()

    if talkSelect == 3:
        talksel3.talkSel3()

    if talkSelect == 4:
        print('\nYou tell your friends you need a minute.')
        time.sleep(2)
        mm2.mainMenu2()