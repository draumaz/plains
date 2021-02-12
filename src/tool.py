import os
import time
import mm1
from toolsel1 import *
from toolsel2 import *
from toolsel3 import *


def tool():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('Seeming to be completely stranded, you decide to use the tools at your disposal.\n')
    print('PHONE [1]')
    print('RADAR [2]')
    print('SCANNER [3]')
    print('BACK [4]')
    toolSelect = int(input('\nACTION >> '))
    while toolSelect < 1 or toolSelect > 4:
        print('Did you mean something else?')
        time.sleep(0.5)
        tool()
    if toolSelect == 1:
        toolSel1()
    if toolSelect == 2:
        toolSel2()
    if toolSelect == 3:
        toolSel3()
    if toolSelect == 4:
        mm1.mainMenu1()
