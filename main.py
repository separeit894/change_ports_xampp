from tkinter import *
from tkinter import ttk
import tkinter as tk
from src.change_port_apache import change_port_apache
from src.change_ssl import change_port_ssl
from src.mysql_and_phpmyadmin import change_port_mysql

root = Tk()
root.title("Главное меню")
root.geometry("600x400")

style = ttk.Style()
style.configure("Big.TButton", font=("Arial", 12), padding=10, width=20, height=5)

main_label = ttk.Label(root, text="Главное меню", font=("Arial", 12))
main_label.pack(anchor=CENTER, padx=10, pady=20)

def apache_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта MySQL")
    window.geometry("500x250")

    enter_pole = tk.Entry(window, width=20, font=("Arial", 16))
    enter_pole.pack(anchor=CENTER, pady=30)

    result_label = ttk.Label(window, text="Работа выполнена", font=("Arial", 12))

    def on_submit():
        print("Вы ввели:", enter_pole.get())
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        change_port_apache(enter_pole.get())

    submit_button = tk.Button(window, text="Применить", command=on_submit)
    submit_button.pack()

button_mysql = ttk.Button(root, text="Apache", command=apache_button, style="Big.TButton")
button_mysql.pack(anchor=CENTER)

# ApacheSSL

def apachessl_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта ApacheSSL")
    window.geometry("500x250")

    enter_pole = tk.Entry(window, width=20, font=("Arial", 16))
    enter_pole.pack(anchor=CENTER, pady=30)

    result_label = ttk.Label(window, text="Работа выполнена", font=("Arial", 12))

    def on_submit():
        print("Вы ввели:", enter_pole.get())
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        change_port_ssl(enter_pole.get())

    submit_button = tk.Button(window, text="Применить", command=on_submit)
    submit_button.pack()

button_mysql = ttk.Button(root, text="ApacheSSL", command=apachessl_button, style="Big.TButton")
button_mysql.pack(anchor=CENTER)


# Mysql

def mysql_button():
    window = Toplevel(root)  # Используем Toplevel вместо Tk() для дочерних окон
    window.title("Меню изменения порта MySQL")
    window.geometry("500x250")

    enter_pole = tk.Entry(window, width=20, font=("Arial", 16))
    enter_pole.pack(anchor=CENTER, pady=30)

    result_label = ttk.Label(window, text="Работа выполнена", font=("Arial", 12))

    def on_submit():
        print("Вы ввели:", enter_pole.get())
        result_label.pack(anchor=CENTER, pady=20, padx=20)
        # Через 3000 мс (3 секунды) удаляем надпись
        window.after(3000, result_label.pack_forget)
        change_port_mysql(enter_pole.get())

    submit_button = tk.Button(window, text="Применить", command=on_submit)
    submit_button.pack()

button_mysql = ttk.Button(root, text="MySQL", command=mysql_button, style="Big.TButton")
button_mysql.pack(anchor=CENTER, fill=tk.X, padx=100)

root.mainloop()