import os
import time
import talk
import saan
import embark
import configparser
import handig

def mainMenu2():
    save = handig.savePull()
    var1 = save[0]
    var6 = save[5]
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
    print('A fancy, metallic ship lands a little ways from where you landed.')
    if var6 == 0:
        print('Your friends walk out, and approach you.\n')
    if var6 == 1:
        print('Your friends seem like they want to keep their distance.\n')
    print('TALK [1]')
    print('SAAN [2]')
    print('EMBARK [3]')
    print('QUIT [4]')

    while True:
        try:
            mainmenuSelect2 = int(input('\nACTION >> '))

            if mainmenuSelect2 == 1:
                talk.talk()
            if mainmenuSelect2 == 2:
                saan.saan()
            if mainmenuSelect2 == 3:
                embark.Embark()
            if mainmenuSelect2 == 4:
                handig.quitHandler()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu2()
