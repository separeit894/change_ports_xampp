from tkinter import (
    Toplevel,
    CENTER,
    ttk,
    messagebox
)

from core import change_port_mysql
from datetime import datetime

import os
import logging
import traceback


result_port_mysql = ""

def mysql_button(root, style) -> None:
    try:
        window = Toplevel(root)  
        window.title("MySQL Port Change Menu")
        window.geometry("500x250")

        enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
        # Размещается по центру
        enter_pole.pack(anchor=CENTER, pady=30)
        enter_pole.insert(0, result_port_mysql)

        
        def on_submit():
            global result_port_mysql
            result_port_mysql = str(enter_pole.get())
            print("You have entered:", enter_pole.get())
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : Port MySQL that user entered : {result_port_mysql}")
            if not result_port_mysql == "":
                # Передаем значение нового порта в функцию
                result = change_port_mysql(result_port_mysql)
                if result:
                    messagebox.showinfo("Information", "The port has been changed successfully!")
                window.after(250, window.destroy())

        # Кнопка 'Применить', прикрепляется к окну window. Ссылается на функцию on_submit. Имеет стиль 'Small.TButton'

        submit_button = ttk.Button(
            window, text="Apply", command=on_submit, style="Small.TButton"
        )

        submit_button.pack()
        
    except Exception:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : An error has been detected!\n{tb}")


if __name__ == "__main__":
    mysql_button()
