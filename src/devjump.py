import mm3
import mm2
import mm1
import time
import os
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
                config = configparser.ConfigParser()
                config['ch1endflag'] = {'var1': '1'}
                with open('save/config.ini', 'w') as configfile:
                       config.write(configfile)
                config = configparser.ConfigParser()
                config['chaptflagger'] = {'var2': '1'}
                with open('save/config2.ini', 'w') as configfile:
                       config.write(configfile)
                mm2.mainMenu2()

            if devSelect == 3: #Chapter 3 Jump
                config = configparser.ConfigParser()
                config['ch1endflag'] = {'var1': '1'}
                with open('save/config.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['chaptflagger'] = {'var2': '2'}
                with open('save/config2.ini', 'w') as configfile:
                    config.write(configfile)
                mm3.mainMenu3()

            if devSelect == 4: #Full Reset
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
                config = configparser.ConfigParser()
                config['badendext'] = {'var10': '0'}
                with open('save/config10.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['splashskip'] = {'var11': '0'}
                with open('save/config11.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['lizarddx'] = {'var12': '0'}
                with open('save/config12.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['splashskip2'] = {'var13': '0'}
                with open('save/config13.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['gameover'] = {'var14': '0'}
                with open('save/config14.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['blade'] = {'var15': '0'}
                with open('save/config15.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['flower'] = {'var16': '0'}
                with open('save/config16.ini', 'w') as configfile:
                    config.write(configfile)
                time.sleep(0.05)
                print('Complete.')
                time.sleep(0.1)
                devJump()

            if devSelect == 5: #Bad Ending
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
                print('Complete.')
                time.sleep(0.25)
                devJump()

            if devSelect == 6:
                config = configparser.ConfigParser()
                config['toolflag'] = {'var3': '1'}
                with open('save/config3.ini', 'w') as configfile:
                       config.write(configfile)
                print('\nVariable set.')
                time.sleep(0.2)
                devJump()

            if devSelect == 7:
                config = configparser.ConfigParser()
                config['lizard'] = {'var6': '1'}
                with open('save/config6.ini', 'w') as configfile:
                    config.write(configfile)
                config = configparser.ConfigParser()
                config['lizardext'] = {'var7': '1'}
                with open('save/config7.ini', 'w') as configfile:
                    config.write(configfile)
                print('\nVariables set.')
                time.sleep(0.2)
                devJump()

            if devSelect == 8:
                config = configparser.ConfigParser()
                config['splashskip'] = {'var11': '1'}
                with open('save/config11.ini', 'w') as configfile:
                    config.write(configfile)
                print('\nVariables set.')
                time.sleep(0.2)
                devJump()

            if devSelect == 9:
                config = configparser.ConfigParser()
                config['splashskip'] = {'var11': '0'}
                with open('save/config11.ini', 'w') as configfile:
                    config.write(configfile)
                print('\nVariables set.')
                time.sleep(0.2)
                devJump()

            if devSelect == 10:
                config = configparser.ConfigParser()
                config['flower'] = {'var16': '1'}
                with open('save/config16.ini', 'w') as configfile:
                    config.write(configfile)

            if devSelect == 11:
                os.system('cls||clear')
                quit()
        except ValueError:
            devJump()

devJump()
