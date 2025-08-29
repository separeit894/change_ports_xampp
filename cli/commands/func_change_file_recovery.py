import traceback
import os
import logging

from core import run_as_admin
from core import is_admin
from core import Recovery_Files
from config import Escape_Sequences
from config import Colors

from datetime import datetime

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)


def file_recovery_mode_console() -> None:
    recovery_files = Recovery_Files()
    if is_admin():
        try:
            while True:
                list_text_file_recovery = [
                    "Restore Apache file:",
                    "Restore ApacheSSL file:",
                    "Restore MySQL files:",
                    "Restore xampp-control.ini file",
                    "Return to the main menu"
                ]
                for i, line in enumerate(list_text_file_recovery):
                    print(f"{i}. {line}")

                choise = int(input("Select a menu item (0 - 4): "))
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : choise : {choise}")
                if choise == 0:
                    result = recovery_files.file_recovery_apache()
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}File Apache overwritten{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : File Apache overwritten")
                elif choise == 1:
                    result = recovery_files.file_recovery_apachessl()
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}File ApacheSSL overwritten{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : File ApacheSSL overwritten")
                elif choise == 2:
                    result = recovery_files.file_recovery_mysql()
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}Files MySQL overwrittens{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Files MySQL overwritten")
                elif choise == 3:
                    result = recovery_files.file_recovery_xampp_control()
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}File xampp-control overwritten{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : File xampp-control overwritten")
                elif choise == 4:
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Returned to the main menu")
                    break

        except Exception as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )
            logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : An error has been detected! : \n{tb}")
            
    else:
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Restarting the program with administrator rights")
        run_as_admin()


if __name__ == "__main__":
    file_recovery_mode_console()
