import os
import time
import configparser
import mm2

def ch1End():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print("You didn't notice it at first, but alongside a strange noise, you see a black disc in the sky.\n")
    print('LOOK [1]')

    ch1EndSelect = int(input('\nACTION >> '))

    while ch1EndSelect < 1 or ch1EndSelect > 1:
        ch1End()

    if ch1EndSelect == 1:
        print('\nThe black disc descends from the sky, and lands safely. A hatch opens, and your friends walk out.')
        time.sleep(5)
        os.system('clear')
        print('\nCHAPTER I COMPLETE!\n')
        time.sleep(2)
        os.system('clear')
        print('\nSaving...')
        config = configparser.ConfigParser() #Move to seperate function
        config['ch2flagger'] = {'var2': '1'}
        with open('save/config2.ini', 'w') as configfile:
                config.write(configfile)
        time.sleep(0.5)
        print('Saved.')
        time.sleep(1)
        mm2.mainMenu2()
