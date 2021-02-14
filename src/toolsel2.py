import os
import time
import tool
import toolflagger

def toolSel2():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('Using your radar, you can attempt to establish contact.\n')
    print('SCAN [1]')
    print('BACK [2]')

    toolSelect2 = int(input('\nACTION >> '))
    while toolSelect2 < 1 or toolSelect2 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        toolSel2()

    if toolSelect2 == 1:
        print('\nYou try establishing contact...your radar just shuts off.')
        time.sleep(4)
        toolflagger.toolFlagger()
    if toolSelect2 == 2:
        print("\nProbably wouldn't work, anyway.")
        time.sleep(2)
        tool.tool()
