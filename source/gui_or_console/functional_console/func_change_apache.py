from ...change_ports import change_port_apache

def apache():
    while True:
        print("1. Ввести новый порт Apache: ")
        print("2. Вернуться в главное меню")

        choise = int(input("Выберите пункт меню ( 1 - 2 ): "))
        if choise == 1:
            new_port = str(input("Введите новый порт: "))
            change_port_apache(new_port)
            break
        elif choise == 2:
            break

if __name__ == "__main__":
    apache()
