import os
import time
import textwrap
import scripts

def resetter():
    save = scripts.savePull()
    var9 = save[8]
    var10 = save[9]
    if var9 == 0:
        print('\nDoing this will reset everything. Are you sure?')
        print('\nRESET [1]')
        print('BACK [2]')
    if var9 == 1:
        print('\nRESET [1]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                if var9 == 1:
                    scripts.savePull()
                    print('\nReset failed.\n')
                    time.sleep(1)
                    if var10 == 0:
                        line_ext = 9
                        state_ext = 1
                        scripts.saveWriter()
                    quit()
                if var9 == 0:
                    normalReset()
                    return
            if choose == 2:
                if var9 == 1:
                    quit()
                if var9 == 0:
                    return
            if choose == 420:
                print('')
                scripts.easterEgg()
                resetter()
        except ValueError:
            scripts.inpErrorHandler()
            resetter()

def normalReset():
    line_ext = 0
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 1
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 2
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 3
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 4
    state_ext = 1
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 5
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 7
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 13
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 14
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    line_ext = 15
    state_ext = 0
    scripts.saveWriter(line_ext, state_ext)
    print('\nReset.')
    time.sleep(0.5)