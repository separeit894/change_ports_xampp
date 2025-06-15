from .functional_console import apache
from .functional_console import apachessl
from .functional_console import mysql
from .functional_console import xampp_control
from .functional_console import file_recovery_c
import  sys
import ctypes

# def create_console():
#     ctypes.windll.kernel32.AllocConsole()
#     sys.stdout = open('CONOUT$', 'w')  # Перенаправляем стандартный вывод в консоль
#     sys.stderr = open('CONOUT$', 'w')
#     sys.stdin = open('CONIN$', 'r')

def console():
    # create_console()
    while True:
        print("1. Change port Apache ")
        print("2. Change port ApacheSSL ")
        print("3. Change port MySQL ")
        print("4. Edit xampp control.ini. Administrator rights required! ")
        print("5. Recover files ")

        choise = int(input("Select a menu item ( 1 - 5 ): "))
        
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
            print('You have selected an incorrect number!')


if __name__ == "__main__":
    console()
