import os
import time
import ch1endb

def ch1End():
    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    print("You didn't notice it at first, but alongside a strange noise, you see a black disc in the sky.\n")
    print('LOOK [1]')

    ch1EndSelect = int(input('\nACTION >> '))

    while ch1EndSelect < 1 or ch1EndSelect > 1:
        ch1End()

    if ch1EndSelect == 1:
        print('\nThe black disc descends from the sky, and lands safely. A hatch opens, and your friends walk out.')
        time.sleep(5)
        os.system('cls||clear')
        print('\nCHAPTER I COMPLETE!\n')
        time.sleep(2)
        os.system('cls||clear')
        print('\nSaving...')
        ch1endb.ch1EndB()
