import traceback
import logging
import os

from datetime import datetime

from config import (
    Escape_Sequences,
    Colors
)

def change_settings_mode_console() -> None:
    try:
        while True:
            list_text_settings = [
                "Change Encoding",
                "Change Path Apache",
                "Change Path ApacheSSL",
                "Change Path MySQL",
                "Change Path PhpMyAdmin Config",
                "Change Path Xampp Control INI",
                "Go back to the main menu"
            ]
            
            for i, line in enumerate(list_text_settings):
                print(f"{i}. {line}")
                
            choise = int(input(f"Select a menu item ( 0 - {len(list_text_settings) - 1} ): "))
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : choise : {choise}")
            
            if choise == 0:
                from config import (
                    get_encoding, 
                    set_encoding
                )
                print(f"Current Encoding : {get_encoding()}")
                use_encoding = str(input("Enter new encoding : "))
                set_encoding(use_encoding)
            elif choise == 1:
                from config import (
                    get_file_path_Apache,
                    set_file_path_Apache
                )
                print(f"Current Path Apache : {get_file_path_Apache()}")
                use_new_path_apache = str(input("Enter new path Apache : "))
                set_file_path_Apache(use_new_path_apache)
            elif choise == 2:
                from config import (
                    get_file_path_ApacheSSL,
                    set_file_path_ApacheSSL
                )
                print(f"Current Path ApacheSSL : {get_file_path_ApacheSSL()}")
                use_new_path_ApacheSSL = str(input("Enter new path ApacheSSL : "))
                set_file_path_ApacheSSL(use_new_path_ApacheSSL)
            elif choise == 3:
                from config import (
                    get_file_path_MySQLINI,
                    set_file_path_MySQLIni
                )
                
                print(f"Current Path MySQL INI : {get_file_path_MySQLINI()}")
                use_new_path_MySQL_INI = str(input("Enter new path MySQL INI : "))
                set_file_path_MySQLIni(use_new_path_MySQL_INI)
            elif choise == 4:
                from config import (
                    get_file_path_PhpMyAdminConfig,
                    set_file_path_PhpMyAdminConfig
                )
                
                print(f"Current Path PhpMyAdmin Config : {get_file_path_PhpMyAdminConfig()}")
                use_new_path_PhpMyAdminConfig = str(input("Enter new path PhpMyAdmin Config : "))
                set_file_path_PhpMyAdminConfig(use_new_path_PhpMyAdminConfig)
            elif choise == 5:
                from config import (
                    get_file_path_xampp_control_ini,
                    set_file_path_xampp_control_ini
                )
                
                print(f"Current Path Xampp Control INI : {get_file_path_xampp_control_ini()}")
                use_new_path_xampp_control_ini = str(input("Enter new path xampp control ini : "))
                set_file_path_xampp_control_ini(use_new_path_xampp_control_ini)
            elif choise == 6:
                print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}Return to main menu{Colors.RESET}{Escape_Sequences.new_line}")
                break
            else:
                print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}There is no such number in this list! Сhose Again{Colors.RESET}{Escape_Sequences.new_line}")
                continue
            
    except Exception:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.BOLD}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : An error has been detected! : \n{tb}")
    
if __name__ == "__main__":
    change_settings_mode_console()