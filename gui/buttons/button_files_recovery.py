from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from core import Recovery_Files


def bfiles_recovery(root, style):
    window = Toplevel(root)
    window.title("Меню восстановление файлов")
    window.geometry("500x300")
    recovery_files = Recovery_Files()
    # Восстановления файла Apache
    spaces_for_apache = "           "
    
    result_f_f_r_ap = recovery_files.file_recovery_apache
    button_apache = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apache}Apache",
        command=result_f_f_r_ap,
        style="Big.TButton",
    )
    
    if result_f_f_r_ap:
        messagebox.showinfo(
            "Успешное восстановление файла", "Файл Apache восстановлен!"
        )

    button_apache.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файла ApacheSSL
    result_r_f_f_r_a = recovery_files.file_recovery_apachessl
    spaces_for_apachessl = "        "
    button_apachessl = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apachessl}ApacheSSL",
        command=result_r_f_f_r_a,
        style="Big.TButton",
    )
    

    button_apachessl.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файлов MySQL
    result_r_f_f_r_m = recovery_files.file_recovery_mysql
    spaces_for_mysql = "           "
    button_mysql = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_mysql}MySQL",
        command=result_r_f_f_r_m,
        style="Big.TButton",
    )
    
    
    

    button_mysql.pack(anchor="center", fill=tk.X, padx=150)

    result_r_f_f_r_x = recovery_files.file_recovery_xampp_control
    # Восстановление файла xampp-control.ini
    button_xampp_control = ttk.Button(
        window,
        text="Восстановить файл\n    xampp-control.ini",
        command=result_r_f_f_r_x,
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
