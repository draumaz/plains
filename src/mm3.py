import os
import time
import textwrap

def mainMenu3():
    os.system('cls||clear')
    print('\n')
    print(textwrap.fill("Thank you for playing! You've reached the end of this build - but much, much more is coming. Stay tuned!", 75))
    print('')
    print(textwrap.fill("Visit https://github.com/draumaz/plains to keep up with the game!", 75))
    time.sleep(5)
    quit()


def mainMenu3R():
    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print('Placeholder\n')
    print('OPT1 [1]')
    print('OPT2 [2]')
    print('OPT3 [3]')
    while True:
        try:
            mainmenuSelect2 = int(input('\nACTION >> '))
            
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu3()