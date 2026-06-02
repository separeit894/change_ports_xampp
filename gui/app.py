from tkinter import (
    CENTER,
    W,
    Tk,
    ttk
)

import tkinter as tk

import traceback
import webbrowser
import logging
import os

from .buttons import (
    apache_button,
    apachessl_button,
    mysql_button,
    edit_xampp_control_button,
    bfiles_recovery,
    parametrs_button
)
from config import (
    get_encoding,
    version
)

from datetime import datetime


class GUI:
    try:
        def __init__(self):
            self.root = Tk()
            self.root.title("Change Ports Xampp")
            # Создаю окно на 600x550
            self.root.geometry("600x550")

            # Создаю новый стиль кнопок для MySQL, ApacheSSL, Apache
            self.style = ttk.Style()
            self.style.configure(
                "Big.TButton", font=("Arial", 12), padding=10, width=20, height=5
            )

            self.style.configure(
                "Small.TButton", font=("Arial", 10), padding=10, width=20, height=5
            )
            self.style.configure("BigText.TButton", font=("Arial",13))

            # Обозначение версии приложения
            self.version_int = version.split("-")[1]
            self.text_version = ttk.Label(self.root, text=f"Version: {self.version_int}", font=("Arial", 12))

            self.text_version.pack(anchor=W)
            
            self.button_parametrs = ttk.Button(self.root, text="Settings", style="BigText.TButton", command=lambda: parametrs_button(self.root, self.style))
            self.button_parametrs.pack(anchor="ne", padx=10, pady=10)
            # Текст 'Главное меню', который будет использовать шрифт Arial 12 пунктов
            self.main_label = ttk.Label(self.root, text="Main Menu", font=("Arial", 16))
            # Размещает этот текст по центру
            self.main_label.pack(anchor=CENTER, padx=10, pady=30)

            self.button_apache = ttk.Button(
                self.root,
                text="Apache",
                command=lambda: apache_button(self.root, self.style),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_apache.pack(anchor=CENTER, fill=tk.X, padx=100)


            self.button_apachessl = ttk.Button(
                self.root,
                text="ApacheSSL",
                command=lambda: apachessl_button(self.root, self.style),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_apachessl.pack(anchor=CENTER, fill=tk.X, padx=100)

            
            self.button_mysql = ttk.Button(
                self.root,
                text="MySQL",
                command=lambda: mysql_button(self.root, self.style),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_mysql.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Кнопка 'edit xampp control.ini', прикреплена к главному окну ( root ). Используется стиль Big.TButton ( см. 16 стр )

            self.button_xampp_control = ttk.Button(
                self.root,
                text="\tEdit xampp control.ini\nAdministrator rights are required!",
                command=lambda: edit_xampp_control_button(self.root, self.style),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_xampp_control.pack(anchor=CENTER, fill=tk.X, padx=100)

            # Эта кнопка сделана для того чтобы восстановить файлы, в случае их некорректной работы
            self.button_file_recovery = ttk.Button(
                self.root,
                text="File Recovery",
                command=lambda: bfiles_recovery(self.root, self.style),
                style="Big.TButton",
            )
            # Кнопка будет размещена по центру, отступ по x 100, будет растягиваться по ширине
            self.button_file_recovery.pack(anchor=CENTER, fill=tk.X, padx=100)
            
            self.created_by = ttk.Label(self.root, text="Created by separeit894", font=("Arial", 10))
            self.created_by.pack(anchor="n")
            
            link_github_text = "GitHub"
            self.link_github = ttk.Label(self.root, text=link_github_text, foreground="blue", cursor="hand2", font=("Arial", 10))
            self.link_github.pack(anchor="n")
            self.link_github.bind("<Button-1>", lambda e: self.open_links("https://github.com/separeit894"))
            
            main_page_text = "Main Page CPX GitHub"
            self.main_page_cpx = ttk.Label(self.root, text=main_page_text, foreground="blue", cursor="hand2", font=("Arial", 10))
            self.main_page_cpx.pack(anchor="n")
            self.main_page_cpx.bind("<Button-1>", lambda e: self.open_links("https://github.com/separeit894/change_ports_xampp"))
            
            link_releases_text = "CPX releases here!"
            self.link_releases = ttk.Label(self.root, text=link_releases_text, foreground="blue", cursor="hand2", font=("Arial", 10))
            self.link_releases.pack(anchor="n")
            self.link_releases.bind("<Button-1>", lambda e: self.open_links("https://github.com/separeit894/change_ports_xampp/releases"))
            
            
            self.use_encoding = tk.StringVar()
            self.use_encoding.set(get_encoding())
            
            self.lbl_use_encoding = ttk.Label(self.root, text=f"Currently used encoding: {self.use_encoding.get()}", font=("Arial", 13))
            self.lbl_use_encoding.pack(anchor="sw")
            
            def on_change(*args):
                self.update_use_encoding(self.use_encoding.get())
                
            self.use_encoding.trace_add('write', on_change)
            
            self.update_use_encoding(self.use_encoding.get())
            
            self.check_encoding_loop()
        
        def check_encoding_loop(self):
            # 1. Получаем актуальное значение из config/__init__.py
            current_actual_enc = get_encoding()
            
            # 2. Если оно отличается от того, что сейчас на экране
            if current_actual_enc != self.use_encoding.get():
                self.use_encoding.set(current_actual_enc)
                self.update_use_encoding(current_actual_enc)
                
            # 3. Повторяем проверку каждые 500 миллисекунд (полсекунды)
            self.root.after(1000, self.check_encoding_loop)
            
            
        def update_use_encoding(self, use_encoding):
            self.lbl_use_encoding.config(text=f"Currently used encoding: {use_encoding}")
            
            
        def open_links(self, url):
            webbrowser.open(url)
        
        def run_app(self):
            self.root.mainloop()
    
    
        

    except Exception as ex:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : An error has been detected!\n{tb}")


if __name__ == "__main__":
    GUI().run_app()
