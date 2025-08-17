from tkinter import Toplevel
from tkinter import CENTER
from tkinter import ttk
from tkinter import messagebox

from core import change_port_ssl

result_port_apachessl = ""

def apachessl_button(root, style):
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Port Change Menu ApacheSSL")
    window.geometry("500x250")

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))

    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)
    enter_pole.insert(0, result_port_apachessl)
    
    
    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        global result_port_apachessl
        result_port_apachessl = str(enter_pole.get())

        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("You have entered:", enter_pole.get())

        if not result_port_apachessl == "":
            # Передаем значение нового порта в функцию
            result = change_port_ssl(result_port_apachessl)
            if result:
                messagebox.showinfo("Information", "The port has been changed successfully!")
            window.after(250, window.destroy())

    # Кнопка 'Применить', прикрепляется к окну window. Ссылается на функцию on_submit Имеет стиль 'Small.TButton

    submit_button = ttk.Button(
        window, text="Apply", command=on_submit, style="Small.TButton"
    )
    submit_button.pack()


if __name__ == "__main__":
    apachessl_button()
