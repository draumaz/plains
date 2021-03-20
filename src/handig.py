import configparser
import time
import os

#HANDIG#
#Tool reference script 
#Widely referenced in all other functions

def spookPull(): #Worst ending looper
    while True:
        try:
            file = open('plains.txt', 'r')
            file.close()
            print('EVIL')
            time.sleep(0.25)
        except FileNotFoundError:
            quit()

def savePull(): #Retrieves save states and returns them
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
            return var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16
        except ValueError:
            return

def versionHeader(): #Displays the title and version
    print('\nThe Plains v0.22\n')
    return

def invDisplay(): #Displays inventory
    config = configparser.ConfigParser()
    config.read('save/config15.ini')
    var15 = config.getint('blade', 'var15')
    config = configparser.ConfigParser()
    config.read('save/config16.ini')
    var16 = config.getint('flower', 'var16')
    if var16 == 0:
        flower = "EMPTY"
    if var15 == 0:
        blade = "EMPTY"
    if var16 == 1:
        flower = "1x FLOWER"
    if var16 == 2 or var16 == 3:
        flower = "0x FLOWER"
    if var15 == 1:
        blade = "1x KNIFE"
    if var15 == 2:
        blade = "0x KNIFE"
    print("INV:", flower, blade, '\n', sep=" | ")
    return
