import os
import time
import mm2

def Embark2():
    print("\nSaan mentions how beautiful this planet is.")
    time.sleep(2)
    print("Seems like they all want to stick around for a bit.")
    time.sleep(2)
    print('\nLEAVE [1]')
    print('STAY [2]')

    embSelect2 = int(input('\nACTION >> '))

    while embSelect2 < 1 or embSelect2 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        Embark2()

    if embSelect2 == 1:
        print('\nYou decide to depart anyways, and your journey comes to an end.')
        time.sleep(3)
        os.system('cls||clear')
        print('\n\nTHANK YOU SO MUCH FOR PLAYING!')
        time.sleep(4)
        quit()

    if embSelect2 == 2:
        print('\nYour friends have a point. You decide to stick around.')
        time.sleep(3)
        mm2.mainMenu2()
