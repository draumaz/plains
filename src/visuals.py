from tools import version, clear, sleep, array_reader, os_check

class headers:
    def splash_header():
        print("\n===========THE PLAINS=============")
        print("=====MADE BY DRAUMAZ IN 2021======")
        print("=======WRITTEN IN PYTHON!=========")
        print("==CHARACTER DESIGN BY BRYCE CANO==\n")

    def version_header():
        print("\nThe Plains", version(), "\n", end="")

    def exit_header():
        clear()
        print("\nThanks for playing my game!")
        sleep(0.5)
        print("\nKeep up with development at ", end="")
        array_reader("https://github.com/draumaz/plains-reboot", 0.004)
        print(".\n")
        sleep(0.05)
        if os_check() == 1:
            input("Press ENTER to continue: ")
