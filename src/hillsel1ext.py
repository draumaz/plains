import os
import time
import hill
import lizardman
import mm1

def hillSel1Ext():
    os.system('clear')
    print('\nThe Plains v0.16\n')
    print('The huge reptilian sees you, and approaches.\n')
    print('KILL [1]')
    print('TALK [2]')
    print('BACK [3]')

    hillSel1ExtSel = int(input('\nACTION >> '))
    while hillSel1ExtSel < 1 or hillSel1ExtSel > 3:
        print('Did you mean something else?')
        time.sleep(0.5)
        hillSel1Ext()
    if hillSel1ExtSel == 1:
        print('\nWith one blow, you kill the lizard man.')
        time.sleep(5)
        lizardman.lizardMan()
    if hillSel1ExtSel == 2:
        print('PH TALK')
        time.sleep(5)
        hillSel1Ext()
    if hillSel1ExtSel == 3:
        print('\nUpon seeing the towering lizard, you decide to head back.')
        time.sleep(2)
        mm1.mainMenu1()
