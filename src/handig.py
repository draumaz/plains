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
    file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    file.close()

def savePull(): #Retrieves variables and returns an array
    while True:
        try:
            file = open('data.txt', 'r')
            lines = file.readlines()
            a = int(lines[0])
            b = int(lines[1])
            c = int(lines[2])
            d = int(lines[3])
            e = int(lines[4])
            f = int(lines[5])
            g = int(lines[6])
            h = int(lines[7])
            i = int(lines[8])
            j = int(lines[9])
            k = int(lines[10])
            l = int(lines[11])
            m = int(lines[12])
            n = int(lines[13])
            o = int(lines[14])
            p = int(lines[15])
            q = int(lines[16])
            file.close()
            return [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]
        except ValueError:
            saveCorruptHandler()
        except FileNotFoundError:
            saveGenerator()

def saveCorruptHandler():
    while True:
        try:
            handig.screenClear()
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
    print('\nThe Plains v0.24\n')

def invDisplay(): #Displays inventory
    save = savePull()
    did_murder = save[6]
    blade_state = save[14]
    flower_state = save[15]
    bottle_state = save[16]
    if blade_state == 1 or flower_state == 1 or bottle_state == 1 or blade_state == 2 or flower_state == 2 or bottle_state == 2:
        visibility = 1
    else:
        visibility = 0
    if flower_state == 0 or flower_state == 2:
        flower = ''
    if flower_state == 1:
        flower = "1x FLOWER"
    if blade_state  == 0 or blade_state == 2:
        blade = ''
    if blade_state == 1 and did_murder == 0:
        blade = "1x KNIFE"
    if blade_state == 1 and did_murder == 1:
        blade = "1x KNIFE (BLOODIED)"
    if bottle_state == 0 or bottle_state == 2:
        bottle = ''
    if bottle_state == 1:
        bottle = "1x BOTTLE"
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
    handig.screenClear()

invDisplay()