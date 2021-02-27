import os
import time
import mm1
import textwrap
import toolsel1
import toolsel2
import toolsel3
import configparser

def toolEx():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')

    if var3 == 0:
        print('')
        print(textwrap.fill("You decide that checking your tools isn't worth your time or effort.", 75))
        time.sleep(3)
        mm1.mainMenu1()
    if var3 == 1:
        print('')
        print("With your friends contacted, you decide to head back.")
        time.sleep(2)
        print(textwrap.fill("Seems like a good time to stand in front of a hill for a while.", 75))
        time.sleep(4)
        print(";)")
        time.sleep(0.05)
        mm1.mainMenu1()

def tool():
    os.system('cls||clear')
    print('\nThe Plains v0.19\n')
    print(textwrap.fill('Seeming to be completely stranded, you decide to use the tools at your disposal.\n', 75))
    print('\nPHONE [1]')
    print('RADAR [2]')
    print('SCANNER [3]')
    print('BACK [4]')
    
    while True:
        try:
            toolSelect = int(input('\nACTION >> '))

            if toolSelect == 1:
                toolsel1.toolSel1()
            if toolSelect == 2:
                toolsel2.toolSel2()
            if toolSelect == 3:
                toolsel3.toolSel3()
            if toolSelect == 4:
                toolEx()

        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            tool()
