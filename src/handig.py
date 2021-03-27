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
            one = int(lines[0])
            two = int(lines[1])
            three = int(lines[2])
            four = int(lines[3])
            five = int(lines[4])
            six = int(lines[5])
            seven = int(lines[6])
            eight = int(lines[7])
            nine = int(lines[8])
            ten = int(lines[9])
            eleven = int(lines[10])
            twelve = int(lines[11])
            thirteen = int(lines[12])
            fourteen = int(lines[13])
            fifteen = int(lines[14])
            sixteen = int(lines[15])
            save.close()
            return [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
        except ValueError:
            saveCorruptHandler()
        except FileNotFoundError:
            saveGenerator()

def saveCorruptHandler():
    while True:
        try:
            os.system('cls||clear')
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

def versionHeader(): #Displays the title and version
    print('\nThe Plains v0.23\n')

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

def quitHandler(): #Handles quit actions
    os.system('cls||clear')
    quit()

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
    os.system('cls||clear')
