import os
import time
import talk
import saan
import embark

def mainMenu2():
    os.system('clear')
    print('\nThe Plains v0.17\n')
    print('A fancy, metallic ship lands a little ways from where you landed.')
    print('Your friends walk out, and approach you.\n')
    print('TALK [1]')
    print('SAAN [2]')
    print('EMBARK [3]')
    print('QUIT [4]')

    mainmenuSelect2 = int(input('\nACTION >> '))

    while mainmenuSelect2 < 1 or mainmenuSelect2 > 5:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        mainMenu2()

    if mainmenuSelect2 == 1:
        talk.talk()

    if mainmenuSelect2 == 2:
        saan.saan()

    if mainmenuSelect2 == 3:
        embark.Embark()

    if mainmenuSelect2 == 4:
        os.system('clear')
        print('\nThanks for playing!')
        time.sleep(0.5)
        quit()
