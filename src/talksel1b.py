import os
import time
import talksel1eg

def talkSel1B():
    print('\nYour friends ask you a question.')
    time.sleep(2)
    print('"Liam, is everything alright?"\n')
    time.sleep(2)
    print('EXPLAIN [1]')
    print('BACK [2]')

    talkSel1ESelect2 = int(input('\nACTION >> '))

    while talkSel1ESelect2 < 1 or talkSel1ESelect2 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        talkSel1B()

    if talkSel1ESelect2 == 1:
        print("\nYou explain to them that you're just feeling off.")
        time.sleep(3)
        print("\n:)")
        time.sleep(0.15)
        talksel1eg.talkSel1EG()

    if talkSel1ESelect2 == 2:
        print("\nThey wouldn't get it.")
        time.sleep(5)
        talk.talk()
