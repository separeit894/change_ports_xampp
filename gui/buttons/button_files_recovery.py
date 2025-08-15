from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from core import Recovery_Files


def on_apache_click():
    if Recovery_Files().file_recovery_apache:
        messagebox.showinfo("Успех", "Файл Apache уже восстановлен!")
    
def on_apachessl_click():
    if Recovery_Files().file_recovery_apachessl:
        messagebox.showinfo("Успех", "Файл ApacheSSL уже восстановлен!")

def on_mysql_click():
    if Recovery_Files().file_recovery_mysql:
        messagebox.showinfo("Успех", "Файл MySQL уже восстановлен!")
        

def on_xampp_control_click():
    if Recovery_Files().file_recovery_xampp_control:
        messagebox.showinfo("Успех", "Файл xampp control уже восстановлен!")
        

def bfiles_recovery(root, style):
    window = Toplevel(root)
    window.title("Меню восстановление файлов")
    window.geometry("500x300")
    recovery_files = Recovery_Files()
    # Восстановления файла Apache
    spaces_for_apache = "           "
    
    
    button_apache = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apache}Apache",
        command=on_apache_click,
        style="Big.TButton",
    )
    
    

    button_apache.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файла ApacheSSL
    spaces_for_apachessl = "        "
    button_apachessl = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apachessl}ApacheSSL",
        command=on_apachessl_click,
        style="Big.TButton",
    )
    

    button_apachessl.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файлов MySQL
    spaces_for_mysql = "           "
    button_mysql = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_mysql}MySQL",
        command=on_mysql_click,
        style="Big.TButton",
    )
    
    
    

    button_mysql.pack(anchor="center", fill=tk.X, padx=150)

    
    # Восстановление файла xampp-control.ini
    button_xampp_control = ttk.Button(
        window,
        text="Восстановить файл\n    xampp-control.ini",
        command=on_xampp_control_click,
        style="Big.TButton",
    )
    

    button_xampp_control.pack(anchor="center", fill=tk.X, padx=150)

    def close_window():
        print("Закрытие окна")
        window.destroy()

    def reset_timer():
        print("Обнуление таймера")
        global timer
        window.after_cancel(timer)
        timer = window.after(10000, close_window)

    window.bind("<Any-Button>", reset_timer)

    timer = window.after(10000, close_window)


if __name__ == "__main__":
    bfiles_recovery()
