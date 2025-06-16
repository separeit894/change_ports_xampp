from ...change_ports import change_port_apache

def apache_mode_console():
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

if __name__ == "__main__":
    apache_mode_console()
