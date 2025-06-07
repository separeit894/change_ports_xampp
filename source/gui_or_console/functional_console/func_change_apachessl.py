from ...change_ports import change_port_ssl

def apachessl():
    while True:
        print("1. Ввести новый порт ApacheSSL: ")
        print("2. Вернуться в главное меню")

        choise = int(input("Выберите пункт меню ( 1 - 2 ): "))
        if choise == 1:
            new_port = str(input("Введите новый порт: "))
            change_port_ssl(new_port)
            break
        elif choise == 2:
            break

if __name__ == "__main__":
    apachessl()
