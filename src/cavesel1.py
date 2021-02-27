import os
import time
import tool
import cave

def caveSel1():
    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print("You continue deeper down the cave. It's getting pretty difficult to see...\n")
    print('CONTINUE [1]')
    print('BACK [2]')

    while True:
        try:
            caveSelect1 = int(input('\nACTION >> '))

            if caveSelect1 == 1:
                print('\nDespite the darkness, you keep walking, until you eventually hit a wall.')
                time.sleep(4)
                print('...pretty boring in here. You decide to head back.')
                time.sleep(4)
                cave.cave()

            if caveSelect1 == 2:
                print("\nContinuing in a cave this dark is just asking for trouble.")
                time.sleep(3)
                cave.cave()
                
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            caveSel1()
