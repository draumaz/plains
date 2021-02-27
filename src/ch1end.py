import os
import time
import ch1endb
import textwrap

def ch1End():
    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print(textwrap.fill("You didn't notice it at first, but alongside a strange noise, you see a black disc in the sky.\n", 75))
    print('\nLOOK [1]')

    while True:
        try:
            ch1EndSelect = int(input('\nACTION >> '))

            while ch1EndSelect < 1 or ch1EndSelect > 1:
                ch1End()

            if ch1EndSelect == 1:
                print('')
                print(textwrap.fill('The black disc descends from the sky, and lands safely. A hatch opens, and your friends walk out.', 75))
                time.sleep(5)
                os.system('cls||clear')
                print('\nCHAPTER I COMPLETE!\n')
                time.sleep(2)
                os.system('cls||clear')
                print('\nSaving...')
                ch1endb.ch1EndB()
        except ValueError:
            ch1End()
