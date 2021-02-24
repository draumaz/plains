import os
import time
import configparser
import tool

def toolFlagger():
	config = configparser.ConfigParser()
	config['toolflag'] = {'var3': '1'}
	with open('save/config3.ini', 'w') as configfile:
		config.write(configfile)
	tool.tool()
