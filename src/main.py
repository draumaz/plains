import os
import time
import configparser
from configparser import NoOptionError, NoSectionError
import mm1
import mm2
import mm3
import reset
import textwrap

def breakTest():
    while True:
        try:
            file = open('plains.txt', 'r')
            file.close()
            os.system('cls||clear')
            print('\nFATAL ERROR OCCURRED')
            reset.resetter()
            quit()
        except FileNotFoundError:
            fileTest()

def fileTest():
   while True:
       try:
            config = configparser.ConfigParser() #Verify config files are found and valid
            config.read('save/config.ini')
            var1 = config.getint('ch1endflag', 'var1')
            config = configparser.ConfigParser()
            config.read('save/config2.ini')
            var2 = config.getint('chaptflagger', 'var2')
            config = configparser.ConfigParser()
            config.read('save/config3.ini')
            var3 = config.getint('toolflag', 'var3')
            config = configparser.ConfigParser()
            config.read('save/config4.ini')
            var4 = config.getint('friendflag', 'var4')
            config = configparser.ConfigParser()
            config.read('save/config5.ini')
            var5 = config.getint('reset', 'var5')
            config = configparser.ConfigParser()
            config.read('save/config6.ini')
            var6 = config.getint('lizard', 'var6')
            config = configparser.ConfigParser()
            config.read('save/config7.ini')
            var7 = config.getint('lizardext', 'var7')
            config = configparser.ConfigParser()
            config.read('save/config8.ini')
            var8 = config.getint('okay', 'var8')
            config = configparser.ConfigParser()
            config.read('save/config9.ini')
            var9 = config.getint('badend', 'var9')
            config = configparser.ConfigParser()
            config.read('save/config10.ini')
            var10 = config.getint('badendext', 'var10')
            config = configparser.ConfigParser()
            config.read('save/config11.ini')
            var11 = config.getint('splashskip', 'var11')
            config = configparser.ConfigParser()
            config.read('save/config12.ini')
            var12 = config.getint('lizarddx', 'var12')
            config = configparser.ConfigParser()
            config.read('save/config13.ini')
            var13 = config.getint('splashskip2', 'var13')
            config = configparser.ConfigParser()
            config.read('save/config14.ini')
            var14 = config.getint('gameover', 'var14')
            config = configparser.ConfigParser()
            config.read('save/config15.ini')
            var15 = config.getint('blade', 'var15')
            config = configparser.ConfigParser()
            config.read('save/config16.ini')
            var16 = config.getint('flower', 'var16')
            splashScreen()
       except (NoOptionError, NoSectionError):
          saveDirGenerator()

def saveDirGenerator(): #Generate save sub-directory
    while True:
        try:
            os.mkdir('save')
            saveGenerator()
        except FileExistsError:
            saveGenerator()

def saveGenerator(): #Generate save files
    while True:
        try:
            save = open("save/config.ini", "w+")
            save.write('[ch1endflag]')
            save.write('\nvar1 = 0')
            save.close()
            save = open("save/config2.ini", "w+")
            save.write('[chaptflagger]')
            save.write('\nvar2 = 0')
            save.close()
            save = open("save/config3.ini", "w+")
            save.write('[toolflag]')
            save.write('\nvar3 = 0')
            save.close()
            save = open("save/config4.ini", "w+")
            save.write('[friendflag]')
            save.write('\nvar4 = 0')
            save.close()
            save = open("save/config5.ini", "w+")
            save.write('[reset]')
            save.write('\nvar5 = 0')
            save.close()
            save = open("save/config6.ini", "w+")
            save.write('[lizard]')
            save.write('\nvar6 = 0')
            save.close()
            save = open("save/config7.ini", "w+")
            save.write('[lizardext]')
            save.write('\nvar7 = 0')
            save.close()
            save = open("save/config8.ini", "w+")
            save.write('[okay]')
            save.write('\nvar8 = 0')
            save.close()
            save = open("save/config9.ini", "w+")
            save.write('[badend]')
            save.write('\nvar9 = 0')
            save.close()
            save = open("save/config10.ini", "w+")
            save.write('[badendext]')
            save.write('\nvar10 = 0')
            save.close()
            save = open("save/config11.ini", "w+")
            save.write('[splashskip]')
            save.write('\nvar11 = 0')
            save.close()
            save = open("save/config12.ini", "w+")
            save.write('[lizarddx]')
            save.write('\nvar12 = 0')
            save.close()
            save = open("save/config13.ini", "w+")
            save.write('[splashskip2]')
            save.write('\nvar13 = 0')
            save.close()
            save = open("save/config14.ini", "w+")
            save.write('[gameover]')
            save.write('\nvar14 = 0')
            save.close()
            save = open("save/config15.ini", "w+")
            save.write('[blade]')
            save.write('\nvar15 = 0')
            save.close()
            save = open("save/config16.ini", "w+")
            save.write('[flower]')
            save.write('\nvar16 = 0')
            save.close()
            fileTest()
        except FileExistsError:
            fileTest()

def splashScreen(): #Main menu
    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')
    config = configparser.ConfigParser()
    config.read('save/config10.ini')
    var10 = config.getint('badendext', 'var10')
    config = configparser.ConfigParser()
    config.read('save/config14.ini')
    var14 = config.getint('gameover', 'var14')

    if var10 == 1:
        mainAlt2()
    if var9 == 1:
        mainExt()
    if var9 == 0:
        os.system('cls||clear')
        print('\n==THE PLAINS==')
        print('==MADE BY DRAUMAZ IN 2021==')
        print('==WRITTEN IN PYTHON==')
        print('==CHARACTER BY BRYCE CANO==')
        if var14 == 0:
            print('\nPLAY [1]')
        if var14 == 1:
            print('\nPLAY [1] ★')
        print('RESET [2]')
        while True:
            try:
                bsSel1 = int(input('\nACTION >> '))
                if bsSel1 == 1:
                    saveLoader()
                if bsSel1 == 2:
                    os.system('cls||clear')
                    print('\nThe Plains v0.21')
                    reset.resetter()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                splashScreen()

def saveLoader():
    config = configparser.ConfigParser()
    config.read('save/config14.ini')
    var14 = config.getint('gameover', 'var14')
    config = configparser.ConfigParser()
    config.read('save/config2.ini')
    var2 = config.getint('chaptflagger', 'var2')
    if var14 == 0:
        if var2 == 0: #Chapter 1
            mm1.mainMenu1()
        if var2 == 1: #Chapter 2
            mm2.mainMenu2()
        if var2 == 2: #Chapter 3
            mm3.mainMenu3()
    if var14 == 1:
        mm3.mainMenu3()

##==ALTERNATE ENDINGS==##

def mainExt():
    os.system('cls||clear')
    print('\n==AAAAAAAAAA==')
    print('==AAAAAAAA AAAAAAA AAAAAAA==')
    print('==KILLER KILLER KILLER==')
    print('==KILLER KILLER==')
    time.sleep(0.05)
    os.system('cls||clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    time.sleep(5)
    mainExt2()

def mainExt2():
    os.system('cls||clear')
    print('\n==THE PLAINS==')
    print('==MADE BY DRAUMAZ IN 2021==')
    print('==WRITTEN IN PYTHON==')
    print('==CHARACTER BY BRYCE CANO==')
    print('\n[3]')
    while True:
        try:
            extSel = int(input('\nACTION >> '))
            if extSel == 3:
                mainAlt()
        except ValueError:
            mainExt2()

def mainAlt():
    os.system('cls||clear')
    print('\n...')
    time.sleep(5)
    print("\nYou killed him.")
    time.sleep(3)
    print("You abandoned your friends.")
    time.sleep(3)
    os.system('cls||clear')
    print('\n...')
    time.sleep(2)
    mainAlt2()

def mainAlt2():
    config = configparser.ConfigParser()
    config.read('save/config10.ini')
    var10 = config.getint('badendext', 'var10')
    os.system('cls||clear')
    print("\nDo you regret it?")
    print('\nYES [1]')
    print('NO [2]')
    while True:
        try:
            altSel = int(input('\nACTION >> '))
            if altSel == 1:
                mainAlt3()
            if altSel == 2:
                if var10 == 1:
                    time.sleep(0.75)
                    print('\nError.')
                    time.sleep(0.5)
                    mainAlt2()
                if var10 == 0:
                    print("You're proud of it.")
                    time.sleep(2)
                    print("Here's your chance.")
                    time.sleep(1)
                    reset.resetter()
        except ValueError:
            mainAlt2()
        except KeyboardInterrupt:
            mainAlt2()

def mainAlt3():
    print('\nSo you regret what you have done.')
    time.sleep(2)
    print('You know, that changes nothing.')
    time.sleep(2)
    print("You killed him.")
    time.sleep(2)
    print(textwrap.fill("Think about what that means. You downloaded a game, just to kill an innocent creature.", 75))
    time.sleep(3)
    print("Does that make you feel good?")
    time.sleep(4)
    print("The ability to hurt others, without recourse?")
    time.sleep(4)
    os.system('cls||clear')
    time.sleep(2)
    print('\nYou still have the chance to make things right.')
    time.sleep(2)
    print('You can go back there, do the right thing.')
    time.sleep(2)
    mainAlt4()

def mainAlt4():
    os.system('cls||clear')
    print('\nWill you?')
    print('\nYES [1]')
    print('NO [2]')
    while True:
        try:
            schl = int(input('\nACTION >> '))
            if schl == 1:
                config = configparser.ConfigParser()
                config['badend'] = {'var9': '0'}
                with open('save/config9.ini', 'w') as configfile:
                       config.write(configfile)
                config = configparser.ConfigParser()
                config['badendext'] = {'var10': '0'}
                with open('save/config10.ini', 'w') as configfile:
                    config.write(configfile)
                time.sleep(2)
                reset.resetter()
            if schl == 2:
                mainAlt5()
        except ValueError:
            mainAlt4()

def mainAlt5():
    os.system('cls||clear')
    config = configparser.ConfigParser()
    config['badendext'] = {'var10': '1'}
    with open('save/config10.ini', 'w') as configfile:
        config.write(configfile)
    time.sleep(5)
    print('\nFATAL ERROR ENCOUNTERED')
    time.sleep(2)
    dest = open('plains.txt', 'w+')
    dest.write('EVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\nEVIL\n')
    dest.close()
    quit()

breakTest() #Execution call
