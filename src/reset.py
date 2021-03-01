import os
import time
import main
import configparser

def resetter():

    config = configparser.ConfigParser()
    config.read('save/config9.ini')
    var9 = config.getint('badend', 'var9')

    if var9 == 0:
        print('\nDoing this will reset everything. Are you sure?')
        print('\nRESET [1]')
        print('BACK [2]')
    if var9 == 1:
        print('\nRESET [1]')

    while True:
        try:
            reSel1 = int(input('\nACTION >> '))

            while reSel1 < 1 or reSel1 > 2:
                print('\nDid you mean something else?')
                time.sleep(0.5)
                resetter()

            if reSel1 == 1:
                if var9 == 1:
                    print('\nResetting...')
                    time.sleep(6)
                    print('Reset failed.')
                    config = configparser.ConfigParser()
                    config['badendext'] = {'var10': '1'}
                    with open('save/config10.ini', 'w') as configfile:
                        config.write(configfile)
                    time.sleep(2)
                    print('\nPlease restart the game.')
                    time.sleep(3)
                    quit()

                if var9 == 0:

                    print('\nResetting...')

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
                    config['reset'] = {'var5': '1'}
                    with open('save/config5.ini', 'w') as configfile:
                        config.write(configfile)

                    config = configparser.ConfigParser()
                    config['lizard'] = {'var6': '0'}
                    with open('save/config6.ini', 'w') as configfile:
                        config.write(configfile)

                    config = configparser.ConfigParser()
                    config['okay'] = {'var8': '0'}
                    with open('save/config8.ini', 'w') as configfile:
                        config.write(configfile)

                    config = configparser.ConfigParser()
                    config['gameover'] = {'var14': '0'}
                    with open('save/config14.ini', 'w') as configfile:
                        config.write(configfile)

                    config = configparser.ConfigParser()
                    config['blade'] = {'var15': '0'}
                    with open('save/config15.ini', 'w') as configfile:
                        config.write(configfile)

                    time.sleep(0.5)

                    print('Reset.')
                    time.sleep(1)
                    print('\nPlease restart the game.')
                    time.sleep(3)
                    os.system('cls||clear')
                    quit()

            if reSel1 == 2:
                if var9 == 1:
                    resetter()
                if var9 == 0:
                    print('\nThe game will now close. Your data was not altered.')
                    time.sleep(2)
                    quit()
        except ValueError:
            print('\nDid you mean something else?')
            time.sleep(0.5)
            resetter()
