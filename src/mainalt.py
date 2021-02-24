import os
import time
import configparser
import reset
import textwrap

def mainAlt():
    os.system('cls||clear')
    print('\n...')
    time.sleep(5)
    print("\nDo you regret your actions?")
    print('\nYES [1]')
    print('NO [2]')

    altSel = int(input('\nACTION >> '))

    while altSel < 1 or altSel > 2:
        print('\nThis is not an acceptable response.')
        time.sleep(2)
        mainAlt()

    if altSel == 1:
        print('\nSo you regret what you have done.')
        time.sleep(2)
        print('Do you really think this changes anything?')
        time.sleep(2)
        print("You're a murderer.")
        time.sleep(2)
        print(textwrap.fill("You have the ability to reset this world, over and over again..", 75))
        time.sleep(3)
        print("Does that make you feel good?")
        time.sleep(4)
        print("The ability to")
        time.sleep(0.5)
        print('Ḱ̴̪̰̬͉͎͙̯̝͓͉̖ͣ̔̾̓̍͐̓̋̏̽ͥ̍ͦ́͞͠I̧̡̦̣͓̬͚̪͚̻̳͙̰͖̭̭͚̭̥͓͕̊̂̿͛ͪ̒ͮ̍̓̈́̐̽͜L̛̘̟̘͎̘͙͚͍̖̦͍̠̹̠̠ͭͭ̅̌̄̓ͧͭ̈́͛̎̿̉͊͆L̛̫̮̳̼̦̦͓͚͖͇̑ͦ̿͋̆ͣ̑͆͂̀ͅ?̧̘̗͍͔͙̟̞̤̦͕̘͓̞̰̱̰ͮ̇ͥͪ̀ͅ')
        time.sleep(4)
        os.system('cls||clear')
        time.sleep(2)
        print('\nBut you still have the chance to make things right.')
        time.sleep(2)
        print('Please, do the right thing.')
        config = configparser.ConfigParser()
        config['badend'] = {'var9': '0'}
        with open('save/config9.ini', 'w') as configfile:
               config.write(configfile)
        time.sleep(2)
        reset.resetter()

    if altSel == 2:
        print('\nIs that so.')
        time.sleep(2)
        print('So be it.')
        time.sleep(2)
        quit()
