import os
import time
import configparser
import reset
import textwrap

def mainAlt():
    os.system('cls||clear')
    print('\n...')
    time.sleep(5)
    print("\nWhat you did...it's inexcusable.")
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

            while altSel < 1 or altSel > 2:
                mainAlt2()

            if altSel == 1:
                print('\nSo you regret what you have done.')
                time.sleep(2)
                print('Do you really think this changes anything?')
                time.sleep(2)
                print("You're a murderer.")
                time.sleep(2)
                print(textwrap.fill("You have the ability to reset this world, over and over again..", 75))
                time.sleep(3)
                print("Does that make you feel good?")
                time.sleep(4)
                print("The ability to hurt others, without recourse?")
                time.sleep(4)
                print("Just because it's a video game.")
                time.sleep(4)
                os.system('cls||clear')
                time.sleep(2)
                print('\nYou still have the chance to make things right.')
                time.sleep(2)
                print('Please, do the right thing.')
                config = configparser.ConfigParser()
                config['badend'] = {'var9': '0'}
                with open('save/config9.ini', 'w') as configfile:
                       config.write(configfile)
                time.sleep(2)
                reset.resetter()

            if altSel == 2:
                if var10 == 1:
                    time.sleep(0.75)
                    print('\nError.')
                    time.sleep(0.5)
                    mainAlt2()
                if var10 == 0:
                    print('\nIs that so.')
                    time.sleep(2)
                    print("Here's your chance.")
                    time.sleep(1)
                    reset.resetter()
        except ValueError:
            mainAlt2()
        except KeyboardInterrupt:
            mainAlt2()
