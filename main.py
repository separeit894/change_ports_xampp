from tkinter import *
from tkinter import ttk
import tkinter as tk
from src import *

result_port_mysql = None
result_port_apache = None
result_port_apachessl = None

def main():
    root = Tk()
    root.title("Change Ports Xampp")
    # Создаю окно на 600x400
    root.geometry("600x400")


    style = ttk.Style()
    # Создаю новый стиль кнопок для MySQL, ApacheSSL, Apache
    style.configure("Big.TButton", font=("Arial", 12), padding=10, width=20, height=5)
    style.configure("Small.TButton", font=("Arial", 10), padding=10, width=20, height=5)

    # Обозначение версии приложения
    text_version = ttk.Label(root, text="Версия: 1.9", font=("Arial", 8))
    text_version.pack(anchor=W)

    # Текст 'Главное меню', который будет использовать шрифт Arial 12 пунктов
    main_label = ttk.Label(root, text="Главное меню", font=("Arial", 12))
    # Размещает этот текст по центру
    main_label.pack(anchor=CENTER, padx=10, pady=30)


    """
    Внизу кнопка 'Apache', прикреплен к главному окну ( root )
    Ссылается на функцию 'apache_button' (см. код с 30 - 53 стр.)
    Используется стиль Big.TButton ( см. 16 стр )
    """
    button_apache = ttk.Button(root, text="Apache", command=lambda: apache_button(root, style), style="Big.TButton")
    # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
    button_apache.pack(anchor=CENTER, fill=tk.X, padx=100)


    """
    Кнопка 'ApacheSSL', прикреплен к главному окну ( root )
    Ссылается на функцию 'apachessl_button' (см. код с 73 - 103 стр.)
    Используется стиль Big.TButton ( см. 16 стр )
    """
    button_apachessl = ttk.Button(root, text="ApacheSSL", command=lambda: apachessl_button(root, style), style="Big.TButton")
    # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
    button_apachessl.pack(anchor=CENTER, fill=tk.X, padx=100)


    """
    Кнопка 'MySQL', прикреплена к главному окну ( root )
    Ссылается на функцию 'mysql_button' (см. код с 116 - 134 стр.)
    Используется стиль Big.TButton ( см. 16 стр )
    """
    button_mysql = ttk.Button(root, text="MySQL", command=lambda: mysql_button(root, style), style="Big.TButton")
    # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
    button_mysql.pack(anchor=CENTER, fill=tk.X, padx=100)


    """
    Кнопка 'edit xampp control.ini', прикреплена к главному окну ( root )
    Ссылается на функцию 'edit_xampp_control_button' (см. код с 176 - 261 стр.)
    Используется стиль Big.TButton ( см. 16 стр )
    """
    button_xampp_control = ttk.Button(root, text="Edit xampp control.ini\nТребуются права администратора!", command=lambda: edit_xampp_control_button(root, style), style="Big.TButton")
    # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
    button_xampp_control.pack(anchor=CENTER, fill=tk.X, padx=100)

    # Запускается цикл
    root.mainloop()

if __name__ == "__main__":
    main()
