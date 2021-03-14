import os
import time
import configparser
import reset
import textwrap

def mainAlt5():
    os.system('cls||clear')
    time.sleep(5)
    print('\nFATAL ERROR ENCOUNTERED')
    time.sleep(2)
    dest = open('plains.txt', 'w+')
    dest.write('EVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\n')
    dest.close()
    quit()


def mainAlt4():
    os.system('cls||clear')
    print('Will you?')
    print('\nYES [1]')
    print('NO [2]')
    while True:
        try:
            schl = int(input('\nACTION >> '))
            if schl == 1:
                config = configparser.ConfigParser()
                config['badend'] = {'var9': '0'}
                with open('save/config9.ini', 'w') as configfile:
                       config.write(configfile)
                config = configparser.ConfigParser()
                config['badendext'] = {'var10': '0'}
                with open('save/config10.ini', 'w') as configfile:
                    config.write(configfile)
                time.sleep(2)
                reset.resetter()
            if schl == 2:
                mainAlt5()
        except ValueError:
            mainAlt4()

def mainAlt3():
    print('\nSo you regret what you have done.')
    time.sleep(2)
    print('You know, that changes nothing.')
    time.sleep(2)
    print("You killed him.")
    time.sleep(2)
    print(textwrap.fill("Think about what that means. You downloaded a game, just to kill an innocent creature.", 75))
    time.sleep(3)
    print("Does that make you feel good?")
    time.sleep(4)
    print("The ability to hurt others, without recourse?")
    time.sleep(4)
    os.system('cls||clear')
    time.sleep(2)
    print('\nYou still have the chance to make things right.')
    time.sleep(2)
    print('You can go back there, and make things right.')
    time.sleep(2)
    mainAlt4()

def mainAlt():
    os.system('cls||clear')
    print('\n...')
    time.sleep(5)
    print("\nYou killed him.")
    time.sleep(3)
    os.system('cls||clear')
    print('\n...')
    time.sleep(2)
    mainAlt2()

def mainAlt2():

    config = configparser.ConfigParser()
    config.read('save/config10.ini')
    var10 = config.getint('badendext', 'var10')

    os.system('cls||clear')
    print("\nDo you regret it?")
    print('\nYES [1]')
    print('NO [2]')

    while True:
        try:
            altSel = int(input('\nACTION >> '))

            if altSel == 1:
                mainAlt3()
            if altSel == 2:
                if var10 == 1:
                    time.sleep(0.75)
                    print('\nError.')
                    time.sleep(0.5)
                    mainAlt2()
                if var10 == 0:
                    print("You're proud of it.")
                    time.sleep(2)
                    print("Here's your chance.")
                    time.sleep(1)
                    reset.resetter()

        except ValueError:
            mainAlt2()
        except KeyboardInterrupt:
            mainAlt2()
