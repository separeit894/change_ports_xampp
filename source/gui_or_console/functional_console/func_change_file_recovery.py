import ctypes

from ...change_ports import run_as_admin
from ...change_ports import file_recovery_apache
from ...change_ports import file_recovery_apachessl
from ...change_ports import file_recovery_mysql
from ...change_ports import file_recovery_xampp_control

def file_recovery_c():
    if ctypes.windll.shell32.IsUserAnAdmin():
        while True:
            print("1. Восстановить файл Apache : ")
            print("2. Восстановить файл ApacheSSL: ")
            print("3. Восстановить файлы MySQL: ")
            print("4. Восстановить файл xampp-control.ini ")
            print("5. Вернуться в главное меню")

            choise = int(input("Выберите пункт меню ( 1 - 5 ): "))
            if choise == 1:
                file_recovery_apache()
            elif choise == 2:
                file_recovery_apachessl()
            elif choise == 3:
                file_recovery_mysql()
            elif choise == 4:
                file_recovery_xampp_control()
            elif choise == 5:
                break

    else:
        run_as_admin()

if __name__ == "__main__":
    file_recovery_c()
