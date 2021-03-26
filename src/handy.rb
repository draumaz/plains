def saveGen
    file = File.open("data.txt", "w")
    File.write("data.txt", "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
    return
end

def saveWrite(line_ext, state_ext)
    save = File.open('data.txt', 'r+') do |file|
        lines = file.each_line.to_a
        lines[line_ext] = state_ext, "\n"
        file.rewind
        file.write(lines.join)
        return
    end
end

def saveRead
    save = File.open('data.txt', 'r')
    var1 = Integer(save.readlines[0])
    save = File.open('data.txt', 'r')
    var2 = Integer(save.readlines[1])
    save = File.open('data.txt', 'r')
    var3 = Integer(save.readlines[2])
    save = File.open('data.txt', 'r')
    var4 = Integer(save.readlines[3])
    save = File.open('data.txt', 'r')
    var5 = Integer(save.readlines[4])
    save = File.open('data.txt', 'r')
    var6 = Integer(save.readlines[5])
    save = File.open('data.txt', 'r')
    var7 = Integer(save.readlines[6])
    save = File.open('data.txt', 'r')
    var8 = Integer(save.readlines[7])
    save = File.open('data.txt', 'r')
    var9 = Integer(save.readlines[8])
    save = File.open('data.txt', 'r')
    var10 = Integer(save.readlines[9])
    save = File.open('data.txt', 'r')
    var11 = Integer(save.readlines[10])
    save = File.open('data.txt', 'r')
    var12 = Integer(save.readlines[11])
    save = File.open('data.txt', 'r')
    var13 = Integer(save.readlines[12])
    save = File.open('data.txt', 'r')
    var14 = Integer(save.readlines[13])
    save = File.open('data.txt', 'r')
    var15 = Integer(save.readlines[14])
    save = File.open('data.txt', 'r')
    var16 = Integer(save.readlines[15])
    save.close
    return var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16
end

def splashDisplay
    puts '==THE PLAINS==============='
    puts '==MADE BY DRAUMAZ IN 2021=='
    puts '==MADE IN RUBY!============'
    puts '==CHARACTER BY BRYCE CANO=='
    return
end

def screenClear
    system("cls||clear")
    return
end

def versionHeader
    puts "\nThe Plains v0.23\n"
    return
end

def invDisplay
    var7 = saveRead[6]
    var15 = saveRead[14]
    var16 = saveRead[15]
    if var15 == 0
        blade = "EMPTY"
    end
    if var16 == 0
        flower = "EMPTY"
    end
    if var16 == 1
        flower = "1x FLOWER"
    end
    if var16 == 2 or var16 == 3 or var16 == 4
        flower = "0x FLOWER"
    end
    if var15 == 1 and var7 == 1
        blade = "1x KNIFE (BLOODIED)"
    end
    if var15 == 1 and var7 == 0
        blade = "1x KNIFE"
    end
    if var15 == 2
        blade = "0x KNIFE"
    end
    print "\nINV: ", flower, ' | ', blade
    puts ""
    return
end

def quitHandler
    exit
end

def inpErHandler
    puts "\nDid you mean something else?"
    sleep(0.5)
    return
end

def easterEgg
    puts "                   .-') _    ('-. .-.   ('-.                  "
    puts "                  (  OO) )  ( OO )  / _(  OO)                 "
    puts "                  /     '._ ,--. ,--.(,------.                "
    puts "                  |'--...__)|  | |  | |  .---'                "
    puts "                  '--.  .--'|   .|  | |  |                    "
    puts "                     |  |   |       |(|  '--.                 "
    puts "                     |  |   |  .-.  | |  .--'                 "
    puts "                     |  |   |  | |  | |  `---.                "
    puts "                     `--'   `--' `--' `------'                "
    puts "   _ (`-.              ('-.                  .-') _   .-')    "
    puts "  ( (OO  )            ( OO ).-.             ( OO ) ) ( OO ).  "
    puts " _.`     \ ,--.       / . --. /  ,-.-') ,--./ ,--,' (_)---\_) "
    puts "(__...--'' |  |.-')   | \-.  \   |  |OO)|   \ |  |\ /    _ |  "
    puts " |  /  | | |  | OO ).-'-'  |  |  |  |  \|    \|  | )\  :` `.  "
    puts " |  |_.' | |  |`-' | \| |_.'  |  |  |(_/|  .     |/  '..`''.) "
    puts " |  .___.'(|  '---.'  |  .-.  | ,|  |_.'|  |\    |  .-._)   \ "
    puts " |  |      |      |   |  | |  |(_|  |   |  | \   |  \       / "
    puts " `--'      `------'   `--' `--'  `--'   `--'  `--'   `-----'  "
    sleep(4)
    return
end