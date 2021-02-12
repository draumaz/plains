import os
import time
import mm1
import tool

def toolSel1():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('You pull out your phone. Unsurprisingly, the signal is rather weak.\n')
    print('MESSAGE A FRIEND [1]')
    print('BACK [2]')

    toolSelect1 = int(input('\nACTION >> '))
    while toolSelect1 < 1 or toolSelect > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        toolSel1()

    if toolSelect1 == 1:
        print('Test')
    if toolSelect1 == 0:
        print('What good is a phone without service?')
        time.sleep(3)
        tool.tool()
