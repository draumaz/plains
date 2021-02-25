import os
import time
import hill

def hillSel3():
    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    print('You sit down in the grassy plains and look at the sky. It is absolutely gorgeous.')
    print('\nEXAMINE [1]')
    print('BACK [2]')

    while True:
        try:
            hillSel3Select = int(input('\nACTION >> '))

            while hillSel3Select < 1 or hillSel3Select > 2:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                hillSel3()

            if hillSel3Select == 1:
                print('\nLaying down on the grass, it makes you feel truly refreshed.')
                time.sleep(3)
                hill.hill()

            if hillSel3Select == 2:
                print('\nYou decide that you have more important things to be doing.')
                time.sleep(2)
                hill.hill()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            hillSel3()
