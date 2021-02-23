import os
import time
import tool
import toolflagger
import configparser

def toolSel1():
    config = configparser.ConfigParser()
    config.read('save/config3.ini')
    var3 = config.getint('toolflag', 'var3')
    os.system('clear')
    print('\nThe Plains v0.17\n')
    print('You pull out your phone. Unsurprisingly, the signal is rather weak.\n')
    print('MESSAGE A FRIEND [1]')
    print('BACK [2]')

    toolSelect1 = int(input('\nACTION >> '))

    while toolSelect1 < 1 or toolSelect1 > 2:
        print('\nDid you mean something else?')
        time.sleep(0.5)
        toolSel1()

    if toolSelect1 == 1:
        if var3 == 0:
            print("\nThe message won't even go through...")
            time.sleep(4)
            toolflagger.toolFlagger()
        if var3 == 1:
            print("\nYou've already made contact.")
            time.sleep(2)
            tool.tool()

    if toolSelect1 == 2:
        if var3 == 0:
            print("\nWhat good's a phone without service?")
            time.sleep(3)
            tool.tool()
        if var3 == 1:
            tool.tool()
