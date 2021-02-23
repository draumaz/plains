import os
import time
import mm1
import hillsel1
import hillsel2
import hillsel3
import configparser

def hill():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('clear')
    print('\nThe Plains v0.17\n')
    print('That hill looks pretty strange. It juts out of the landscape in an unrealistic way.')
    if var6 == 0:
        print('In the distance, you can see a creature moving about.\n')
        print('GO TOWARDS THE CREATURE [1]')
    if var6 == 1:
        print('')
        print('GO FORWARDS [1]')
    print('STAND STILL [2]')
    print('LOOK AT THE SKY [3]')
    print('BACK [4]')

    hillSelect = int(input('\nACTION >> '))

    while hillSelect < 1 or hillSelect > 4:
        print('\nDid you mean something else?')
        time.sleep(0.5)

    if hillSelect == 1:
        hillsel1.hillSel1()

    if hillSelect == 2:
        hillsel2.hillSel2()

    if hillSelect == 3:
        hillsel3.hillSel3()

    if hillSelect == 4:
        print('\nBest to head back.')
        time.sleep(2)
        mm1.mainMenu1()
