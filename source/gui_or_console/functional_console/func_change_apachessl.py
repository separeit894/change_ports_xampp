from ...change_ports import change_port_ssl

def apachessl_mode_console():
    while True:
        print("1. Enter a new Apache SSL port: ")
        print("2. Go back to the main menu")

        choise = int(input("Select a menu item ( 1 - 2 ): "))
        if choise == 1:
            new_port = str(input("Enter a new port: "))
            change_port_ssl(new_port)
            break
        elif choise == 2:
            break

if __name__ == "__main__":
    apachessl_mode_console()
