from source import mode_gui
from source import mode_console

import sys
import ctypes


def create_console():
    ctypes.windll.kernel32.AllocConsole()
    sys.stdout = open("CONOUT$", "w")  # Перенаправляем стандартный вывод в консоль
    sys.stderr = open("CONOUT$", "w")
    sys.stdin = open("CONIN$", "r")


def main():
    if len(sys.argv) > 1:
        if "--console" in sys.argv:
            create_console()
            mode_console()
        else:
            mode_gui()
    else:
        mode_gui()


if __name__ == "__main__":
    main()
