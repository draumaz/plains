import os
import sys
import time
import scripts
import textwrap
import mm3

def riverMain():
	while True:
		try:
			vars = scripts.savePull()
			has_bottle = vars[16]
			scripts.screenClear()
			scripts.versionHeader()
			scripts.invDisplay()
			print(textwrap.fill('Making your way over to a river, you see lots of strange grasses. The water flows peacefully.', 75))
			print('\nSIT DOWN [1]')
			if has_bottle == 1 or has_bottle == 5:
				print('FILL BOTTLE [2]')
			if has_bottle == 4:
				print('DUMP WATER OUT [2]')
			if has_bottle == 2 or has_bottle == 0:
				print('DRINK WATER [2]')
			print('BACK [3]')
			choose = int(input('\nACTION >> '))
			if choose == 1:
				pass
			if choose == 2:
				if has_bottle == 1 or has_bottle == 5:
					line_ext = 16
					state_ext = 4
					scripts.saveWriter(line_ext, state_ext)
					print('\nYou scoop your bottle in the water and collect it.')
					time.sleep(3)
					riverMain()
				if has_bottle == 2 or has_bottle == 0:
					print('\nYou drink the water. It tastes sweet...')
					time.sleep(3)
					riverMain()
				if has_bottle == 4:
					line_ext = 16
					state_ext = 5
					scripts.saveWriter(line_ext, state_ext)
					print('\nYou dump the water out into the river.')
					time.sleep(3)
					riverMain()
			if choose == 3:
				print("\nAs beautiful as the river is, there's so much more to discover.")
				time.sleep(4)
				mm3.mainMenu3()
			if choose > 3 or choose < 1:
				scripts.inpErrorHandler()
				riverMain()
		except ValueError:
			scripts.inpErrorHandler()
			riverMain()