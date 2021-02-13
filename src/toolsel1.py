import os
import time
import tool

def toolSel1():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('You pull out your phone. Unsurprisingly, the signal is rather weak.\n')
    print('MESSAGE A FRIEND [1]')
    print('BACK [2]')

    toolSelect1 = int(input('\nACTION >> '))
    while toolSelect1 < 1 or toolSelect1 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        toolSel1()

    if toolSelect1 == 1:
        print("The message won't even go through...")
        fname = "config2.py"
        data = 1
        with open(fname, 'w') as f:
            f.write('var2 = {}'.format(data))
            f.close()
        time.sleep(4)
        tool.tool()
    if toolSelect1 == 0:
        print("What good's a phone without service?")
        time.sleep(3)
        tool.tool()
