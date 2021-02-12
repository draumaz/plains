import os
import time
import mm1
from cavesel1 import *
from cavesel2 import *
from cavesel3 import *

def cave():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('You make your way towards a deep, dark cave. You can barely see anything past the entrance.\n')
    print('CONTINUE [1]')
    print('LOOK AROUND [2]')
    print('LISTEN [3]')
    print('BACK [4]')
    caveSelect = int(input('\nACTION >> '))
    while caveSelect < 1 or caveSelect > 4:
        print('Did you mean something else?')
        time.sleep(0.5)
        cave()
    if caveSelect == 1:
        caveSel1()
    if caveSelect == 2:
        caveSel2()
    if caveSelect == 3:
        caveSel3()
    if caveSelect == 4:
        print('Seems pretty forboding...best to head back.')
        time.sleep(3)
        mm1.mainMenu1()
