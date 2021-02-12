import os
import time
import hill
import config

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
    print('KEEP STANDING [1]')
    print('GO BACK [2]')
    
    hillSel2Select = int(input('\nACTION >> '))
    
    if hillSel2Select == 1:
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('Standing there motionless, it gives you the feeling that everythings going to be alright.\n')
        fname = 'config.py'
        data = 1
        with open(fname, 'w') as f:
            f.write('var1 = {}'.format(data))
        time.sleep(5)
        hill.hill()
    if hillSel2Select == 0:
        print('\nYou decide to stop being motionless, and return to a life full of motion.\n')
        time.sleep(5)
        hill.hill()
