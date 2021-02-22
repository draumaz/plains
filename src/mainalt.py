import os
import time
import configparser
import reset

def mainAlt():
    os.system('clear')
    print('\n...')
    time.sleep(2)
    print("\nDo you regret your actions?")
    print('\nYES [1]')
    print('NO [2]')

    altSel = int(input('\nACTION >> '))

    while altSel < 1 or altSel > 2:
        print('\nThis is not an acceptable response.')
        time.sleep(2)
        mainAlt()

    if altSel == 1:
        print('\nSo you regret what you have done.')
        time.sleep(2)
        print('Do you really think this changes anything?')
        time.sleep(2)
        print("He's still dead.")
        time.sleep(2)
        print("Sure, you can reset. But I'm sure you can tell that they don't trust you.")
        time.sleep(5)
        os.system('clear')
        time.sleep(2)
        print('\nThere is one way we can make things right.')
        time.sleep(2)
        print('Please, do the right thing.')
        time.sleep(1)
        config = configparser.ConfigParser()
        config['badend'] = {'var9': '0'}
        with open('save/config9.ini', 'w') as configfile:
               config.write(configfile)
        time.sleep(2)
        reset.resetter()

    if altSel == 2:
        print('\nIs that so.')
        time.sleep(2)
        print('So be it.')
        time.sleep(2)
        quit()
