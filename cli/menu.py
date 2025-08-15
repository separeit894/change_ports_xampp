from .commands import *

from config import Colors
from config import Escape_Sequences

import traceback
import sys
import ctypes
import webbrowser

class CLI:
    def create_console(self):
        ctypes.windll.kernel32.AllocConsole()
        sys.stdout = open("CONOUT$", "w", buffering=1)  
        sys.stderr = open("CONOUT$", "w", buffering=1)
        sys.stdin = open("CONIN$", "r")

    def mode_console(self):
        self.create_console()
        try:
            while True:
                list_text_main_menu = [
                    "Created by separeit894", 
                    "Github","Main Page CPX Github", 
                    "CPX releases here!", 
                    "Change port Apache",
                    "Change port ApacheSSL", 
                    "Change port MySQL", 
                    "Edit xampp control.ini. Administrator rights required!",
                    "Recover files"
                    ]
                
                for i, line in enumerate(list_text_main_menu):
                    if i == 0:
                        print(line)
                        continue
                    elif i == 3:
                        print(f"{i}. {line}{Escape_Sequences.double_new_line}")
                        continue
                    print(f"{i}. {line}")
                

                choise = int(input("Select a menu item ( 1 - 8 ): "))
                if choise == 1:
                    url = "https://github.com/separeit894"
                    webbrowser.open(url)
                elif choise == 2:
                    url = "https://github.com/separeit894/change_ports_xampp"
                    webbrowser.open(url)
                elif choise == 3:
                    url = "https://github.com/separeit894/change_ports_xampp/releases"
                    webbrowser.open(url)
                elif choise == 4:
                    apache_mode_console()
                elif choise == 5:
                    apachessl_mode_console()
                elif choise == 6:
                    mysql_mode_console()
                elif choise == 7:
                    xampp_control_mode_console()
                elif choise == 8:
                    file_recovery_mode_console()
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
