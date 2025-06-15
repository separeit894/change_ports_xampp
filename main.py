from source import gui
from source import console

import sys
import subprocess
import ctypes
console_argv = False
def create_console():

    ctypes.windll.kernel32.AllocConsole()
    sys.stdout = open('CONOUT$', 'w')  # Перенаправляем стандартный вывод в консоль
    sys.stderr = open('CONOUT$', 'w')
    sys.stdin = open('CONIN$', 'r')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if "--console" in sys.argv:
            console_argv = True
            create_console()
            console()
        else:
            gui()
    else:
        subprocess.run(["cmd", "/c", "echo 'Для того чтобы узнать о программе --help'"])
        gui()