import os
import time
import textwrap
import handig

def mainMenu3(): #WIP (main mm3)
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill("You and your friends are walking through a field of yellow-red grass.", 75))
    print(textwrap.fill("There's so many strange things to see on this planet.", 75))
    print('\nOPT1 [1]')
    print('OPT2 [2]')
    print('OPT3 [3]')
    print('QUIT [4]')
    while True:
        try:
            mainmenuSelect2 = int(input('\nACTION >> '))
            if mainmenuSelect2 == 1:
                pass
            if mainmenuSelect2 == 2:
                pass
            if mainmenuSelect2 == 3:
                pass
            if mainmenuSelect2 == 4:
                handig.quitHandler()
            if mainmenuSelect2 > 4 or mainmenuSelect2 < 0:
                handig.inpErrorHandler()
                mainMenu3()
        except ValueError:
            handig.inpErrorHandler()
            mainMenu3()

def mainMenu3P(): #Placeholder director
    os.system('cls||clear')
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