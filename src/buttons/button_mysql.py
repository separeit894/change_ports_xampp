import os, sys
from tkinter import *
from tkinter import ttk
from ..change_ports.change_ports_mysql_and_phpmyadmin import change_port_mysql

sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))
# MySQL

def mysql_button(root, style):
    
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта MySQL")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Будет работать после того как пользователь кликнул по кнопке 'Применить'
    #result_label = ttk.Label(window, text="Порт изменен", font=("Arial", 12))

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        global result_port_mysql

        result_port_mysql = str(enter_pole.get())
        print("Вы ввели:", enter_pole.get())
        if not result_port_mysql == "": 
            # Выводит строку с успешным изменением порта ( см. 124 строку кода )
            #result_label.pack(anchor=CENTER, pady=20, padx=20)
            # Через 3000 мс (3 секунды) удаляем надпись
            #window.after(3000, result_label.pack_forget)
            # Передаем значение нового порта в функцию
            change_port_mysql(result_port_mysql)

    """
    Кнопка 'Применить', прикрепляется к окну window.
    Ссылается на функцию on_submit ( см. 87 строку кода )
    Имеет стиль 'Small.TButton ( см. 17 строку кода )'
    """
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()

if __name__ == "__main__":
    mysql_button()