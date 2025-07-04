from source import GUI
from source import CLI

import sys
import importlib


class App:
    def __init__(self, console, messagebox):
        self.console = console
        self.messagebox = messagebox
        
        if console:
            CLI(self.console, self.messagebox).run_app()
        else:
            GUI(self.console, self.messagebox).run_app()
        
    def print_console_and_messagebox(self):
        print(f"Console: {self.console}\nMessagebox: {self.messagebox}\n")


def main():
    console, messagebox = None, None
    if len(sys.argv) > 1:
        if "--console" in sys.argv:
            console = True
            messagebox = False
        else:
            console = False
            messagebox = importlib.import_module("tkinter.messagebox")
    else:
        console = False
        messagebox = importlib.import_module("tkinter.messagebox")
        
    return console, messagebox


if __name__ == "__main__":
    console, messagebox = main()
    app = App(console, messagebox)
