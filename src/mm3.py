import os
import time
import textwrap
import scripts
import lizard
import river

def mainMenu3(): #WIP (main mm3)
    scripts.screenClear()
    scripts.versionHeader()
    scripts.invDisplay()
    vars = scripts.savePull()
    var6 = vars[5]
    print(textwrap.fill("You're all walking through a field of grass.", 75))
    print('Saan points out the river, and your other friends ', end='')
    if var6 == 1:
        print('notice the Placeholder')
        print('that something something something.')
    if var6 == 0:
        print("notice a reptilian")
        print("near the cave you were at.")
    print('\nPLACEHOLDER [1]')
    if var6 != 1:
        print('LIZARD [2]')
    if var6 == 1:
        print('DEAD LIZARD PLACEHOLDER [2]')
    print('RIVER [3]')
    print('QUIT [4]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                pass
            if choose == 2:
                if var6 == 0:
                    lizard.Lizard()
                if var6 == 1:
                    pass
            if choose == 3:
                river.riverMain()
            if choose == 4:
                scripts.quitHandler()
            if choose > 4 or choose < 0:
                scripts.inpErrorHandler()
                mainMenu3()
        except ValueError:
            scripts.inpErrorHandler()
            mainMenu3()

def mainMenu3W(): #Placeholder director
    scripts.screenClear()
    line_ext = 13
    state_ext = 1
    scripts.saveWriter(line_ext, state_ext)
    scripts.versionHeader()
    scripts.invDisplay()
    print(textwrap.fill("Thank you for playing! You've reached the end of this build - but much, much more is coming. Stay tuned!", 75))
    print('')
    print(textwrap.fill("Visit https://github.com/draumaz/plains to keep up with the game!", 75))
    print('')
    time.sleep(5)
    quit()