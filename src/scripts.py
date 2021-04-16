import os
import sys
import time

def saveWriter(line_ext, state_ext): #Save write bus
    state_ext_wr = str(state_ext) + '\n'
    file = open('data.txt', 'r')
    line = file.readlines()
    line[line_ext] = state_ext_wr
    file = open('data.txt', 'w')
    file.writelines(line)
    file.close()

def saveGenerator(): #Creates blank save file
    file = open('data.txt', 'w+')
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    file.close()

def savePull(): #Retrieves variables and returns an array
    while True:
        try:
            file = open('data.txt', 'r')
            lines = file.readlines()
            a = int(lines[0]) #sound flag (end of chapter 1)
            b = int(lines[1]) #chapter launch flag
            c = int(lines[2]) #tool usage flag (chapter 1)
            d = int(lines[3]) #friend flag (chapter 2)
            e = int(lines[4]) #reset flag
            f = int(lines[5]) #lizard murder flag
            g = int(lines[6]) #lizard perm flag
            h = int(lines[7]) #explain flag (chapter 2)
            i = int(lines[8]) #bad ending flag
            j = int(lines[9]) #bad ending extended
            k = int(lines[10]) #lizard fight disappear (int 3)
            l = int(lines[11]) #lizard deluxe
            m = int(lines[12]) #skip splash 2 (deprecated)
            n = int(lines[13]) #game over (deprecated)
            o = int(lines[14]) #knife flag
            p = int(lines[15]) #flower flag
            q = int(lines[16]) #bottle flag
            r = int(lines[17]) #lizard gone flag (chapter 3)
            file.close()
            return [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]
        except ValueError:
            saveCorruptHandler()
        except FileNotFoundError:
            saveGenerator()

def saveCorruptHandler():
    while True:
        try:
            screenClear()
            print('\nYour save file is corrupted.')
            print('Would you like to reset?')
            print('\nYES [1]')
            print('NO [2]')
            choose = int(input('\nACTION >> '))
            if choose == 1:
                os.remove('data.txt')
                saveGenerator()
                print('\nSave reset. Please restart the game.')
                quit()
            if choose == 2:
                quit()
            if choose > 2 or choose < 1:
                inpErrorHandler()
                saveCorruptHandler()
        except ValueError:
            inpErrorHandler()
            saveCorruptHandler()

def screenClear():
    os.system('cls||clear')

def versionHeader(): #Displays the title and version
    print('\nThe Plains v0.25\n')

def invDisplay(): #Displays inventory
    save = savePull()
    did_murder = save[5]
    blade_state = save[14]
    flower_state = save[15]
    bottle_state = save[16]
    if blade_state != 0 or flower_state != 0 or bottle_state != 0:
        visibility = 1
    else:
        visibility = 0
    if flower_state == 0 or flower_state == 2 or flower_state == 4:
        flower = 'EMPTY'
    if flower_state == 1:
        flower = "1x FLOWER"
    if blade_state  == 0 or blade_state == 2:
        blade = 'EMPTY'
    if blade_state == 1 and did_murder == 0:
        blade = "1x KNIFE"
    if blade_state == 1 and did_murder == 1:
        blade = "1x KNIFE (BLOODIED)"
    if bottle_state == 0 or bottle_state == 2:
        bottle = 'EMPTY'
    if bottle_state == 1 or bottle_state == 5:
        bottle = "1x EMPTY BOTTLE"
    if bottle_state == 3:
        bottle = "1x BOTTLE (BLOOD)"
    if bottle_state == 4:
        bottle = "1x BOTTLE (WATER)"
    if visibility == 1:
        print("INV:", flower, blade, bottle, '\n', sep=" | ")
    if visibility == 0:
        print(end='')
        
def quitHandler():
    screenClear()
    sys.exit()

def inpErrorHandler(): #ValueError exception handler
    print('\nDid you mean something else?')
    time.sleep(0.25)

def easterEgg():
    print("                   .-') _    ('-. .-.   ('-.                  ")
    print("                  (  OO) )  ( OO )  / _(  OO)                 ")
    print("                  /     '._ ,--. ,--.(,------.                ")
    print("                  |'--...__)|  | |  | |  .---'                ")
    print("                  '--.  .--'|   .|  | |  |                    ")
    print("                     |  |   |       |(|  '--.                 ")
    print("                     |  |   |  .-.  | |  .--'                 ")
    print("                     |  |   |  | |  | |  `---.                ")
    print("                     `--'   `--' `--' `------'                ")
    print("   _ (`-.              ('-.                  .-') _   .-')    ")
    print("  ( (OO  )            ( OO ).-.             ( OO ) ) ( OO ).  ")
    print(" _.`     \ ,--.       / . --. /  ,-.-') ,--./ ,--,' (_)---\_) ")
    print("(__...--'' |  |.-')   | \-.  \   |  |OO)|   \ |  |\ /    _ |  ")
    print(" |  /  | | |  | OO ).-'-'  |  |  |  |  \|    \|  | )\  :` `.  ")
    print(" |  |_.' | |  |`-' | \| |_.'  |  |  |(_/|  .     |/  '..`''.) ")
    print(" |  .___.'(|  '---.'  |  .-.  | ,|  |_.'|  |\    |  .-._)   \ ")
    print(" |  |      |      |   |  | |  |(_|  |   |  | \   |  \       / ")
    print(" `--'      `------'   `--' `--'  `--'   `--'  `--'   `-----'  ")
    time.sleep(2)
    screenClear()

invDisplay()
