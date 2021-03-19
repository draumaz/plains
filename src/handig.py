import configparser

def invDisplay():
    config = configparser.ConfigParser()
    config.read('save/config15.ini')
    var15 = config.getint('blade', 'var15')
    config = configparser.ConfigParser()
    config.read('save/config16.ini')
    var16 = config.getint('flower', 'var16')
    if var16 == 0:
        flower = "EMPTY"
    if var15 == 0:
        blade = "EMPTY"
    if var16 == 1:
        flower = "1x FLOWER"
    if var16 == 2 or var16 == 3:
        flower = "0x FLOWER"
    if var15 == 1:
        blade = "1x KNIFE"
    if var15 == 2:
        blade = "0x KNIFE"
    print('\nThe Plains v0.22\n') #Version
    print("INV:", flower, blade, '\n', sep=" | ") #Inventory display
    return
