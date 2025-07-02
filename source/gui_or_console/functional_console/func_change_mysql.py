import traceback

from ...config import Escape_Sequences
from ...config import Colors


def mysql_mode_console(console, messagebox):
    from ...change_ports import change_port_mysql

    try:
        while True:
            print("1. Enter new port MySQL: ")
            print("2. Return to main menu")

            choise = int(input("Select a menu item ( 1 - 2 ): "))
            if choise == 1:
                new_port = str(input("Enter new port: "))
                change_port_mysql(new_port, console, messagebox)
                break
            elif choise == 2:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )


if __name__ == "__main__":
    mysql_mode_console()
