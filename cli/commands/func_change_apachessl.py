from core import change_port_ssl
from config import Escape_Sequences
from config import Colors

import traceback


def apachessl_mode_console():
    try:
        while True:
            list_text_apachessl = [
                "Enter a new Apache SSL port:",
                "Go back to the main menu"
            ]
            for i, line in enumerate(list_text_apachessl):
                print(f"{i}. {line}")

            choise = int(input("Select a menu item ( 0 - 1 ): "))
            if choise == 0:
                new_port = str(input("Enter a new port: "))
                result = change_port_ssl(new_port)
                if result:
                    print(
                        f"{Escape_Sequences.double_new_line}{Colors.GREEN}ApacheSSL port changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
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
    apachessl_mode_console()
