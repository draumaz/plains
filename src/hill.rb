require './handy'
require './mm1'

def hill
    begin
        var1 = saveRead[0]
        var6 = saveRead[5]
        var12 = saveRead[11]
        var16 = saveRead[15]
        screenClear
        versionHeader
        invDisplay
        if var6 == 0 and var1 == 0
            puts "\nThat hill looks pretty odd. Pokes out of the landscape in a strange way."
        end
        if var6 == 0 and var1 == 1
            puts "\nHaving stood there, you hear a strange noise in the distance."
            puts "Perhaps going back will show you the answer?"
        end
        if var6 == 1 and var1 == 0
            puts "\nYou should stand still."
        end
        if var6 == 1 and var1 == 1
            puts "\nThey're coming. Go back."
        end
        if var6 == 0 and var12 == 0 and var16 != 2
            puts "In the distance, you can see a lizard-like creature moving around."
            puts "\nGO TOWARDS HIM [1]"
        end
        if var16 == 2
            puts "You can see the lizard sitting down, drinking a soda."
            puts "\nVISIT HIM [1]"
        end
        if var12 == 1
            puts ""
        end
        if var6 == 1
            puts ""
            puts "GO FORWARDS [1]"
        end
        if var1 == 0
            puts "STAND STILL [2]"
        end
        puts "TAKE A BREAK [3]"
        puts "BACK [4]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            hillSel1
        end
        if choose == 2
            if var1 == 0
                hillSel2
            end
            if var1 == 1
                inpErHandler
                hill
            end
        end
        if choose == 3
            hillSel3
        end
        if choose == 4
            if var6 == 0
                puts "\nBest to head back."
                sleep(2)
                mainMenu1
            end
            if var6 == 1
                mainMenu1
            end
        end
        if choose > 4 or choose < 1
            inpErHandler
            hill
        end
    rescue ArgumentError
        inpErHandler
        hill
    end
end

def hillSel1
    begin
        var5 = saveRead[4]
        var6 = saveRead[5]
        var7 = saveRead[6]
        var15 = saveRead[14]
        var16 = saveRead[15]
        screenClear
        versionHeader
        invDisplay
        if var6 == 1
            puts "\nSilence fills the air."
            if var16 == 1
                puts "\nFLOWER [1]"
            end
            if var16 == 0
                puts ""
            end
            if var16 == 3
                puts ""
            end
            puts "BACK [2]"
            print "\nACTION >> "
            choose = Integer(gets.chomp)
            if choose == 1
                if var16 != 1
                    inpErHandler
                    hillSel1
                end
                if var16 == 1
                    line_ext = 15
                    state_ext = 3
                    saveWrite(line_ext, state_ext)
                    puts "\nYou lay the flower next to his lifeless corpse."
                    sleep(5)
                    hill
                end
            end
            if choose == 2
                puts "two"
            end
            if choose > 2 or choose < 1
                inpErHandler
                hillSel1
            end
        end
        if var6 != 2 and var16 != 2
            puts "\nThe huge reptilian sees you, and approaches."
        end
        if var16 == 2
            puts "\nThe reptilian smiles at you."
        end
        if var7 == 0
            puts ""
        end
        if var7 == 1
            sleep(2)
            puts "Looks like he's having a sense of déjà vu.\n"
            sleep(3)
        end
        if var15 == 1
            puts "KILL [1]"
        end
        puts "TALK [2]"
        if var16 == 0
            puts "BACK [3]"
        end
        if var16 == 1
            puts "GIVE FLOWER [3]"
            puts "BACK [4]"
        end
        if var16 == 2
            puts "BACK [3]"
        end
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var15 != 1
                inpErHandler
                hillSel1
            end
            if var15 == 1
                line_ext = 5
                state_ext = 1
                saveWrite(line_ext, state_ext)
                line_ext = 6
                state_ext = 1
                saveWrite(line_ext, state_ext)
                puts "\nYou run up to the lizard and stab him to death."
                sleep(3)
                puts "Blood stains your outfit."
                sleep(5)
                hill
            end
            if var15 == 1 and var16 == 2
                puts "\nI genuinely don't have the heart to program a scenario for this."
                sleep(1)
                puts "Sorry!! -draumaz"
                sleep(1)
                hillSel1
            end
        end
        if choose == 2
            puts "two"
        end
        if choose == 3
            if var16 == 0
                puts "\nHe seems threatening... best to head back."
                sleep(3)
                hill
            end
            if var16 == 1
                line_ext = 15
                state_ext = 2
                saveWrite(line_ext, state_ext)
                puts "\nYou give the lizard the flower. He blushes at you."
                sleep(4)
                hillSel1
            end
        end
        if choose == 4
            puts "four"
        end
        if choose > 4 or choose < 1
            inpErHandler
            hillSel1
        end
    rescue ArgumentError
        inpErHandler
        hillSel1
    end
end

def hillSel2
    begin
        var6 = saveRead[5]
        screenClear
        versionHeader
        invDisplay
        if var6 == 0
            puts "\nDespite the massive mountains ahead, you decide to just keep still."
            sleep(1)
            puts "."
            sleep(1)
            puts "."
            sleep(1)
            puts "."
            sleep(2)
            puts "Seems like a waste of time."
            sleep(1)
            puts "\nKEEP STANDING [1]"
            puts "BACK [2]"
            print "\nACTION >> "
            choose = Integer(gets.chomp)
            if choose == 1
                line_ext = 0
                state_ext = 1
                saveWrite(line_ext, state_ext)
                sleep(3)
                puts "\nYou're completely zoned out."
                sleep(2)
                puts "...but..."
                sleep(1)
                puts "You hear something and head back to the start."
                sleep(3)
                mainMenu1
            end
            if choose == 2
                puts "You decide to return to a life of motion."
                sleep(2)
                hill()
            end
            if choose > 2 or choose < 1
                inpErHandler
                hillSel2
            end
        end
        if var6 == 1
            line_ext = 0
            state_ext = 1
            saveWrite(line_ext, state_ext)
            sleep(4)
            puts "\nYou've done something real bad, haven't you?"
            sleep(2)
            mainMenu1
        end
    rescue ArgumentError
        inpErHandler
        hillSel2
    end
end

def hillSel3
    begin
        var16 = saveRead[15]
        screenClear
        versionHeader
        invDisplay
        puts "\nYou sit down on the warm grass and get a look around."
        if var16 == 0
            puts "There's a beautiful flower rooted right next to you."
            puts "\nPICK [1]"
        end
        if var16 == 1
            puts ""
        end
        puts "LAY DOWN [2]"
        puts "BACK [3]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var16 == 1 or var16 == 2
                inpErHandler
                hillSel3
            end
            if var16 == 0
                line_ext = 15
                state_ext = 1
                saveWrite(line_ext, state_ext)
                puts "\nThe flower comes off the root without hesistation."
                puts "You put it in your pocket."
                sleep(2)
                hill
            end
        end
        if choose == 2
            puts "Laying here is truly refreshing. But you have work to do..."
            sleep(4)
            hill
        end
        if choose == 3
            hill
        end
        if choose > 3 or choose < 1
            inpErHandler
            hillSel3
        end
    rescue ArgumentError
        inpErHandler
        hillSel3
    end
end