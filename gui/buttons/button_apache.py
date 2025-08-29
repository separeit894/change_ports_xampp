from tkinter import Toplevel
from tkinter import CENTER
from tkinter import ttk
from tkinter import messagebox

from core import change_port_apache
from datetime import datetime
import os
import logging

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)

result_port_apache = ""

def apache_button(root, style) -> None:
    
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Port Change Menu Apache")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)
    enter_pole.insert(0, result_port_apache)
    
    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit() -> None:
        global result_port_apache
        result_port_apache = str(enter_pole.get())
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : New port Apache that user entered : {result_port_apache}")
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("You have entered:", enter_pole.get())
        if not result_port_apache == "":
            result = change_port_apache(result_port_apache)
            if result:
                messagebox.showinfo("Information", "The port has been changed successfully!")
            window.after(250, window.destroy())

    # Кнопка submit_button, прикрепляется к окну window Используется стиль 'Small.TButton'
    submit_button = ttk.Button(
        window, text="Apply", command=on_submit, style="Small.TButton"
    )
    submit_button.pack()


if __name__ == "__main__":
    apache_button()
