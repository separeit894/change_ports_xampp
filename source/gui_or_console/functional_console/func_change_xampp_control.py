import traceback

from ...config import Escape_Sequences
from ...config import Colors


def xampp_control_mode_console(console, messagebox):
    from ...change_ports import run_as_admin
    from ...change_ports import is_admin
    from ...change_ports import edit_file_xampp_control

    if is_admin(console, messagebox):
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
                    edit_file_xampp_control(new_port_apache, "None", "None", console, messagebox)
                elif choise == 1:
                    new_port_apachessl = str(input("Enter new port ApaceSSL: "))
                    edit_file_xampp_control("None", new_port_apachessl, "None", console, messagebox)
                elif choise == 2:
                    new_port_mysql = str(input("Enter new port MySQL: "))
                    edit_file_xampp_control("None", "None", new_port_mysql, console, messagebox)
                elif choise == 3:
                    break

        except BaseException as e:
            tb = traceback.format_exc()
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )
    else:
        run_as_admin(console, messagebox)


if __name__ == "__main__":
    xampp_control_mode_console()
