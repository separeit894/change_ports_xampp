from .functional_console import *
import traceback

from ..color_output import Colors
from ..config import Escape_Sequences

from .update_cpx import checking_for_update
from .update_cpx import update_console




def mode_console():
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
                apache_mode_console()
            elif choise == 2:
                apachessl_mode_console()
            elif choise == 3:
                mysql_mode_console()
            elif choise == 4:
                xampp_control_mode_console()
            elif choise == 5:
                file_recovery_mode_console()
            elif choise == 6:
                if checking_for_update():
                    update_console()
            else:
                print(
                    f"{Escape_Sequences.new_line}{Colors.RED}You have selected an incorrect number!{Colors.RESET}{Escape_Sequences.new_line}"
                )

    except BaseException as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.double_new_line}"
        )


if __name__ == "__main__":
    mode_console()
