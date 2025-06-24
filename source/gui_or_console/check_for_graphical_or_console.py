import sys
import importlib


def mode_console_or_gui():
    if len(sys.argv) > 1:
        if "--console" in sys.argv:
            console = True
            messagebox = None
    else:
        console = None
        messagebox = importlib.import_module("tkinter.messagebox")

    return console, messagebox


if __name__ == "__main__":
    mode_console_or_gui()
