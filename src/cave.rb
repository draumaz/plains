require './handy'
require './mm1'

def cave
    begin
        screenClear
        versionHeader
        invDisplay
        puts "\nYou make your way towards a deep, dark cave."
        puts "You can barely see anything at all.\n\n"
        puts "CONTINUE [1]"
        puts "LOOK AROUND [2]"
        puts "LISTEN [3]"
        puts "BACK [4]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            caveSel1
        end
        if choose == 2
            caveSel2
        end
        if choose == 3
            caveSel3
        end
        if choose == 4
            puts "\nSeems pretty forboding...best to head back."
            sleep(2)
            mainMenu1
        end
    rescue ArgumentError
        inpErHandler
        cave
    end
end

def caveSel1
    begin
        var15 = saveRead[14]
        screenClear
        versionHeader
        invDisplay
        if var15 == 0
            puts "\nYou continue deeper down the cave. You can almost see a small box."
            puts "\nOPEN [1]"
        end
        if var15 == 1
            puts "\nJust a dingy old cave."
            puts "\nPUT KNIFE BACK [1]"
        end
        if var15 == 2
            puts "\nYou continue back down. There's that box with the knife."
            puts "\nTAKE BACK [1]"
        end
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var15 == 0
                line_ext = 14
                state_ext = 1
                saveWrite(line_ext, state_ext)
                puts "\nYou open the box and find a knife laying inside. You take it."
                sleep(3)
                caveSel1
            end
            if var15 == 1
                line_ext = 14
                state_ext = 2
                saveWrite(line_ext, state_ext)
                puts "\nYou open the box, and put the knife back."
                sleep(3)
                caveSel1
            end
            if var15 == 2
                line_ext = 14
                state_ext = 1
                saveWrite(line_ext, state_ext)
                puts "\nYou open the box, and take the knife back."
                sleep(3)
                caveSel1
            end
        end
        if choose == 2
            puts "\nContinuing in a cave this dark, it's just asking for trouble."
            sleep(3)
            cave
        end
        if choose > 2 or choose < 1
            inpErHandler
            caveSel1
        end
    rescue ArgumentError
        inpErHandler
        caveSel1
    end
end

def caveSel2
    begin
        screenClear
        versionHeader
        invDisplay
        puts "\nUp against the entrance is a sign. It's written in a strange system."
        puts "\nDECIPHER [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            puts "\nYou pull out your phone, and attempt to translate the symbols."
            sleep(4)
            puts '...looks like it says "Abandon all hope, ye who enter here".'
            sleep(4)
            puts "Better safe than sorry."
            sleep(2)
            cave
        end
        if choose == 2
            puts "\nToo much work, anyways."
            sleep(2)
            cave
        end
        if choose > 2 or choose < 1
            inpErHandler
            caveSel2
        end
    rescue ArgumentError
        inpErHandler
        caveSel2
    end
end

def caveSel3
    begin
        screenClear
        versionHeader
        invDisplay
        puts "\nYou focus your listening on the cave. You can hear a faint" 
        puts "rumbling noise coming from within."
        puts "\nDISCERN [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            puts "\nYou listen as hard as you can, in an attempt to discern words."
            sleep(4)
            puts "...that's certainly not any language you know."
            sleep(2)
            cave
        end
        if choose == 2
            puts "Probably just nature."
            sleep(2)
            cave
        end
        if choose > 2 or choose < 1
            inpErHandler
            caveSel3
        end
    rescue ArgumentError
        inpErHandler
        caveSel3
    end
end