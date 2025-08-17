import traceback

from config import Escape_Sequences
from config import Colors


def xampp_control_mode_console():
    from core import run_as_admin
    from core import is_admin
    from core import edit_file_xampp_control

    if is_admin():
        try:
            while True:
                list_text_xampp_control = [
                    "Enter new port Apache :",
                    "Enter new port ApacheSSL:",
                    "Enter new port MySQL:",
                    "Return to main menu"
                ]
                for i, line in enumerate(list_text_xampp_control):
                    print(f"{i}. {line}")

                choise = int(input("Select a menu item ( 0 - 3 ): "))
                if choise == 0:
                    new_port_apache = str(input("Enter new port Apache: "))
                    result = edit_file_xampp_control(new_port_apache, "None", "None")
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}Port(s) changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                elif choise == 1:
                    new_port_apachessl = str(input("Enter new port ApaceSSL: "))
                    result = edit_file_xampp_control("None", new_port_apachessl, "None")
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}Port(s) changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                elif choise == 2:
                    new_port_mysql = str(input("Enter new port MySQL: "))
                    result = edit_file_xampp_control("None", "None", new_port_mysql)
                    if result:
                        print(
                            f"{Escape_Sequences.double_new_line}{Colors.GREEN}Port(s) changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                        )
                elif choise == 3:
                    break

        except Exception as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )
    else:
        run_as_admin()


if __name__ == "__main__":
    xampp_control_mode_console()
