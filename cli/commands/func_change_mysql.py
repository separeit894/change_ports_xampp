import traceback

from config import Escape_Sequences
from config import Colors


def mysql_mode_console():
    from core import change_port_mysql

    try:
        while True:
            list_text_mysql = [
                "Enter new port MySQL:",
                "Return to main menu"
            ]
            
            for i, line in enumerate(list_text_mysql):
                print(f"{i}. {line}")

            choise = int(input("Select a menu item ( 0 - 1 ): "))
            if choise == 0:
                new_port = str(input("Enter new port: "))
                result = change_port_mysql(new_port)
                if result:
                    print(
                        f"{Escape_Sequences.double_new_line}{Colors.GREEN}MySQL port changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                    )
                break
            elif choise == 1:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )


if __name__ == "__main__":
    mysql_mode_console()
