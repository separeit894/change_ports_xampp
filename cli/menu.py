from .commands import *

from config import (
    Escape_Sequences,
    Colors
)

from datetime import datetime

import traceback
import os
import logging
import webbrowser



class CLI:
    def mode_console(self):
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
                    "Recover files",
                    "Parametrs"
                    ]
                
                for i, line in enumerate(list_text_main_menu):
                    if i == 0:
                        print(line)
                        continue
                    elif i == 3:
                        print(f"{i}. {line}{Escape_Sequences.double_new_line}")
                        continue
                    print(f"{i}. {line}")
                

                choise = int(input(f"Select a menu item ( 1 - {len(list_text_main_menu) - 1} ): "))
                if choise == 1:
                    url = "https://github.com/separeit894"
                    webbrowser.open(url)
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Following the link : {url}")
                elif choise == 2:
                    url = "https://github.com/separeit894/change_ports_xampp"
                    webbrowser.open(url)
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Following the link : {url}")
                elif choise == 3:
                    url = "https://github.com/separeit894/change_ports_xampp/releases"
                    webbrowser.open(url)
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Following the link : {url}")
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
                elif choise == 9:
                    change_settings_mode_console()
                    # encoding = input("Enter encoding who you was use: ")
                    # from config import set_encoding
                    # set_encoding(encoding)
                else:
                    print(
                        f"{Escape_Sequences.new_line}{Colors.RED}You have selected an incorrect number!{Colors.RESET}{Escape_Sequences.new_line}"
                    )
                    logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : choise : {choise}")

        except KeyboardInterrupt:
            print("\nClose Program with help ctrl+c")
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Exception KeyboardInterrupt")
            
        except Exception:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.BOLD}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.double_new_line}"
            )
            logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Error\n{tb}")
            
    
    def run_app(self):
        self.mode_console()
        

if __name__ == "__main__":
    CLI().run_app()
