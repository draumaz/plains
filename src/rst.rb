require './handy'

def reset
    begin
        var9 = saveRead[8]
        var10 = saveRead[9]
        if var9 == 0
            screenClear
            puts "\nDoing this will reset everything. Are you sure?"
            puts "\nRESET [1]"
            puts "BACK [2]"
        end
        if var9 == 1
            puts "\nRESET [1]"
        end
        print "\nACTION >> "
        choose = Integer(gets.chomp)
        if choose == 1
            if var9 == 1
                if var10 == 0
                    line_ext = 9
                    state_ext = 1
                    saveWrite(line_ext, state_ext)
                end
                puts "\nReset failed."
                sleep(1)
                quitHandler
            end
            if var9 != 1
                resetProc
                puts "\nReset."
                sleep(0.25)
                return
            end
        end
        if choose == 2
            return
        end
        if choose == 420
            easterEgg
            reset
        end
        if choose > 2 and choose < 420 or choose < 1 or choose > 420
            inpErHandler
            reset
        end
    rescue ArgumentError
        inpErHandler
        reset
    end
end

def resetProc
    line_ext = 0
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 1
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 2
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 3
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 4
    state_ext = 1
    saveWrite(line_ext, state_ext)
    line_ext = 5
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 7
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 13
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 14
    state_ext = 0
    saveWrite(line_ext, state_ext)
    line_ext = 15
    state_ext = 0
    saveWrite(line_ext, state_ext)
    return
end