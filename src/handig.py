import os
import time

#HANDIG#
#Tool reference script 
#Widely referenced in all other functions

def saveWriter(line_ext, state_ext): #Save writing bus: all variable save instances pass through this function
    file = open('data.txt', 'r')
    line = file.readlines()
    line[line_ext] = state_ext
    file = open('data.txt', 'w')
    file.writelines(line)
    file.close()
    return

def saveGenerator(): #Creates save file if it doesn't already exist
    save = open('data.txt', 'w+')
    save.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    save.close()
    return

def savePull(): #Pulls and retrieves all variables and returns into an array
    while True:
        try:
            save = open('data.txt', 'r')
            lines = save.readlines()
            var1 = int(lines[0])
            var2 = int(lines[1])
            var3 = int(lines[2])
            var4 = int(lines[3])
            var5 = int(lines[4])
            var6 = int(lines[5])
            var7 = int(lines[6])
            var8 = int(lines[7])
            var9 = int(lines[8])
            var10 = int(lines[9])
            var11 = int(lines[10])
            var12 = int(lines[11])
            var13 = int(lines[12])
            var14 = int(lines[13])
            var15 = int(lines[14])
            var16 = int(lines[15])
            save.close()
            return var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16
        except ValueError:
            print('Save read failed. Please check your save.')
            quit()
        except FileNotFoundError:
            saveGenerator()

def versionHeader(): #Displays the title and version
    print('\nThe Plains v0.22\n')
    return

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
    return

def quitHandler(): #Handles quit actions
    os.system('cls||clear')
    quit()

def inpErrorHandler(): #ValueError exception handler
    print('\nDid you mean something else?')
    time.sleep(0.5)
    return
