import os
import time
import hill
import ch2flagger

def hillSel2():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print('Despite the massive mountain ahead of you, you decide to simply stand still.')
    time.sleep(2)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Seems like a bit of a waste of time.')
    time.sleep(4)
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
        print('\nStanding there motionless, it gives you the feeling that everythings going to be alright.\n')
        time.sleep(5)
        ch2flagger.ch2Flagger()
    if hillSel2Select == 2:
        print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
        time.sleep(5)
        hill.hill()
