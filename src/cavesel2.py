import os
import time
import tool
import cave

def caveSel2():
    os.system('clear')
    print('\nThe Plains v0.14\n')
    print("Up against the entrance is a sign. It's written in a strange, alien system.\n")
    print('DECIPHER [1]')
    print('BACK [2]')

    caveSelect2 = int(input('\nACTION >> '))
    while caveSelect2 < 1 or caveSelect2 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        caveSel2()

    if caveSelect2 == 1:
        print('\nYou pull out your phone, and attempt to translate the symbols.')
        time.sleep(4)
        print('...looks like it says "Abandon all hope, ye who enter here".')
        time.sleep(4)
        print('\nBetter safe than sorry.')
        time.sleep(2)
        cave.cave()

    if caveSelect2 == 0:
        print("\nToo much work, anyways.")
        time.sleep(2)
        cave.cave()
