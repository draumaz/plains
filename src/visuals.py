import tools

def header():
    print("\n==THE PLAINS======================")
    print("==MADE BY DRAUMAZ IN 2021=========")
    print("==WRITTEN IN PYTHON!==============")
    print("==CHARACTER DESIGN BY BRYCE CANO==\n")

def exit_header():
    tools.clear()
    print("\nThanks for playing my game!")
    tools.snooze(0.5)
    print("\nKeep up with development at ", end="")
    tools.array_reader("https://github.com/draumaz/plains-reboot", 0.004)
    print(".\n")
    tools.snooze(0.05)
    if tools.os_check() == 1:
        input("Press ENTER to continue: ")
