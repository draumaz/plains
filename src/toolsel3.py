import os
import time
import tool

def toolSel3():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('Looks like your scanner is functioning just fine.\n')
    print('SIGNAL [1]')
    print('BACK [2]')

    toolSelect3 = int(input('\nACTION >> '))
    while toolSelect3 < 1 or toolSelect3 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        toolSel3()

    if toolSelect3 == 1:
        print('You try to send out a signal, and it looks like it was received!')
        fname = "config2.py"
        data = 1
        with open(fname, 'w') as f:
            f.write('var2 = {}'.format(data))
        time.sleep(4)
        tool.tool()
    if toolSelect3 == 2:
        print("Probably wouldn't work, anyway.")
        time.sleep(2)
        tool.tool()
