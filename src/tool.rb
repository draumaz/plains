require './handy'
require './mm1'

def tool
    begin
        var3 = saveRead[2]
        screenClear
        versionHeader
        invDisplay
        puts "\nYou're completely stranded. Might as well use your tools."
        puts "\nPHONE [1]"
        puts "RADAR [2]"
        puts "SCANNER [3]"
        puts "BACK [4]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            toolSel1
        end
        if choose == 2
            toolSel2
        end
        if choose == 3
            toolSel3
        end
        if choose == 4
            if var3 == 0
                puts "\nThese tools probably wouldn't work, anyways."
                sleep(3)
                mainMenu1
            end
            if var3 == 1
                puts "\nWith your friends contacted, you've got some time to kill."
                sleep(3)
                mainMenu1
            end
        end
        if choose > 4 or choose < 1
            inpErHandler
            tool
        end
    rescue ArgumentError
        inpErHandler
        tool
    end
end

def toolSel1
    begin
        var3 = saveRead[2]
        screenClear
        versionHeader
        invDisplay
        puts "\nYou pull out your phone. Surprisingly, the cell service is quite good."
        puts "\nCALL A FRIEND [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var3 != 1
                line_ext = 0
                state_ext = 1
                saveWrite(line_ext, state_ext)
                line_ext = 2
                state_ext = 1
                saveWrite(line_ext, state_ext)
                puts "\nYou get ahold of your friends, and they tell you they're coming!"
                sleep(4)
                mainMenu1()
            end
            if var3 == 1
                puts "\nYou've already made contact."
            end
        end
        if choose == 2
            tool
        end
        if choose > 2 or choose < 1
            inpErHandler
            toolSel1
        end
    rescue ArgumentError
        inpErHandler
        toolSel1
    end
end

def toolSel2
    begin
        var3 = saveRead[2]
        screenClear
        versionHeader
        invDisplay
        if var3 == 3
            puts "\nDoesn't work :("
            sleep(2)
            tool
        end
        puts "\nYour radar is showing some signs of life, but nothing extraordinary."
        puts "\nSCAN [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var3 == 3
                puts "\nYou've already tried using this tool."
                sleep(2)
                tool
            end
            if var3 != 3
                line_ext = 2
                state_ext = 3
                saveWrite(line_ext, state_ext)
                puts "\nYou try scanning around...it just shuts off."
                sleep(2)
                tool
            end
        end
        if choose == 2
            tool
        end
        if choose > 2 or choose < 1
            inpErHandler
            toolSel2
        end
    rescue ArgumentError
        inpErHandler
        toolSel2
    end
end

def toolSel3
    begin
        var3 = saveRead[2]
        screenClear
        versionHeader
        invDisplay
        if var3 != 4
            puts "\nYour scanner seems to be working just fine."
        end
        if var3 == 4
            puts "\nThis machine barely functions, and it's a liar on top."
        end
        puts "\nGET SIGNAL [1]"
        puts "BACK [2]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var3 == 4
                puts "\nThis machine has caused you enough trouble..."
                sleep(3)
                tool
            end
            if var3 != 4
                line_ext = 2
                state_ext = 4
                saveWrite(line_ext, state_ext)
                puts "\nSeems like this dastardly machine has played you for a fool,"
                puts "seems like it doesn't work after all..."
                sleep(4)
                tool
            end
        end
        if choose == 2
            tool
        end
        if choose > 2 or choose < 1
            inpErHandler
            toolSel3
        end
    rescue ArgumentError
        inpErHandler
        toolSel3
    end
end