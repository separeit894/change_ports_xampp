import ctypes
from ...change_ports import run_as_admin
from ...change_ports import edit_file_xampp_control

def xampp_control():
    if ctypes.windll.shell32.IsUserAnAdmin():
        while True:
            print("1. Ввести новый порт Apache : ")
            print("2. Ввести новый порт ApacheSSL: ")
            print("3. Ввести новый порт MySQL: ")
            print("4. Вернуться в главное меню")

            choise = int(input("Выберите пункт меню ( 1 - 4 ): "))
            if choise == 1:
                new_port_apache = str(input("Введите новый порт Apache: "))
                edit_file_xampp_control(new_port_apache, "None", "None")
            elif choise == 2:
                new_port_apachessl = str(input("Введите новый порт ApaceSSL: "))
                edit_file_xampp_control("None", new_port_apachessl, "None")
            elif choise == 3:
                new_port_mysql = str(input("Введите новый порт MySQL: "))
                edit_file_xampp_control("None", "None", new_port_mysql)
            elif choise == 4:
                break

    else:
        run_as_admin()

if __name__ == "__main__":
    xampp_control()
