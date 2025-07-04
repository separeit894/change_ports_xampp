from .functional_console import *
import traceback

from ..config import Colors
from ..config import Escape_Sequences

from .update_cpx import Update
import sys
import ctypes

class CLI:
    def __init__(self, console, messagebox):
        self.console = console
        self.messagebox = messagebox
        
    def create_console(self):
        ctypes.windll.kernel32.AllocConsole()
        sys.stdout = open("CONOUT$", "w")  
        sys.stderr = open("CONOUT$", "w")
        sys.stdin = open("CONIN$", "r")

    def mode_console(self):
        self.create_console()
        try:
            while True:
                print("1. Change port Apache ")
                print("2. Change port ApacheSSL ")
                print("3. Change port MySQL ")
                print("4. Edit xampp control.ini. Administrator rights required! ")
                print("5. Recover files ")
                print("6. Проверить версию приложения")

                choise = int(input("Select a menu item ( 1 - 5 ): "))

                if choise == 1:
                    apache_mode_console(self.console, self.messagebox)
                elif choise == 2:
                    apachessl_mode_console(self.console, self.messagebox)
                elif choise == 3:
                    mysql_mode_console(self.console, self.messagebox)
                elif choise == 4:
                    xampp_control_mode_console(self.console, self.messagebox)
                elif choise == 5:
                    file_recovery_mode_console(self.console, self.messagebox)
                elif choise == 6:
                    update = Update(self.console, self.messagebox)
                    if update.checking_for_update():
                        update.update_console()
                else:
                    print(
                        f"{Escape_Sequences.new_line}{Colors.RED}You have selected an incorrect number!{Colors.RESET}{Escape_Sequences.new_line}"
                    )

        except BaseException as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.double_new_line}"
            )
    
    def run_app(self):
        self.mode_console()

if __name__ == "__main__":
    CLI().run_app()
