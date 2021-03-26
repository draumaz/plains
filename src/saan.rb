require './handy'
require './mm2'

def saan
    var4 = saveRead[3]
    var6 = saveRead[5]
    var8 = saveRead[7]
    var16 = saveRead[15]
    screenClear
    versionHeader
    invDisplay
    if var8 == 0 and var6 == 1
        puts "\nSaan won't even look you in the eye."
        sleep(4)
        mainMenu2
    end
    if var4 == 1
        puts "\nSaan seems distant."
    end
    if var4 != 1
        puts "\nSaan seems excited to see you."
    end
    puts "\nWHERE ARE WE? [1]"
    puts "FLIRT WITH HIM [2]"
    if var16 != 1
        puts "BACK [3]"
    end
    if var16 == 1
        puts "GIVE FLOWER [3]"
        puts "BACK [4]"
    end
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
        puts "\nSaan explains how far away you ended up. It's a good thing you called them in time."
        sleep(5)
        saan
    end
    if choose == 2
        if var4 == 1
            puts "\nHe seems busy."
            sleep(2)
            mainMenu2
        end
        if var4 == 2
            puts "\nYou keep telling him how cute he is...you're making him blush!"
            sleep(4)
            saan
        end
        if var4 == 0 or var4 == 3
            puts "\nYou tell Saan that he has cute eyes."
            sleep(2)
            puts "He looks happy."
            sleep(2)
            flirtytoSaan
            saan
        end
    end
    if choose == 3
        if var16 == 0 and var4 == 1 or var16 == 2 and var4 == 1
            mainMenu2
        end
        if var16 == 0 and var4 == 2 or var16 == 2 and var4 == 2
            puts "\nSaan follows you back, looking happy."
            sleep(3)
            mainMenu2
        end
        if var16 == 0 and var4 == 0 or var16 == 0 and var4 == 3
            puts "\nSaan follows you back."
            sleep(3)
            mainMenu2
        end
        if var16 == 1 and var4 == 1
            puts "\nSaan reluctantly takes the flower. He seems confused."
            sleep(3)
            flowertoSaan
            saan
        end
        if var16 == 1 and var4 == 2
            puts "\nSaan looks borderline embarassed, you've made him blush so much."
            sleep(3)
            puts "He happily takes the flower."
            sleep(2)
            flowertoSaan
            saan
        end
        if var16 == 1 and var4 == 3 or var16 == 1 and var4 == 0
            puts "\nSaan thanks you for the flower."
            sleep(3)
            flowertoSaan
            saan
        end
        if var16 == 3 or var4 == 1
            puts "\nSaan follows you back with the flower."
            sleep(3)
            mainMenu2
        end
        if var16 == 3 or var4 == 2
            puts "\nSaan follows you back closely, happily admiring the flower you gave him."
            sleep(3)
            mainMenu2
        end
        if var16 == 3 or var4 == 3
            puts "\nSaan follows you, admiring his flower."
            sleep(3)
            mainMenu2
        end
    end
    if choose == 4
        if var4 < 1
            puts "\nYou walk back without talking...how rude."
            sleep(2)
            rudetoSaan
            mainMenu2
        end
        if var4 == 2
            puts "\nYou head back, Saan still blushing."
            sleep(2)
            mainMenu2
        end
    end
end

def rudetoSaan
    line_ext = 3
    state_ext = 1
    saveWrite(line_ext, state_ext)
    return
end

def flirtytoSaan
    line_ext = 3
    state_ext = 2
    saveWrite(line_ext, state_ext)
    return
end

def neutraltoSaan
    line_ext = 3
    state_ext = 3
    saveWrite(line_ext, state_ext)
    return
end

def flowertoSaan
    line_ext = 15
    state_ext = 3
    saveWrite(line_ext, state_ext)
    return
end