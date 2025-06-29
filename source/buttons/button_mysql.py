from tkinter import Toplevel
from tkinter import CENTER
from tkinter import ttk

from ..change_ports.change_ports_mysql_and_phpmyadmin import change_port_mysql


def mysql_button(root, style):
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта MySQL")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        result_port_mysql = str(enter_pole.get())
        print("Вы ввели:", enter_pole.get())
        if not result_port_mysql == "":
            # Передаем значение нового порта в функцию
            change_port_mysql(result_port_mysql)
            window.after(250, window.destroy())

    # Кнопка 'Применить', прикрепляется к окну window. Ссылается на функцию on_submit. Имеет стиль 'Small.TButton'

    submit_button = ttk.Button(
        window, text="Применить", command=on_submit, style="Small.TButton"
    )

    submit_button.pack()


if __name__ == "__main__":
    mysql_button()
