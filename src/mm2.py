import os
import time
import talk

def mainMenu2():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print('A fancy, metallic ship lands a little ways from where you landed.')
    print('Your friends walk out, and approach you.\n')
    print('TALK [1]')
    print('FRIEND1 [2]')
    print('FRIEND2 [3]')
    print('QUIT [4]')

    mainmenuSelect2 = int(input('\nACTION >> '))

    if mainmenuSelect2 == 1:
        talk.talk()

    if mainmenuSelect2 == 2:
        mainMenu2()

    if mainmenuSelect2 == 3:
        mainMenu2()

    if mainmenuSelect2 == 4:
        os.system('clear')
        print('\nThanks for playing!')
        time.sleep(0.5)
        quit()
