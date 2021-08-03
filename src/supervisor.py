import tools
import visuals
import save
import sys

def superblade():
    tools.clear()
    save.exists()
    visuals.header()
    print("PLAY [1]\nRESET [2]\nQUIT [3]\n")
    i = tools.user_input(1, 3)
    if i == 1:
        pass
    elif i == 2:
        if tools.reset() == 0:
            superblade()
    elif i == 3:
        visuals.exit_header()
        sys.exit()