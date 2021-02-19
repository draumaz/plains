import os
import time
import talk

def talkSel2():
        os.system('clear')
        print('\nThe Plains v0.15\n')
        print("talkSel2 PH.\n")
        print('OPT1 [1]')
        print('BACK [2]')

        talkSel2Select = int(input('\nACTION >> '))

        while talkSel2Select < 1 or talkSel2Select > 2:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            talkSel1()

        if talkSel2Select == 1:
            print("\nOPT1.")
            time.sleep(5)
            talk.talk()

        if talkSel2Select == 2:
            print("\nBACK.")
            time.sleep(5)
            talk.talk()
