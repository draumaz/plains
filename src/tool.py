import os
import time
import mm1
import textwrap
import toolsel1
import toolsel2
import toolsel3


def tool():
    os.system('cls||clear')
    print('\nThe Plains v0.18\n')
    print(textwrap.fill('Seeming to be completely stranded, you decide to use the tools at your disposal.\n', 75))
    print('\nPHONE [1]')
    print('RADAR [2]')
    print('SCANNER [3]')
    print('BACK [4]')

    toolSelect = int(input('\nACTION >> '))

    while toolSelect < 1 or toolSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        tool()

    if toolSelect == 1:
        toolsel1.toolSel1()

    if toolSelect == 2:
        toolsel2.toolSel2()

    if toolSelect == 3:
        toolsel3.toolSel3()

    if toolSelect == 4:
        mm1.mainMenu1()
