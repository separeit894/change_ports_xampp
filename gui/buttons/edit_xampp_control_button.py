from tkinter import Toplevel
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from core import (
    run_as_admin,
    is_admin,
    edit_file_xampp_control,
)


result_port_apache = ""
result_port_apachessl = ""
result_port_mysql = ""

check_completed_variables = False

def edit_xampp_control_button(root, style):
    if is_admin():
                
        window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
        window.title("Меню изменения портов в xampp_control.ini")
        window.geometry("500x300")

        # Apache
        Frame_Apache = ttk.Frame(window)
        Frame_Apache.pack(pady=10)

        Label_Apache = ttk.Label(
            Frame_Apache, text="Apache", width=10, font=("Arial", 12)
        )

        Label_Apache.pack(side=tk.LEFT)

        # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
        enter_pole_apache = ttk.Entry(Frame_Apache, width=20, font=("Arial", 16))

        enter_pole_apache.pack(side=tk.LEFT)

        # Значение, которое пользователь ввел ранее
        enter_pole_apache.insert(0, result_port_apache)

        # ApacheSSL
        Frame_ApacheSSL = ttk.Frame(window)
        Frame_ApacheSSL.pack(pady=10)

        Label_ApacheSSL = ttk.Label(
            Frame_ApacheSSL, text="ApacheSSL", width=10, font=("Arial", 12)
        )

        Label_ApacheSSL.pack(side=tk.LEFT)

        # Поле ввода, прикрепляется к окну window, будет иметь шрифт Arial 16 пунктов
        enter_pole_apachessl = ttk.Entry(Frame_ApacheSSL, width=20, font=("Arial", 16))

        # Размещается по центру
        enter_pole_apachessl.pack(side=tk.LEFT)

        enter_pole_apachessl.insert(0, result_port_apachessl)

        # MySQL
        Frame_MySQL = ttk.Frame(window)
        Frame_MySQL.pack(pady=10)

        Label_MySQL = ttk.Label(Frame_MySQL, text="MySQL", width=10, font=("Arial", 12))

        Label_MySQL.pack(side=tk.LEFT)

        # Поле ввода, прикрепляется к Frame_MySQL, будет иметь шрифт Arial 16 пунктов
        enter_pole_mysql = ttk.Entry(Frame_MySQL, width=20, font=("Arial", 16))

        enter_pole_mysql.pack(side=tk.LEFT)

        enter_pole_mysql.insert(0, str(result_port_mysql))

        # Функция, которая будеть работать если пользователь нажмет на кнопку 'Применить'
        def on_submit():
            global result_port_apache, result_port_mysql, result_port_apachessl
            # Если переменная пуста, то значение берется из того что пользователь ввел
            
            
            def get_value_port(enter_pole, result_port):
                if result_port == "":
                    result_port = str(enter_pole.get())
                else:
                    result_port = str(enter_pole.get())
                
                return result_port
            
            result_port_apache = get_value_port(enter_pole_apache, result_port_apache)
            result_port_apachessl = get_value_port(enter_pole_apachessl, result_port_apachessl)
            result_port_mysql = get_value_port(enter_pole_mysql, result_port_mysql)
                    
        
            # Передаем параметры в функцию
            result = edit_file_xampp_control(
                result_port_apache, result_port_apachessl, result_port_mysql
            )
            
            if result:
                messagebox.showinfo("Информация", "Порты изменены успешно!")

            window.after(250, window.destroy())

        submit_button = ttk.Button(
            window, text="Применить", command=on_submit, style="Small.TButton"
        )

        submit_button.pack()

    else:
        # Перезапуск программы в случае если нету прав администратора
        print("Ошибка: Требуются права администратора.")
        run_as_admin()

    # Кнопка 'Применить', прикрепляется к окну window. Ссылается на функцию on_submit. Имеет стиль 'Small.TButton'


if __name__ == "__main__":
    edit_file_xampp_control()
