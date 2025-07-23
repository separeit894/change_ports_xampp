import traceback

from ...config import Escape_Sequences
from ...config import Colors


def apache_mode_console():
    from ...change_ports import change_port_apache

    try:
        while True:
            list_text_apache = [
                "Introduce a new Apache port:",
                "Go back to the main menu"
            ]
            for i, line in enumerate(list_text_apache):
                print(f"{i}. {line}")

            choise = int(input("Select a menu item ( 0 - 1 ): "))
            if choise == 0:
                new_port = str(input("Enter a new port: "))
                change_port_apache(new_port)
                break
            elif choise == 1:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )


if __name__ == "__main__":
    apache_mode_console()
