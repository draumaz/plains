import os
import time
import talk
import saan
import embark
import scripts

def mainMenu2():
    save = scripts.savePull()
    var1 = save[0]
    var6 = save[5]
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
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
            choose = int(input('\nACTION >> '))
            if choose == 1:
                talk.talk()
            if choose == 2:
                saan.saan()
            if choose == 3:
                embark.Embark()
            if choose == 4:
                scripts.quitHandler()
            if choose > 4 or choose < 0:
                scripts.inpErrorHandler()
                mainMenu2()
        except ValueError:
            scripts.inpErrorHandler()
            mainMenu2()
