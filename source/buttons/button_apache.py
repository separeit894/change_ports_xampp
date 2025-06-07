import os
import sys

from tkinter import Toplevel
from tkinter import CENTER
from tkinter import ttk

from ..change_ports.change_port_apache import change_port_apache

sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))


def apache_button(root, style):
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта Apache")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(
        window, 
        width=20,
        font=("Arial", 16)
        )
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        global result_port_apache
        result_port_apache = str(enter_pole.get())
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print(
            "Вы ввели:",
            enter_pole.get()
            )
        if not result_port_apache == "": 
            change_port_apache(result_port_apache)

    # Кнопка submit_button, прикрепляется к окну window Используется стиль 'Small.TButton'
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()
    

if __name__ == "__main__":
    apache_button()
    