import os
import time
import hill

def hillSel3():
    os.system('clear')
    print('\nThe Plains v0.17\n')
    print('You sit down in the grassy plains and look at the sky. It is absolutely gorgeous.')
    print('\nEXAMINE [1]')
    print('BACK [2]')

    hillSel3Select = int(input('\nACTION >> '))

    while hillSel3Select < 1 or hillSel3Select > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        hillSel3()

    if hillSel3Select == 1:
        print('\nYou feel truly refreshed. Perhaps crashlanding might have been just what you needed...')
        time.sleep(2)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('Wonder why your team has yet to contact you...')
        time.sleep(3)
        hill.hill()

    if hillSel3Select == 2:
        print('\nYou decide that you have more important things to be doing.')
        time.sleep(2)
        hill.hill()
