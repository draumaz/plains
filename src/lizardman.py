import configparser
import hill

def lizardMan():
    config = configparser.ConfigParser()
    config['lizard'] = {'var6': '1'}
    with open('save/config6.ini', 'w') as configfile:
        config.write(configfile)
    hill.hill()
