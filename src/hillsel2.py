import os
import time
import hill
import standflagger
import configparser

def hillSel2():
    config = configparser.ConfigParser()
    config.read('save/config6.ini')
    var6 = config.getint('lizard', 'var6')

    os.system('clear')
    print('\nThe Plains v0.17\n')
    print('Despite the massive mountain ahead of you, you decide to simply stand still.')
    time.sleep(2)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    if var6 == 0:
        print('Seems like a bit of a waste of time.')
    if var6 == 1:
        print("You're wasting your time.")
    time.sleep(2)
    print('\nKEEP STANDING [1]')
    print('GO BACK [2]')

    hillSel2Select = int(input('\nACTION >> '))

    if hillSel2Select == 1:
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print("\nStanding there motionless, it gives you the feeling that everything's going to be alright.\n")
        time.sleep(5)
        standflagger.standFlagger()

    if hillSel2Select == 2:
        print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
        time.sleep(5)
        hill.hill()
