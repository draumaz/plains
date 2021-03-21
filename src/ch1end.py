import os
import time
import mm2
import textwrap
import handig

def ch1End():
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
    print(textwrap.fill("You didn't notice it at first, but alongside a strange noise, you see a black disc in the sky.\n", 75))
    print('\nLOOK [1]')
    while True:
        try:
            ch1EndSelect = int(input('\nACTION >> '))
            if ch1EndSelect == 1:
                line_ext = 1
                state_ext = '1\n'
                handig.saveWriter(line_ext, state_ext)
                print('')
                print(textwrap.fill('The spacecraft descends from the sky, and lands safely. A hatch opens, and your friends walk out.', 75))
                time.sleep(5)
                mm2.mainMenu2()
            if ch1EndSelect > 1 or ch1EndSelect < 0:
                ch1End()
        except ValueError:
            ch1End()
