import mm3
import mm2
import mm1
import time
import os
import handig
import configparser

def devJump():
    os.system('cls||clear')
    print('\nDevelopment Hopper\n')
    print('CHAPTER 1 [1]')
    print('CHAPTER 2 [2]')
    print('CHAPTER 3 [3]')
    print('\nPROD RESET [4]')
    print('')
    print('BAD END FLAG [5]')
    print('TOOLS USED FLAG [6]')
    print('KILLED LIZARD FLAG [7]')
    print('SPLASH OFF [8]')
    print('SPLASH ON [9]')
    print('FLOWER [10]')
    print('\nEXIT [11]')

    while True:
        try:
            devSelect = int(input('\nACTION >> '))

            if devSelect == 1: #Chapter 1 Jump
                mm1.mainMenu1()
            if devSelect == 2: #Chapter 2 Jump
                line_ext = 0
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                line_ext = 0
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                mm2.mainMenu2()
            if devSelect == 3: #Chapter 3 Jump
                line_ext = 0
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                line_ext = 1
                state_ext = 2
                handig.saveWriter(line_ext, state_ext)
                mm3.mainMenu3()
            if devSelect == 4: #Full Reset
                save = open('data.txt', 'w+')
                save.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
                save.close()
                devJump()
            if devSelect == 5: #Bad Ending
                line_ext = 8
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                line_ext = 0
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                line_ext = 1
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                devJump()
            if devSelect == 6: #Tools used flag
                line_ext = 2
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                devJump()
            if devSelect == 7: #Lizard murder flag
                line_ext = 5
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                line_ext = 6
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                devJump()
            if devSelect == 8:
                line_ext = 10
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
                devJump()
            if devSelect == 9:
                line_ext = 10
                state_ext = 0
                handig.saveWriter(line_ext, state_ext)
                devJump()
            if devSelect == 10:
                line_ext = 15
                state_ext = 1
                handig.saveWriter(line_ext, state_ext)
            if devSelect == 11:
                os.system('cls||clear')
                quit()
        except ValueError:
            devJump()

devJump()
