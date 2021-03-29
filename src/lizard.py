import os
import time
import handig
import mm3

def Lizard():
	while True:
		try:
			handig.screenClear()
			handig.versionHeader()
			handig.invDisplay()
			vars = handig.savePull()
			var5 = vars[4]
			var7 = vars[6]
			var15 = vars[14]
			var16 = vars[15]
			print('You and your friends walk towards the lizard.', end=' ')
			if var16 == 2:
				print('He waves at you all, inviting you over!')
			if var16 == 0 or 1 or 3:
				print('He notices you.')
			if var5 == 1 and var7 == 1:
				print('He looks incredibly hesistant.')
			print('\nOPTION [1]')
			print('OPTION [2]')
			print('BACK [3]')
			choose = int(input('\nACTION >> '))
			if choose == 1:
				pass
			if choose == 2:
				pass
			if choose == 3:
				print('\nYou all tell him that you need to go for a bit.')
				time.sleep(2)
				mm3.mainMenu3()
			if choose > 3 or choose < 1:
				handig.inpErrorHandler()
				Lizard()
		except ValueError:
			handig.inpErrorHandler()
			Lizard()