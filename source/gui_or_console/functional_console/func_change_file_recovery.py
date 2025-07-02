import traceback

from ...change_ports import run_as_admin
from ...change_ports import is_admin
from ...change_ports import Recovery_Files
from ...config import Escape_Sequences
from ...config import Colors


def file_recovery_mode_console(console, messagebox):
    recovery_files = Recovery_Files(console, messagebox)
    if is_admin(console, messagebox):
        try:
            while True:
                print("1. Restore Apache file: ")
                print("2. Restore ApacheSSL file: ")
                print("3. Restore MySQL files: ")
                print("4. Restore xampp-control.ini file ")
                print("5. Return to the main menu")

                choise = int(input("Select a menu item (1 - 5): "))
                if choise == 1:
                    recovery_files.file_recovery_apache()
                elif choise == 2:
                    recovery_files.file_recovery_apachessl()
                elif choise == 3:
                    recovery_files.file_recovery_mysql()
                elif choise == 4:
                    recovery_files.file_recovery_xampp_control()
                elif choise == 5:
                    break

        except BaseException as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )

    else:
        run_as_admin(console, messagebox)


if __name__ == "__main__":
    file_recovery_mode_console()
