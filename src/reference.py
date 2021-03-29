import handig
import os
import reset

##Cleaning and reference scripts for internal usage##

def display():
    save = handig.savePull()
    var1 = save[0]
    var2 = save[1]
    var3 = save[2]
    var4 = save[3]
    var5 = save[4]
    var6 = save[5]
    var7 = save[6]
    var8 = save[7]
    var9 = save[8]
    var10 = save[9]
    var11 = save[10]
    var12 = save[11]
    var13 = save[12]
    var14 = save[13]
    var15 = save[14]
    var16 = save[15]
    print('')
    print('VAR1: CH1ENDFLAG', '      |', 'STATE:', var1)
    print('VAR2: CHAPTFLAG', '       |', 'STATE:', var2)
    print('VAR3: TOOLFLAG', '        |', 'STATE:', var3)
    print('VAR4: FRIENDFLAG', '      |', 'STATE:', var4)
    print('VAR5: RESET', '           |', 'STATE:', var5)
    print('VAR6: LIZARD', '          |', 'STATE:', var6)
    print('VAR7: LIZARD-EXT', '      |', 'STATE:', var7)
    print('VAR8: OKAY', '            |', 'STATE:', var8)
    print('VAR9: BADEND', '          |', 'STATE:', var9)
    print('VAR10: BADEND-EX', '      |', 'STATE:', var10)
    print('VAR11: SPLASHSKIP', '     |', 'STATE:', var11)
    print('VAR12: LIZARD-DX', '      |', 'STATE:', var12)
    print('VAR13: SPLASHSKIP2', '    |', 'STATE:', var13)
    print('VAR14: GAMEOVER', '       |', 'STATE:', var14)
    print('VAR15: BLADE', '          |', 'STATE:', var15)
    print('VAR16: FLOWER', '         |', 'STATE:', var16)
    print('')

def varMod():
    mod_var = input('\nSelect variable to change (ex. for var12, write 11 (this is not a typo)): ')
    print('Writing to var', mod_var, sep='')
    print('')
    mod_st = input('Variable to write (ex. for 5, write 5): ')
    print('')
    line_ext = int(mod_var)
    state_ext = int(mod_st)
    handig.saveWriter(line_ext, state_ext)
    print('★★★ Wrote variable', state_ext, 'to line', line_ext)
    
def landing():
    print('')
    print('Variable modding [1]')
    print('Variable display [2]')
    print('Variable clear [3]')
    while True:
        try:
            lan = int(input('\nACTION >> '))
            if lan == 1:
                varMod()
                landing()
            if lan == 2:
                display()
                landing()
            if lan == 3:
                os.remove('data.txt')
                handig.saveGenerator()
                print('\nFile reset')
                landing()
        except ValueError:
            print('\n\n\n\n\n\n\n\n\n\n')
            landing()

def clean():
    os.system('rm -r __pycache__')
    os.system('rm -r data.txt')
    os.system('rm -r .DS_Store')
    os.system('rm -r ../.DS_Store')
    quit()

clean()
#landing() #uncomment for var list