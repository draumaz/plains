import os
import time
import mm2

def ch1End():
    os.system('clear')
    print('\nThe Plains v0.13\n')
    print("You didn't notice it at first, but alongside a strange noise, you see a black disk in the sky.\n")
    print('LOOK [1]')
    
    ch1EndSelect = int(input('\nACTION >> '))
    while ch1EndSelect < 1 or ch1EndSelect > 1:
        ch1End()

    if ch1EndSelect == 1:
        print('The black disc descends from the sky, and lands safely. A hatch opens, and your friends walk out.')
        time.sleep(5)
        os.system('clear')
        print('\nCHAPTER I COMPLETE!\n')
        time.sleep(2)
        os.system('clear')
        print('\nSaving...')
        fname = "config3.py"
        data = 1
        with open(fname, 'w') as f:
            f.write('var3 = {}'.format(data))
            f.close()
        print('Saved.')
        time.sleep(1)
        os.system('clear')
        mm2.mainMenu2()
