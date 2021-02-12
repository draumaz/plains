import os
import time
from config3 import *
from mm1 import *
from mm2 import *

os.system('clear')
print('\n==THE PLAINS==')
print('==MADE BY DRAUMAZ IN 2021==')
print('==WRITTEN WITH PYTHON AND VIM==')
print('==CHARACTER BY BRYCE CANO==')
time.sleep(1.5)

print('\nScanning save...')
time.sleep(0.5)

if var3 == 0:
    print('Save loaded.')
    time.sleep(0.5)
    os.system('clear')
    mainMenu1()
if var3 == 1:
    print('Save loaded.')
    time.sleep(0.5)
    os.system('clear')
    mm2.mainMenu2()
