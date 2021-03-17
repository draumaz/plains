import os
import time
import configparser
from configparser import NoOptionError, NoSectionError
import mm1
import mm2
import mm3
import mainalt
import mainext
import reset
import textwrap

def breakTest():
    while True:
        try:
            file = open('plains.txt', 'r')
            file.close()
            os.system('cls||clear')
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
            preSplash()
       except (NoOptionError, NoSectionError):
          saveDirGenerator()

def saveDirGenerator():
    while True:
        try:
            os.mkdir('save')
            saveGenerator()
        except FileExistsError:
            saveGenerator()

def saveGenerator():
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

def preSplash():
    config = configparser.ConfigParser()
    config.read('save/config11.ini')
    var11 = config.getint('splashskip', 'var11')
    splashScreen()

def splashScreen():
    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')
    config = configparser.ConfigParser()
    config.read('save/config10.ini')
    var10 = config.getint('badendext', 'var10')
    config = configparser.ConfigParser()
    config.read('save/config13.ini')
    var13 = config.getint('splashskip2', 'var13')

    if var10 == 1:
        mainalt.mainAlt2()
    if var9 == 1:
        mainext.mainExt()
    if var9 == 0:
        splashScreen2()

def splashScreen2(): #Main menu
    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')
    config = configparser.ConfigParser()
    config.read('save/config14.ini')
    var14 = config.getint('gameover', 'var14')

    if var9 == 1:
        mainext.mainExt()
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
                splashScreen2()

def saveLoader():
    config = configparser.ConfigParser()
    config.read('save/config14.ini')
    var14 = config.getint('gameover', 'var14')
    config = configparser.ConfigParser()
    config.read('save/config2.ini')
    var2 = config.getint('chaptflagger', 'var2')
    if var14 == 0:
        if var2 == 0: #Chapter 1
            os.system('cls||clear')
            mm1.mainMenu1()
        if var2 == 1: #Chapter 2
            os.system('cls||clear')
            mm2.mainMenu2()
        if var2 == 2: #Chapter 3
            os.system('cls||clear')
            mm3.mainMenu3()
    if var14 == 1:
        print('\nScanning save...')
        time.sleep(0.25)
        print('Save loaded.')
        time.sleep(0.5)
        mm3.mainMenu3()

breakTest() #Execution call
