from tkinter import CENTER, W

from tkinter import Tk
from tkinter import ttk

import tkinter as tk
import traceback

from ..buttons import (
    apache_button,
    apachessl_button,
    mysql_button,
    edit_xampp_control_button,
    bfiles_recovery,
)

from .update_cpx import Update
from ..config import version


class mode_gui:
    try:
        def __init__(self, console, messagebox):
            self.console = console
            self.messagebox = messagebox
            self.root = Tk()
            self.root.title("Change Ports Xampp")
            # Создаю окно на 600x400
            self.root.geometry("600x450")

            # Создаю новый стиль кнопок для MySQL, ApacheSSL, Apache
            self.style = ttk.Style()
            self.style.configure(
                "Big.TButton", font=("Arial", 12), padding=10, width=20, height=5
            )

            self.style.configure(
                "Small.TButton", font=("Arial", 10), padding=10, width=20, height=5
            )

            # Обозначение версии приложения
            self.version_int = version.split("-")[1]
            self.text_version = ttk.Label(self.root, text=f"Версия: {self.version_int}", font=("Arial", 8))

            self.text_version.pack(anchor=W)

            # Текст 'Главное меню', который будет использовать шрифт Arial 12 пунктов
            self.main_label = ttk.Label(self.root, text="Главное меню", font=("Arial", 12))
            # Размещает этот текст по центру
            self.main_label.pack(anchor=CENTER, padx=10, pady=30)

            # Внизу кнопка 'Apache', прикреплен к главному окну ( root ). Используется стиль Big.TButton ( см. 16 стр )

            self.button_apache = ttk.Button(
                self.root,
                text="Apache",
                command=lambda: apache_button(self.root, self.style, self.console, self.messagebox),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_apache.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Кнопка 'ApacheSSL', прикреплен к главному окну ( root ). Используется стиль Big.TButton ( см. 16 стр )

            self.button_apachessl = ttk.Button(
                self.root,
                text="ApacheSSL",
                command=lambda: apachessl_button(self.root, self.style, self.console, self.messagebox),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_apachessl.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Кнопка 'MySQL', прикреплена к главному окну ( root ). Ссылается на функцию 'mysql_button' (см. код с 116 - 134 стр.). Используется стиль Big.TButton ( см. 16 стр )
            self.button_mysql = ttk.Button(
                self.root,
                text="MySQL",
                command=lambda: mysql_button(self.root, self.style, self.console, self.messagebox),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_mysql.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Кнопка 'edit xampp control.ini', прикреплена к главному окну ( root ). Используется стиль Big.TButton ( см. 16 стр )

            self.button_xampp_control = ttk.Button(
                self.root,
                text="\tEdit xampp control.ini\nТребуются права администратора!",
                command=lambda: edit_xampp_control_button(self.root, self.style, self.console, self.messagebox),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_xampp_control.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Эта кнопка сделана для того чтобы восстановить файлы, в случае их некорректной работы

            self.button_file_recovery = ttk.Button(
                self.root,
                text="Восстановление файлов",
                command=lambda: bfiles_recovery(self.root, self.style, self.console, self.messagebox),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_file_recovery.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Запускается цикл
            update = Update(console, messagebox)
            if update.checking_for_update():
                update.update_gui(self.root, self.style)
            
        def run_app(self):
            self.root.mainloop()

    except BaseException as e:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")


if __name__ == "__main__":
    mode_gui().run_app()
