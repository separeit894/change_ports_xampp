from ...change_ports import change_port_mysql

import traceback

def mysql_mode_console():
    try:
        while True:
            print("1. Enter new port MySQL: ")
            print("2. Return to main menu")

            choise = int(input("Select a menu item ( 1 - 2 ): "))
            if choise == 1:
                new_port = str(input("Enter new port: "))
                change_port_mysql(new_port)
                break
            elif choise == 2:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")

if __name__ == "__main__":
    mysql_mode_console()