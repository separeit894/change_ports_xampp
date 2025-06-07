from source import gui
from source import console
import sys
import subprocess



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--console":
            console()
        else:
            gui()
    else:
        subprocess.run(["cmd", "/c", "echo 'Для того чтобы узнать о программе --help'"])
        gui()