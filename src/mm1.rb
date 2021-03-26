require './handy'
require './cave'
require './hill'
require './tool'
require './mm2'

def mainMenu1
    begin
        system('cls||clear')
        var1 = saveRead[0]
        var6 = saveRead[5]
        versionHeader
        invDisplay
        puts "\nYou are Liam. An astronaut by trade, you took a bad turn on the Space Belt," 
        puts "and landed on a strange planet. You awaken, laying in a field of grass."
        puts "You see hills, a cave, and strange flora all around you.\n\n"
        puts "HILL [1]"
        puts "CAVE [2]"
        puts "TOOL [3]"
        if var1 == 1
            puts "LOOK AT SKY [4] <--"
            puts "QUIT [5]"
        end
        if var1 == 0
            puts "QUIT [4]"
        end
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            hill
        end
        if choose == 2
            cave
        end
        if choose == 3
            tool
        end
        if choose == 4
            if var1 == 0
                quitHandler
            end
            if var1 == 1
                mainMenu1End
            end
        end
        if choose == 5
            if var1 == 0
                inpErHandler
                mainMenu1
            end
            if var1 == 1
                quitHandler
            end
        end
        if choose > 4 or choose < 1
            inpErHandler
            mainMenu1
        end
    rescue ArgumentError
        inpErHandler
        mainMenu1
    end
end

def mainMenu1End
    begin
        screenClear
        versionHeader
        invDisplay
        puts "\nThe strange noise grows louder and louder until it reaches"
        puts "a sudden stop. You look up, and see a massive black ship floating."
        puts "\nLOOK [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            line_ext = 1
            state_ext = 1
            saveWrite(line_ext, state_ext)
            puts "\nThe shape descends, and you make it out - it's a spaceship!"
            sleep(2)
            puts "Your friends slowly walk out."
            sleep(2)
            mainMenu2
        end
        if choose == 2
            mainMenu1
        end
        if choose > 2 or choose < 1
            inpErHandler
            mainMenu1End
        end
    rescue ArgumentError
        inpErHandler
        mainMenu1End
    end
end
