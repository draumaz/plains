import os
import time
import mm1
import textwrap
import cavesel1
import cavesel2
import cavesel3

def cave():
    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    print(textwrap.fill('You make your way towards a deep, dark cave. You can barely see anything past the entrance.\n', 75))
    print('\nCONTINUE [1]')
    print('LOOK AROUND [2]')
    print('LISTEN [3]')
    print('BACK [4]')

    caveSelect = int(input('\nACTION >> '))

    while caveSelect < 1 or caveSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        cave()

    if caveSelect == 1:
        cavesel1.caveSel1()

    if caveSelect == 2:
        cavesel2.caveSel2()

    if caveSelect == 3:
        cavesel3.caveSel3()

    if caveSelect == 4:
        print('\nSeems pretty forboding...best to head back.')
        time.sleep(3)
        mm1.mainMenu1()
