import os
import time
import tool
import cave

def caveSel3():
    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    print("You focus your listening on the cave. You can hear a faint rumbling noise coming from within.\n")
    print('DISCERN [1]')
    print('BACK [2]')

    while True:
        try:
            caveSelect3 = int(input('\nACTION >> '))

            while caveSelect3 < 1 or caveSelect3 > 2:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                caveSel3()

            if caveSelect3 == 1:
                print('\nYou listen as hard as you can, in an attempt to discern words.')
                time.sleep(4)
                print("...that's certainly not any language you know.")
                time.sleep(2)
                cave.cave()

            if caveSelect3 == 2:
                print("\nYou figure that the rumbling is probably just natural noises.")
                time.sleep(2)
                cave.cave()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            caveSel3()
