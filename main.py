from tkinter import *
from tkinter import ttk
import tkinter as tk
from src.change_port_apache import change_port_apache
from src.change_ssl import change_port_ssl
from src.mysql_and_phpmyadmin import change_port_mysql

root = Tk()
root.title("Change Ports Xampp")
# Создаю окно на 600x400
root.geometry("600x400")


style = ttk.Style()
# Создаю новый стиль кнопок для MySQL, ApacheSSL, Apache
style.configure("Big.TButton", font=("Arial", 12), padding=10, width=20, height=5)
style.configure("Small.TButton", font=("Arial", 10), padding=10, width=20, height=5)

# Обозначение версии приложения
text_version = ttk.Label(root, text="Версия: 1.2", font=("Arial", 8))
text_version.pack(anchor=W)

# Текст 'Главное меню', который будет использовать шрифт Arial 12 пунктов
main_label = ttk.Label(root, text="Главное меню", font=("Arial", 12))
# Размещает этот текст по центру
main_label.pack(anchor=CENTER, padx=10, pady=30)

# Apache

def apache_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта Apache")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)
    
    # Будет работать после того как пользователь кликнул по кнопке 'Применить'
    result_label = ttk.Label(window, text="Порт изменен", font=("Arial", 12))

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("Вы ввели:", enter_pole.get())
        # Выводит строку с успешным изменением порта ( см. 41 строку кода )
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        # Передаем значение нового порта в функцию
        change_port_apache(enter_pole.get())

    """
    Кнопка submit_button, прикрепляется к окну window
    Ссылается на функцию on_submit ( см. 44 строку кода )
    Используется стиль 'Small.TButton' ( см. 17 строку кода)
    """
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()

"""
Внизу кнопка 'Apache', прикреплен к главному окну ( root )
Ссылается на функцию 'apache_button' (см. код с 30 - 53 стр.)
Используется стиль Big.TButton ( см. 16 стр )
"""
button_apache = ttk.Button(root, text="Apache", command=apache_button, style="Big.TButton")
# Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
button_apache.pack(anchor=CENTER, fill=tk.X, padx=100)

# ApacheSSL

def apachessl_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта ApacheSSL")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Будет работать после того как пользователь кликнул по кнопке 'Применить'
    result_label = ttk.Label(window, text="Порт изменен", font=("Arial", 12))

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("Вы ввели:", enter_pole.get())
        # Выводит строку с успешным изменением порта ( см. 84 строку кода )
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        # Передаем значение нового порта в функцию
        change_port_ssl(enter_pole.get())

    """
    Кнопка 'Применить', прикрепляется к окну window.
    Ссылается на функцию on_submit ( см. 87 строку кода )
    Имеет стиль 'Small.TButton ( см. 17 строку кода )'
    """
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()

"""
Кнопка 'ApacheSSL', прикреплен к главному окну ( root )
Ссылается на функцию 'apachessl_button' (см. код с 73 - 103 стр.)
Используется стиль Big.TButton ( см. 16 стр )
"""
button_apachessl = ttk.Button(root, text="ApacheSSL", command=apachessl_button, style="Big.TButton")
# Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
button_apachessl.pack(anchor=CENTER, fill=tk.X, padx=100)

# MySQL

def mysql_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта MySQL")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Будет работать после того как пользователь кликнул по кнопке 'Применить'
    result_label = ttk.Label(window, text="Порт изменен", font=("Arial", 12))

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("Вы ввели:", enter_pole.get())
        # Выводит строку с успешным изменением порта ( см. 124 строку кода )
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        # Передаем значение нового порта в функцию
        change_port_mysql(enter_pole.get())

    """
    Кнопка 'Применить', прикрепляется к окну window.
    Ссылается на функцию on_submit ( см. 87 строку кода )
    Имеет стиль 'Small.TButton ( см. 17 строку кода )'
    """
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()

"""
Кнопка 'MySQL', прикреплена к главному окну ( root )
Ссылается на функцию 'mysql_button' (см. код с 116 - 134 стр.)
Используется стиль Big.TButton ( см. 16 стр )
"""
button_mysql = ttk.Button(root, text="MySQL", command=mysql_button, style="Big.TButton")
# Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
button_mysql.pack(anchor=CENTER, fill=tk.X, padx=100)

# Запускается цикл
root.mainloop()