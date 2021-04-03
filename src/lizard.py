import os
import time
import scripts
import textwrap
import mm3

def Lizard():
	while True:
		try:
			scripts.screenClear()
			scripts.versionHeader()
			scripts.invDisplay()
			vars = scripts.savePull()
			var5 = vars[4]
			var6 = vars[5]
			var7 = vars[6]
			var15 = vars[14]
			var16 = vars[15]
			print('You and your friends walk towards the lizard. ', end='')
			if var16 == 2:
				print('He waves at you all, inviting you over!')
			if var16 == 0 or 1 or 3:
				print('He notices you.')
			if var5 == 1 and var7 == 1:
				print('He looks incredibly hesistant.')
			print('\nTALK [1]')
			print('OPTION [2]')
			print('BACK [3]')
			choose = int(input('\nACTION >> '))
			if choose == 1:
				if var5 == 1 and var7 == 1:
					print("\nYou ask him why he looks so nervous. He can't even look at you.")
					time.sleep(3)
					print("He leaves in a hurry.")
					time.sleep(2)
					line_ext = 17
					state_ext = 1
					scripts.saveWriter(line_ext, state_ext)
					#write new var so he doesn't show up on mm3
					mm3.mainMenu3()
				if var6 == 1:
					Lizard() #shouldn't be possible
				if var16 == 2:
					print('\nHe starts up a little chat with you guys.')
					print('Seems like he really appreciates your presence.')
					time.sleep(5)
					Lizard()
				else:
					print('\nThe lizard man asks you guys if you need help getting back home.')
					time.sleep(3)
					print("Kinda obvious, isn't it?")
					time.sleep(2)
					Lizard()
			if choose == 2:
				pass
			if choose == 3:
				print('\nYou all tell him that you need to go for a bit.')
				time.sleep(2)
				mm3.mainMenu3()
			if choose > 3 or choose < 1:
				scripts.inpErrorHandler()
				Lizard()
		except ValueError:
			scripts.inpErrorHandler()
			Lizard()