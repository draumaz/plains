import os
import time
import talk

def talkSel3():
        os.system('cls||clear')
        print('\nThe Plains v0.19\n')
        print("talkSel3 PH.\n")
        print('OPT1 [1]')
        print('BACK [2]')

        while True:
            try:
                talkSel3Select = int(input('\nACTION >> '))

                if talkSel3Select == 1:
                    print("\nOPT1.")
                    time.sleep(5)
                    talk.talk()
                if talkSel3Select == 2:
                    print("\nBACK.")
                    time.sleep(5)
                    talk.talk()
                    
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel3()
