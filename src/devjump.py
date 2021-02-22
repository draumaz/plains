import mm2
import mm1
import time
import os
import configparser

os.system('clear')
print('\nThe Plains v0.17\n')
print('CHAPTER 1 [1]')
print('CHAPTER 2 [2]')
print('PROD RESET [3]')
print('BAD END [4]')

devSelect = int(input('\nACTION >> '))
if devSelect == 1:
    mm1.mainMenu1()
if devSelect == 2:
    config = configparser.ConfigParser()
    config['ch1endflag'] = {'var1': '1'}
    with open('save/config.ini', 'w') as configfile:
           config.write(configfile)
    config = configparser.ConfigParser()
    config['chaptflagger'] = {'var2': '1'}
    with open('save/config2.ini', 'w') as configfile:
           config.write(configfile)
    mm2.mainMenu2()
if devSelect == 3:
    print('\nProcessing...')
    config = configparser.ConfigParser()
    config['ch1endflag'] = {'var1': '0'}
    with open('save/config.ini', 'w') as configfile:
           config.write(configfile)

    config = configparser.ConfigParser()
    config['chaptflagger'] = {'var2': '0'}
    with open('save/config2.ini', 'w') as configfile:
           config.write(configfile)

    config = configparser.ConfigParser()
    config['toolflag'] = {'var3': '0'}
    with open('save/config3.ini', 'w') as configfile:
           config.write(configfile)

    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '0'}
    with open('save/config4.ini', 'w') as configfile:
           config.write(configfile)

    config = configparser.ConfigParser()
    config['reset'] = {'var5': '0'}
    with open('save/config5.ini', 'w') as configfile:
        config.write(configfile)

    config = configparser.ConfigParser()
    config['lizard'] = {'var6': '0'}
    with open('save/config6.ini', 'w') as configfile:
        config.write(configfile)

    config = configparser.ConfigParser()
    config['lizardext'] = {'var7': '0'}
    with open('save/config7.ini', 'w') as configfile:
        config.write(configfile)

    config = configparser.ConfigParser()
    config['okay'] = {'var8': '0'}
    with open('save/config8.ini', 'w') as configfile:
        config.write(configfile)

    config = configparser.ConfigParser()
    config['badend'] = {'var9': '0'}
    with open('save/config9.ini', 'w') as configfile:
        config.write(configfile)

    time.sleep(0.25)
    print('Complete.')
    time.sleep(1)
    quit()
if devSelect == 4:
    print('\nProcessing...')

    config = configparser.ConfigParser()
    config['badend'] = {'var9': '1'}
    with open('save/config9.ini', 'w') as configfile:
        config.write(configfile)
    config = configparser.ConfigParser()
    config['ch1endflag'] = {'var1': '1'}
    with open('save/config.ini', 'w') as configfile:
           config.write(configfile)
    config = configparser.ConfigParser()
    config['chaptflagger'] = {'var2': '1'}
    with open('save/config2.ini', 'w') as configfile:
           config.write(configfile)
    time.sleep(0.25)
    print('Complete.')
    time.sleep(1)
    quit()
