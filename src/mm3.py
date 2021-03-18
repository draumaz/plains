import os
import time
import textwrap
import configparser
import inventory

def mainMenu3(): #Placeholder director
    os.system('cls||clear')
    config = configparser.ConfigParser()
    config['gameover'] = {'var14': '1'}
    with open('save/config14.ini', 'w') as configfile:
        config.write(configfile)
    print('\nThe Plains v0.21\n')
    inventory.invDisplay()
    print(textwrap.fill("Thank you for playing! You've reached the end of this build - but much, much more is coming. Stay tuned!", 75))
    print('')
    print(textwrap.fill("Visit https://github.com/draumaz/plains to keep up with the game!", 75))
    print('')
    time.sleep(5)
    quit()

def mainMenu3R(): #WIP (main mm3)
    os.system('cls||clear')
    print('\nThe Plains v0.21\n')
    print('Placeholder\n')
    print('OPT1 [1]')
    print('OPT2 [2]')
    print('OPT3 [3]')
    print('OPT4 [4]')
    while True:
        try:
            mainmenuSelect2 = int(input('\nACTION >> '))
            #if mainmenuSelect2 == 1:
            #    opt1()
            #if mainmenuSelect2 == 2:
            #    opt2()
            #if mainmenuSelect2 == 3:
            #    opt3()
            #if mainmenuSelect2 == 4:
            #    quit()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            mainMenu3()
