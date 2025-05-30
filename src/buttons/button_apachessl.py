import os, sys
from tkinter import *
from tkinter import ttk
from ..change_ports.change_port_ssl import change_port_ssl

sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))


# ApacheSSL

def apachessl_button(root, style):
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта ApacheSSL")
    window.geometry("500x250")

    # Создаю новый стиль кнопок для MySQL, ApacheSSL, Apache

    # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
    enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
    # Размещается по центру
    enter_pole.pack(anchor=CENTER, pady=30)

    # Будет работать после того как пользователь кликнул по кнопке 'Применить'
    result_label = ttk.Label(window, text="Порт изменен", font=("Arial", 12))

    # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
    def on_submit():
        global result_port_apachessl
        result_port_apachessl = str(enter_pole.get())
        # Выводит значение, которое пользователь ввел, после того как кликнул по кнопке "Применить"
        print("Вы ввели:", enter_pole.get())
        if not result_port_apachessl == "": 
            # Выводит строку с успешным изменением порта ( см. 84 строку кода )
            result_label.pack(anchor=CENTER, pady=20, padx=20)
            # Через 3000 мс (3 секунды) удаляем надпись
            window.after(3000, result_label.pack_forget)
            # Передаем значение нового порта в функцию
            change_port_ssl(result_port_apachessl)

    """
    Кнопка 'Применить', прикрепляется к окну window.
    Ссылается на функцию on_submit ( см. 87 строку кода )
    Имеет стиль 'Small.TButton ( см. 17 строку кода )'
    """
    submit_button = ttk.Button(window, text="Применить", command=on_submit, style="Small.TButton")
    submit_button.pack()

if __name__ == "__main__":
    apachessl_button()
