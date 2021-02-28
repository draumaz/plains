import os
import time
import configparser
import mm2

def emb2End():
    print('\nYou decide to depart anyways, and your journey comes to an end.')
    time.sleep(3)
    os.system('cls||clear')
    print('\n\nTHANK YOU SO MUCH FOR PLAYING!')
    time.sleep(4)
    config = configparser.ConfigParser()
    config['gameover'] = {'var14': '1'}
    with open('save/config14.ini', 'w') as configfile:
        config.write(configfile)
    quit()

def Embark2():
    print("\nSaan mentions how beautiful this planet is.")
    time.sleep(2)
    print("Seems like they all want to stick around for a bit.")
    time.sleep(2)
    print('\nLEAVE [1]')
    print('STAY [2]')

    while True:
        try:
            embSelect2 = int(input('\nACTION >> '))

            if embSelect2 == 1:
                emb2End()
            if embSelect2 == 2:
                print('\nYour friends have a point. You decide to stick around.')
                time.sleep(3)
                mm2.mainMenu2()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            Embark2()
