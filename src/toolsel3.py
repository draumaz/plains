import os
import time
import tool
import toolflagger

def toolSel3():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('Looks like your scanner is functioning just fine.\n')
    print('SIGNAL [1]')
    print('BACK [2]')

    toolSelect3 = int(input('\nACTION >> '))

    while toolSelect3 < 1 or toolSelect3 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        toolSel3()

    if toolSelect3 == 1:
        print('\nYou try to send out a signal, and it looks like it was received!\n')
        time.sleep(4)
        toolflagger.toolFlagger()

    if toolSelect3 == 2:
        print("\nProbably wouldn't work, anyway.")
        time.sleep(2)
        tool.tool()
