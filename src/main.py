import os
import time
import configparser
import mm1
import mm2

os.system('clear')
print('\n==THE PLAINS==')
print('==MADE BY DRAUMAZ IN 2021==')
print('==WRITTEN WITH PYTHON AND VIM==')
print('==CHARACTER BY BRYCE CANO==')
time.sleep(1.5)

print('\nScanning save...')
config = configparser.ConfigParser()
config.read('save/config2.ini')
var2 = config.getint('chaptflagger', 'var2')

time.sleep(0.5)

if var2 == 0:
    print('Save loaded.')
    time.sleep(0.5)
    os.system('clear')
    mm1.mainMenu1()

if var2 == 1:
    print('Save loaded.')
    time.sleep(0.5)
    os.system('clear')
    mm2.mainMenu2()
