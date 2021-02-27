import os
import time
import talk
import textwrap

def talkSel2():
        os.system('cls||clear')
        print('\nThe Plains v0.19\n')
        print("You just...stare at them. They look bewildered.\n")
        print('KEEP STARING [1]')
        print('GO BACK [2]')

        while True:
            try:
                talkSel2Select = int(input('\nACTION >> '))

                if talkSel2Select == 1:
                    print('')
                    print(textwrap.fill("Your unblinking eyes eventually cause them to wonder if there's something seriously wrong with you.", 75))
                    time.sleep(5)
                    talk.talk()
                if talkSel2Select == 2:
                    print("\nYeah, this is pretty bizarre.")
                    time.sleep(5)
                    talk.talk()

            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                talkSel2()
