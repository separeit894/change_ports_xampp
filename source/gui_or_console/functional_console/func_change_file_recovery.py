import traceback

from ...change_ports import run_as_admin
from ...change_ports import is_admin
from ...change_ports import Recovery_Files
from ...config import Escape_Sequences
from ...config import Colors


def file_recovery_mode_console():
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
                if choise == 0:
                    recovery_files.file_recovery_apache()
                elif choise == 1:
                    recovery_files.file_recovery_apachessl()
                elif choise == 2:
                    recovery_files.file_recovery_mysql()
                elif choise == 3:
                    recovery_files.file_recovery_xampp_control()
                elif choise == 4:
                    break

        except BaseException as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )

    else:
        run_as_admin()


if __name__ == "__main__":
    file_recovery_mode_console()
