from .functional_console import apache
from .functional_console import apachessl
from .functional_console import mysql
from .functional_console import xampp_control
from .functional_console import file_recovery_c

def console():
    while True:
        print("1. Изменить порт Apache ")
        print("2. Изменить порт ApacheSSL ")
        print("3. Изменить порт MySQL ")
        print("4. Edit xampp control.ini. Требуются права администратора! ")
        print("5. Восстановить файлы ")

        choise = int(input("Выберите пункт меню ( 1 - 5 ): "))
        if choise == 1:
            apache()
        elif choise == 2:
            apachessl()
        elif choise == 3:
            mysql()
        elif choise == 4:
            xampp_control()
        elif choise == 5:
            file_recovery_c()
        else:
            print('Вы выбрали некорректный номер!')


if __name__ == "__main__":
    console()
