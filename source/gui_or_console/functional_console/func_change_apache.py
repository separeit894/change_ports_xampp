import traceback


def apache_mode_console():
    try:
        while True:
            print("1. Introduce a new Apache port: ")
            print("2. Go back to the main menu")

            choise = int(input("Select a menu item ( 1 - 2 ): "))
            if choise == 1:
                new_port = str(input("Enter a new port: "))
                change_port_apache(new_port)
                break
            elif choise == 2:
                break

    except BaseException as e:
        tb = traceback.format_exc()
        print(f"An error has been detected!{tb}")


if __name__ == "__main__":
    from ...change_ports import change_port_apache

    apache_mode_console()
