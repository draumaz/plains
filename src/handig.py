import os
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
    save = open('data.txt', 'w+')
    save.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    save.close()

def savePull(): #Retrieves variables and returns an array
    while True:
        try:
            save = open('data.txt', 'r')
            lines = save.readlines()
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
            save.close()
            return [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
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
    os.system('clear')

def versionHeader(): #Displays the title and version
    print('\nThe Plains v0.23_02\n')

def invDisplay(): #Displays inventory
    save = savePull()
    var7 = save[6]
    var15 = save[14]
    var16 = save[15]
    if var16 == 0:
        flower = "EMPTY"
    if var15 == 0:
        blade = "EMPTY"
    if var16 == 1:
        flower = "1x FLOWER"
    if var16 == 2 or var16 == 3 or var16 == 4:
        flower = "0x FLOWER"
    if var15 == 1 and var7 == 0:
        blade = "1x KNIFE"
    if var15 == 1 and var7 == 1:
        blade = "1x KNIFE (BLOODIED)"
    if var15 == 2:
        blade = "0x KNIFE"
    print("INV:", flower, blade, '\n', sep=" | ")

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
