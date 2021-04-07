import textwrap
import scripts
import time
import os
import hill

def battleFlashy():
	scripts.screenClear()
	print('\nB')
	time.sleep(0.06)
	print('A')
	time.sleep(0.06)
	print('T')
	time.sleep(0.06)
	print('T')
	time.sleep(0.06)
	print('L')
	time.sleep(0.06)
	print('E')
	time.sleep(0.06)
	print(' ')
	time.sleep(0.06)
	print('B')
	time.sleep(0.06)
	print('E')
	time.sleep(0.06)
	print('G')
	time.sleep(0.06)
	print('I')
	time.sleep(0.06)
	print('N')
	time.sleep(0.06)
	print('!')
	time.sleep(1)
	battleBegin()

def battleBegin():
	scripts.screenClear()
	scripts.versionHeader()
	print('NAME: LIAM | ATTACK: 0 | DEF: 0')
	print('ENEMY: LIZARD | ATTACK: 60 | DEF: 100')
	print('\nPUNCH [1]')
	print('ITEMS [2]')
	print('FLEE [3]')
	choose = int(input('\nACTION >> '))
	if choose == 1:
		print("\nYou're too weak.")
		time.sleep(1)
		battleBegin()
	if choose == 2:
		battleItems()
	if choose == 3:
		print("\nSeems like the wrong guy to mess with.")
		time.sleep(2)
		hill.hill()
		
def battleItems():
	vars = scripts.savePull()
	has_knife = vars[14]
	if has_knife == 1:
		knife_stat = "1x"
	if has_knife == 0:
		knife_stat = "0x"
	print('')
	time.sleep(0.04)
	print(knife_stat, 'KNIFE [1]')
	time.sleep(0.04)
	print('BACK [2]')
	time.sleep(0.04)
	choose = int(input('\nACTION >> '))
	if choose == 1:
		line_ext = 5
		state_ext = 1
		scripts.saveWriter(line_ext, state_ext)
		line_ext = 6
		state_ext = 1
		scripts.saveWriter(line_ext, state_ext)
		print('\nYou stab him to death.')
		time.sleep(4)
		hill.hill()
	if choose == 2:
		battleBegin()
	