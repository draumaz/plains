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
	time.sleep(0.5)
	battleBegin()

def battleBegin():
	while True:
		try:
			varz = scripts.savePull()
			var = varz[10]
			scripts.screenClear()
			scripts.versionHeader()
			print('NAME: LIAM | ATTACK: 0 | DEF: 0')
			print('ENEMY: LIZARD | ATTACK: 60 | DEF: 100')
			print('\nPUNCH [1]')
			print('ITEMS [2]')
			print('FLEE [3]')
			choose = int(input('\nACTION >> '))
			if choose == 1:
				line_ext = 10
				state_ext = var + 1
				scripts.saveWriter(line_ext, state_ext)
				if var <= 0:
					print("\nYou're too weak.")
					time.sleep(0.35)
					print("He's fully unaffected.")
					time.sleep(1)
					print("...doesn't seem like he wants to be doing this.")
					time.sleep(2)
					battleBegin()
				if var == 1:
					print("\nHe's starting to lose his patience.")
					time.sleep(2)
					battleBegin()
				if var == 2:
					print('\nGetting really impatient now.')
					time.sleep(2)
					battleBegin()
				if var == 3:
					line_ext = 11
					state_ext = 1
					scripts.saveWriter(line_ext, state_ext)
					print('\nThe lizard man gets tired of this, and leaves.')
					time.sleep(2)
					hill.hill()
				if var != 0 or var != 1 or var != 2 or var != 3:
					battleBegin()
			if choose == 2:
				battleItems()
			if choose == 3:
				print("\nSeems like the wrong guy to mess with.")
				time.sleep(2)
				hill.hill()
			if choose > 3 or choose < 1:
				scripts.inpErrorHandler()
				battleBegin()
		except ValueError:
			scripts.inpErrorHandler()
			battleBegin()
		
def battleItems():
	while True:
		try:
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
				print('\nYou lunge at the lizard and stab him to death.')
				time.sleep(4)
				hill.hill()
			if choose == 2:
				battleBegin()
			if choose > 2 or choose < 1:
				scripts.inpErrorHandler()
				battleBegin()
		except ValueError:
			scripts.inpErrorHandler()
			battleBegin()
	