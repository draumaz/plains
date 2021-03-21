import os
import time
import mm2
import configparser
import textwrap
import handig

def friendFlagger3(): #Neutral Flag
    line_ext = 3
    state_ext = '3\n'
    handig.saveWriter(line_ext, state_ext)
    saan()
def friendFlagger2(): #Rude Flag
    line_ext = 3
    state_ext = '1\n'
    handig.saveWriter(line_ext, state_ext)
    mm2.mainMenu2()
def friendFlagger1(): #Flirty Flag
    line_ext = 3
    state_ext = '2\n'
    handig.saveWriter(line_ext, state_ext)
    saan()
def flowerFlag(): #Gave Flower Flag
    line_ext = 15
    state_ext = '3\n'
    handig.saveWriter(line_ext, state_ext)
    saan()

def saan():
    save = handig.savePull()
    var4 = save[3]
    var6 = save[5]
    var8 = save[7]
    var16 = save[15]
    if var8 == 0 and var6 == 1:
        os.system('cls||clear')
        handig.versionHeader()
        handig.invDisplay()
        print("Saan won't even look you in the eye.")
        time.sleep(4)
        mm2.mainMenu2()
    os.system('cls||clear')
    handig.versionHeader()
    handig.invDisplay()
    if var4 == 1:
        print('Saan seems distant.\n')
    if var4 != 1:
        print('Saan seems excited to talk to you.\n')
    print('WHERE ARE WE? [1]')
    print('FLIRT WITH HIM [2]')
    if var16 == 1:
        print('GIVE FLOWER [3]')
        print('BACK [4]')
    if var16 == 0 or var16 == 2 or var16 == 3:
        print('BACK [3]')
    saan2()

def saan2():
    save = handig.savePull()
    var4 = save[3]
    var6 = save[5]
    var8 = save[7]
    var16 = save[15]
    while True:
        try:
            friendSelect1 = int(input('\nACTION >> '))
            if friendSelect1 == 1:
                print('')
                print(textwrap.fill("Saan explains how far away you ended up. This planet is light years away from home..."))
                time.sleep(5)
                friendFlagger3()
            if friendSelect1 == 2:
                if var4 == 2:
                    print('')
                    print(textwrap.fill("You keep telling him how cute he is. He looks happy.", 75))
                    time.sleep(2)
                    saan()
                if var4 == 1:
                    print('\nHe seems busy right now.')
                    time.sleep(2)
                    saan()
                if var4 == 0 or 3:
                    print('\nYou tell Saan that he has cute eyes.')
                    time.sleep(3)
                    print("You're making him blush!")
                    time.sleep(2)
                    friendFlagger1()
            if friendSelect1 == 3:
                if var16 == 0 and var4 == 1 or var16 == 2 and var4 == 1: #back|no flower, rude
                    mm2.mainMenu2()
                if var16 == 0 and var4 == 2 or var16 == 2 and var4 == 2: #back|no flower, flirty
                    print('\nSaan follows you back to where you started, looking happy.')
                    time.sleep(3)
                    mm2.mainMenu2()
                if var16 == 0 and var4 == 0 or var16 == 0 and var4 == 3: #back|no flower, neutral
                    print('\nSaan follows you back to where you started.')
                    time.sleep(3)
                    mm2.mainMenu2()
                if var16 == 1 and var4 == 1: #flower, rude
                    print('\nSaan reluctantly takes the flower. He looks confused.')
                    time.sleep(3)
                    flowerFlag()
                if var16 == 1 and var4 == 2: #flower, flirty
                    print("\nSaan looks borderline embarassed, you've made him blush quite a bit.")
                    print('He happily takes the flower.')
                    time.sleep(3)
                    flowerFlag()
                if var16 == 1 and var4 == 3 or var16 == 1 and var4 == 0: #flower, neutral
                    print("\nSaan appreciates the flower. He admires its petals and form.")
                    time.sleep(3)
                    flowerFlag()
                if var16 == 3 and var4 == 1: #back|flower, rude
                    print('\nSaan follows you back.')
                    time.sleep(2)
                    mm2.mainMenu2()
                if var16 == 3 and var4 == 3: #back|flower, neutral
                    print('\nSaan follows you back to where you started, admiring the flower.')
                    time.sleep(3)
                    mm2.mainMenu2()
                if var16 == 3 and var4 == 2: #back|flower, flirty
                    print('')
                    print(textwrap.fill("Saan happily follows you back to where you started, looking at his flower as he walks.", 75))
                    time.sleep(5)
                    mm2.mainMenu2()   
                else: #Unpredictable scenario handler
                    print("\nYou and Saan head back.")
                    time.sleep(3)
                    mm2.mainMenu2()
            if friendSelect1 == 4:
                if var4 <= 1:
                    print('\nYou walk back without talking...how rude.')
                    time.sleep(2)
                    friendFlagger2()
                if var4 == 2:
                    print('')
                    print(textwrap.fill('You head back to the rest of your friends, Saan still blushing.', 75))
                    time.sleep(2)
                    mm2.mainMenu2()
            if friendSelect1 > 4 or friendSelect1 < 0:
                handig.inpErrorHandler()
                saan()
        except ValueError:
            handig.inpErrorHandler()
            saan()
