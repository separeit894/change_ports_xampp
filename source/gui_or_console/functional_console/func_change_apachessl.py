from ...change_ports import change_port_ssl
from ...config import Escape_Sequences
from ...config import Colors

import traceback


def apachessl_mode_console(console, messagebox):
    try:
        while True:
            print("1. Enter a new Apache SSL port: ")
            print("2. Go back to the main menu")

            choise = int(input("Select a menu item ( 1 - 2 ): "))
            if choise == 1:
                new_port = str(input("Enter a new port: "))
                change_port_ssl(new_port, console, messagebox)
                break
            elif choise == 2:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )


if __name__ == "__main__":
    apachessl_mode_console()
