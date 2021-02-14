import os
import time
import configparser
import tool

def toolFlagger():
	config = configparser.ConfigParser()
	config['toolflag'] = {'var2': '1'}
	with open('config2.ini', 'w') as configfile:
		config.write(configfile)
	tool.tool()
