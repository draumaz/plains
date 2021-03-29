import os
import time
import textwrap
import handig
import lizard

def mainMenu3(): #WIP (main mm3)
    handig.screenClear()
    handig.versionHeader()
    handig.invDisplay()
    vars = handig.savePull()
    var6 = vars[5]
    print(textwrap.fill("You and your friends are walking through a field of yellow-red grass.", 75))
    print(textwrap.fill("There's so many strange things to see on this planet.", 75))
    print('\nOPT1 [1]')
    if var6 != 1:
        print('LIZARD [2]')
    print('OPT3 [3]')
    print('QUIT [4]')
    while True:
        try:
            choose = int(input('\nACTION >> '))
            if choose == 1:
                pass
            if choose == 2:
                lizard.Lizard()
            if choose == 3:
                pass
            if choose == 4:
                handig.quitHandler()
            if choose > 4 or choose < 0:
                handig.inpErrorHandler()
                mainMenu3()
        except ValueError:
            handig.inpErrorHandler()
            mainMenu3()

def mainMenu3W(): #Placeholder director
    handig.screenClear()
    line_ext = 13
    state_ext = 1
    handig.saveWriter(line_ext, state_ext)
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill("Thank you for playing! You've reached the end of this build - but much, much more is coming. Stay tuned!", 75))
    print('')
    print(textwrap.fill("Visit https://github.com/draumaz/plains to keep up with the game!", 75))
    print('')
    time.sleep(5)
    quit()