import os
import time
import mm1
from hillsel1 import *
from hillsel2 import *
from hillsel3 import *

def hill():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('That hill looks pretty strange. It juts out of the landscape in an unrealistic way.\n')
    print('GO TOWARDS [1]')
    print('STAND STILL [2]')
    print('LOOK AT THE SKY [3]')
    print('BACK [4]')
    hillSelect = int(input('\nACTION >> '))
    while hillSelect < 1 or hillSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
    if hillSelect == 1:
        hillSel1()
    if hillSelect == 2:
        hillSel2()
    if hillSelect == 3:
        hillSel3()
    if hillSelect == 4:
        mm1.mainMenu1()
