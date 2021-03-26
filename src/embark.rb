require './handy'
require './mm1'

def embark
    begin
        var6 = saveRead[5]
        var8 = saveRead[7]
        screenClear
        versionHeader
        invDisplay
        if var6 == 1 and var8 == 0
            puts "\nIgnoring your friends, you rush into their ship and lock the doors behind."
        end
        if var6 == 0 or var8 == 1
            puts "\nYou walk to your friends' ship. They follow along shortly thereafter."
        end
        puts "\nLOOK AROUND [1]"
        puts "SET OFF [2]"
        puts "BACK [3]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var6 == 0
                puts "\nThis ship is gorgeous. Complex, shiny white metal covers the interior."
                sleep(3)
                embark
            end
            if var6 == 1
                puts "\nThe ship doesn't matter. It's a means to an end."
                sleep(3)
                embark
            end
        end
        if choose == 2
            if var6 == 1 and var8 == 0
                embarkEvil
            else
                embarkNeut
            end
        end
        if choose == 3
            puts "\nYou decide against leaving just quite yet."
            sleep(2)
            mainMenu2
        end
        if choose > 3 or choose < 1
            inpErHandler
            embark
        end
    rescue ArgumentError
        inpErHandler
        embark
    end
end

def embarkNeut
    begin
        puts "\nSaan mentions how beautiful this planet is."
        sleep(2)
        puts "Seems like they want to stick around for a bit."
        sleep(2)
        puts "\nLEAVE [1]"
        puts "STAY [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            line_ext = 13
            state_ext = 2
            saveWrite(line_ext, state_ext)
            puts "\nYou decide to depart anyways, and your journey comes to an end."
            sleep(3)
            screenClear
            puts "\nTHANK YOU FOR PLAYING!"
            sleep(2)
            quitHandler
        end
        if choose == 2
            line_ext = 1
            state_ext = 2
            saveWrite(line_ext, state_ext)
            puts "\nYou and your friends disembark, and lock up the ship."
            sleep(2)
            puts "Smells like adventure."
            sleep(3)
            mainMenu3
        end
        if choose > 2 or choose < 1
            inpErHandler
            embarkNeut
        end
    rescue ArgumentError
        inpErHandler
        embarkNeut
    end
end

def embarkEvil
    line_ext = 8
    state_ext = 1
    saveWrite(line_ext, state_ext)
    puts "\nBlood still dripping from you, you take off in the ship, leaving your friends behind."
    sleep(6)
    screenClear
    sleep(4)
    puts "EVIL"
    sleep(0.05)
    screenClear
    quitHandler
end
