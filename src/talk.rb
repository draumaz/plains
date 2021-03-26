require './handy'
require './mm2'

def talk
  begin
    var6 = saveRead[5]
    var7 = saveRead[6]
    var8 = saveRead[7]
    screenClear
    versionHeader
    invDisplay
    if var6 == 0 or var7 == 0 or var8 == 1
      puts "\nYour friends are relieved that you're alright."
    end
    if var6 == 1 and var8 == 0
      puts "\nYour friends look at you, horrified."
    end
    if var7 == 1 and var6 == 0 and var8 == 0
      puts "\nThey seem worried."
    end
    if var6 == 0 or var8 == 1
      puts "\nCHAT"
    end
    if var6 == 1 and var8 == 0 or var7 == 1
      puts "\nWHAT'S WITH THAT LOOK? [1]"
    end
    puts "STARE [2]"
    puts "BACK [3]"
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
      if var6 == 1 and var8 == 0
        talksel1C
      else
        talkSel1
      end
    end
    if choose == 2
      talkSel2
    end
    if choose == 3
      if var6 == 1
        mainMenu2
      end
      if var6 == 0
        puts "\nYou tell your friends you need a minute."
        sleep(2)
        mainMenu2
      end
      mainMenu2
    end
    if choose > 3 or choose < 1
      inpErHandler
      talk
    end
  rescue ArgumentError
    inpErrorHandler
    talk
  end
end

def talkSel1
  begin
    screenClear
    versionHeader
    invDisplay
    var3 = saveRead[2]
    var7 = saveRead[6]
    var8 = saveRead[7]
    if var3 == 1
      if var7 == 0 or var8 == 1
        puts "\nYour friends mentioned that your scanner had painful latency."
        sleep(4)
        talk
      end
      if var7 == 1 and var8 == 0
        talksel1B
      end
    end
  if var3 == 0
    talksel1A
  end
  rescue ArgumentError
    inpErHandler
    talkSel1
  end
end

def talkSel1A
  begin
    screenClear
    versionHeader
    invDisplay
    puts "\nYour friends ask you why you didn't use any of your tools to contact them."
    puts "\nUH... [1]"
    puts "BACK [2]"
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
      puts "\nYour friends tell you not to worry...but to do it next time."
      sleep(4)
      talk
    end
    if choose == 2
      puts "\nYou pretend you're getting a call on your phone to avoid this awkward conversation."
      sleep(4)
      talk
    end
    if choose > 2 or choose < 1
      inpErHandler
      talkSel1A
    end
  rescue ArgumentError
    inpErHandler
    talkSel1A
  end
end

def talkSel1B
  begin
    puts "\nYour friends ask you a question."
    sleep(2)
    puts "Liam, are you alright?"
    sleep(2)
    puts "EXPLAIN [1]"
    puts "BACK [2]"
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
      line_ext = 7
      state_ext = 1
      saveWrite(line_ext, state_ext)
      puts "\nYou explain to them that you're just feeling off."
      sleep(3)
      puts "\n:)"
      sleep(0.04)
      talk
    end
    if choose == 2
      puts "\nThey wouldn't get it."
      sleep(4)
      talk
    end
    if choose > 2 or choose < 1
      inpErHandler
      talkSel1B
    end
  rescue ArgumentError
    inpErHandler
    talkSel1B
  end
end

def talkSel1C
  begin
    var6 = saveRead[5]
    screenClear
    versionHeader
    invDisplay
    puts "\nYour friends barely stammer out a question."
    sleep(2)
    puts "Liam, why are you covered in blood?"
    sleep(3)
    puts "\nEXPLAIN [1]"
    puts "RUN AWAY [2]"
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
      puts "\nYou tell your friends it was self-defense."
      sleep(2)
      puts "They seem to understand."
      sleep(4)
      talk
    end
    if choose == 2
      puts "\nYou can't face them."
      sleep(2)
      mainMenu2
    end
    if choose > 2 or choose < 1
      inpErHandler
      talkSel1C
    end
  rescue ArgumentError
    inpErHandler
    talkSel1C
  end
end

def talkSel2
  begin
    screenClear
    versionHeader
    invDisplay
    puts "\nYou just...stare at them. They look bewildered."
    puts "\nKEEP STARING [1]"
    puts "GO BACK [2]"
    print "\nACTION >> "
    choose = Integer(gets.chomp)
    if choose == 1
      puts "\nYour unblinking eyes eventually cause them to wonder if there's something seriously wrong with you."
      sleep(4)
      talk
    end
    if choose == 2
      puts "\nYeah, this is pretty bizarre."
      sleep(1.5)
      talk
    end
    if choose > 2 or choose < 1
      inpErHandler
      talkSel2
    end
  rescue ArgumentError
    inpErHandler
    talkSel2
  end
end
