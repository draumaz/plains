import os
import time
import hill

def hillSel1():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('You walk towards the base of the mountain. You notice that the mountain seems to be moving!\n')
    print('FIGHT [1]')
    print('BACK [2]')

    hillSelect1 = int(input('\nACTION >> '))
    while hillSelect1 < 1 or hillSelect1 > 2:
        print('Did you mean something else?')
        time.sleep(0.5)
        hillSel1()

    if hillSelect1 == 1:
        print('\nYou attempt to fight the giant mountain beast, and die almost instantly.')
        time.sleep(2)
        print('Nice going, genius.')
        time.sleep(2)
        os.system('clear')
        print('\n==GAME OVER==\n')
        time.sleep(1)
        quit()

    if hillSelect1 == 2:
        print('\nUpon seeing that the mountain is alive and ready to strike, you decide to head back.\n')
        time.sleep(4)
        hill.hill()

    time.sleep(2)
    quit()
