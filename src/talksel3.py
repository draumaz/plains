import os
import time
import talk

def talkSel3():
        os.system('clear')
        print('\nThe Plains v0.16\n')
        print("talkSel3 PH.\n")
        print('OPT1 [1]')
        print('BACK [2]')

        talkSel3Select = int(input('\nACTION >> '))

        while talkSel3Select < 1 or talkSel3Select > 2:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talkSel1()

        if talkSel3Select == 1:
            print("\nOPT1.")
            time.sleep(5)
            talk.talk()

        if talkSel3Select == 2:
            print("\nBACK.")
            time.sleep(5)
            talk.talk()
