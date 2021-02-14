import os
import time
import mm2
import talksel1

def talk():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('Your friends seem to be excited to talk to you.\n')
    print('TOOLS [1]')
    print('LOCATION [2]')
    print('PH [3]')
    print('BACK [4]')

    talkSelect = int(input('\nACTION >> '))

    while talkSelect < 1 or talkSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        talk()

    if talkSelect == 1:
        talksel1.talkSel1()

    if talkSelect == 2:
        print('\nPlaceholder talkSel2')
        time.sleep(2)
        talk()

    if talkSelect == 3:
        print('\nPlaceholder talkSel3')
        time.sleep(2)
        talk()
        
    if talkSelect == 4:
        print('\nYou tell your friends you need a minute.')
        time.sleep(2)
        mm2.mainMenu2()
