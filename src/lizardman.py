import configparser
import hill

def lizardMan():
    config = configparser.ConfigParser() #Live
    config['lizard'] = {'var6': '1'}
    with open('save/config6.ini', 'w') as configfile:
        config.write(configfile)

    config = configparser.ConfigParser() #Persist
    config['lizardext'] = {'var7': '1'}
    with open('save/config7.ini', 'w') as configfile:
        config.write(configfile)

    hill.hill()
