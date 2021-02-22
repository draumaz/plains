import os
import time
import configparser

def mainAlt():
    print('\n...')
    time.sleep(2)
    print("\nDo you regret your actions?")
    print('\nYES [1]')
    print('NO [2]')

    altSel = int(input('\nACTION >> '))

    while altSel < 1 or altSel > 2:
        print('\nThis is not an acceptable response.')
        time.sleep(2)
        mainAlt()

    if altSel == 1:
        print('\nSo you regret what you have done.')
        time.sleep(2)
        print('Does this change anything?')
    if altSel == 2:
        print('\nIs that so.')
        time.sleep(2)
        print('So be it.')
        time.sleep(2)
        quit()
