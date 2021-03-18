import configparser

def invDisplay():
    config = configparser.ConfigParser()
    config.read('save/config15.ini')
    var15 = config.getint('blade', 'var15')
    config = configparser.ConfigParser()
    config.read('save/config16.ini')
    var16 = config.getint('flower', 'var16')
    if var16 == 0:
        flower = ""
    if var16 == 1:
        flower = "1x Flower"
    if var16 == 2:
        flower = "0x Flower"
    if var15 == 0:
        blade = ""
    if var15 == 1:
        blade = "1x Knife"
    if var16 != 0 or var15 != 0:
        print("INV:", flower, blade, '\n', sep=" | ")
    return
