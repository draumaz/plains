require './handy'
require './saan'
require './talk'
require './embark'

def mainMenu2
    begin
        var1 = saveRead[0]
        var6 = saveRead[5]
        screenClear
        versionHeader
        invDisplay
        puts "\nYour friends are standing a little ways from you."
        puts "\nALL FRIENDS [1]"
        puts "SAAN [2]"
        puts "EMBARK [3]"
        puts "QUIT [4]"
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            talk
        end
        if choose == 2
            saan
        end
        if choose == 3
            embark
        end
        if choose == 4
            quitHandler
        end
        if choose > 4 or choose < 1
            inpErHandler
            mainMenu2
        end
    rescue ArgumentError
        inpErHandler
        mainMenu2
    end
end
