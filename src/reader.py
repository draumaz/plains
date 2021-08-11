from time import sleep

class readers:
    def array_reader(string, ms):
        for i in string:
            print(i, end="", flush=True)
            sleep(ms)
        return ""
    def option_reader(*args):
        for i in range(2, len(args)):
            print(args[i] + " [" + str(i-1) + "]")
        print()