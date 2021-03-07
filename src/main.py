import os
import time
import configparser
from configparser import NoOptionError, NoSectionError
import mm1
import mm2
import mm3
import mainalt
import mainext
import settings
import textwrap

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
            preSplash()
       except (NoOptionError, NoSectionError): 
          print('')
          print(textwrap.fill("The game was not able to detect critical files. Please double check that this file is in the same folder as the 'save' folder, and restart the game.", 75))
          print('')
          quit()

def preSplash():
    config = configparser.ConfigParser()
    config.read('save/config11.ini')
    var11 = config.getint('splashskip', 'var11')

    if var11 == 0:
        config = configparser.ConfigParser() #Disable message on future plays
        config['splashskip'] = {'var11': '1'}
        with open('save/config11.ini', 'w') as configfile:
            config.write(configfile)

        os.system('cls||clear')
        print('')
        print(textwrap.fill("A MESSAGE FROM THE DEVELOPER:", 75))
        time.sleep(1)
        print('')
        print(textwrap.fill("Thank you for trying out The Plains! This is a major labor of love, and it happens to be my first long-form programming pursuit. The contents in this game are subject to change, as this is a very, very early build.", 75))
        time.sleep(10)
        print('')
        print(textwrap.fill("Regardless, I hope you enjoy the game!", 75))
        time.sleep(1)
        print('')
        print(textwrap.fill("-draumaz"))
        time.sleep(4)
        os.system('cls||clear')
        splashScreen()
    if var11 == 1:
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
        if var13 == 0:
            os.system('cls||clear')
            print('\n==THE PLAINS==')
            print('==MADE BY DRAUMAZ IN 2021==')
            print('==WRITTEN IN PYTHON==')
            print('==CHARACTER BY BRYCE CANO==')
            time.sleep(2)
            splashScreen2()
        if var13 == 1:
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
        print('SETTINGS [2]')
        while True:
            try:
                bsSel1 = int(input('\nACTION >> '))
                if bsSel1 == 1:
                    saveLoader()
                if bsSel1 == 2:
                    settings.settingsMain()
            except ValueError:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                splashScreen2()
                  
def saveLoader():
    config = configparser.ConfigParser()
    config.read('save/config14.ini')
    var14 = config.getint('gameover', 'var14')
    if var14 == 0:
        print('\nScanning save...')
        
        config = configparser.ConfigParser()
        config.read('save/config2.ini')
        var2 = config.getint('chaptflagger', 'var2')
        time.sleep(0.15)

        if var2 == 0: #Chapter 1
            print('Save loaded.')
            time.sleep(0.5)
            mm1.mainMenu1()
        if var2 == 1: #Chapter 2
            print('Save loaded.')
            time.sleep(0.5)
            mm2.mainMenu2()
        if var2 == 2: #Chapter 3
            print('Save loaded.')
            time.sleep(0.5)
            mm3.mainMenu3()
    if var14 == 1:
        print('\nScanning save...')
        time.sleep(0.25)
        print('Save loaded.')
        time.sleep(0.5)
        mm3.mainMenu3()

fileTest() #Execution call
