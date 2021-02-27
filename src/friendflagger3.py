import configparser
import saan

def friendFlagger3(): #Neutral Flag
    config = configparser.ConfigParser()
    config['friendflag'] = {'var4': '1'}
    with open('save/config4.ini', 'w') as configfile:
        config.write(configfile)
    saan()
