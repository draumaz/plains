import os
import time
import tool

def toolSel2():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('Using your radar, you can attempt to establish contact.\n')
    print('SCAN [1]')
    print('BACK [2]')

    toolSelect2 = int(input('\nACTION >> '))
    while toolSelect2 < 1 or toolSelect2 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        toolSel2()

    if toolSelect2 == 1:
        print('You try establing contact...your radar just shuts off.')
        fname = "config2.py"
        data = 1
        with open(fname, 'w') as f:
            f.write('var2 = {}'.format(data))
        time.sleep(5)
        tool.tool()
    if toolSelect2 == 2:
        print("Probably wouldn't work, anyway.")
        time.sleep(2)
        tool.tool()
