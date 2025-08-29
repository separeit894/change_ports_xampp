from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from core import Recovery_Files


def on_apache_click() -> None:
    result = Recovery_Files.file_recovery_apache()
    if result:
        messagebox.showinfo("Success", "The Apache file has already been restored!")
    
def on_apachessl_click() -> None:
    result = Recovery_Files.file_recovery_apachessl()
    if result:
        messagebox.showinfo("Success", "File ApacheSSL has already been restored!")

def on_mysql_click() -> None:
    result = Recovery_Files.file_recovery_mysql()
    if result:
        messagebox.showinfo("Success", "The MySQL file has already been restored!")
        

def on_xampp_control_click() -> None:
    result = Recovery_Files.file_recovery_xampp_control()
    if result:
        messagebox.showinfo("Success", "File xampp control has already been restored!")
        

def bfiles_recovery(root, style) -> None:
    window = Toplevel(root)
    window.title("File Recovery Menu")
    window.geometry("500x300")
    # Восстановления файла Apache
    spaces_for_apache = "           "
    
    
    button_apache = ttk.Button(
        window,
        text=f"Restore the file\n{spaces_for_apache}Apache",
        command=on_apache_click,
        style="Big.TButton",
    )
    

    button_apache.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файла ApacheSSL
    spaces_for_apachessl = "        "
    button_apachessl = ttk.Button(
        window,
        text=f"Restore the file\n{spaces_for_apachessl}ApacheSSL",
        command=on_apachessl_click,
        style="Big.TButton",
    )
    

    button_apachessl.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файлов MySQL
    spaces_for_mysql = "           "
    button_mysql = ttk.Button(
        window,
        text=f"Restore the file\n{spaces_for_mysql}MySQL",
        command=on_mysql_click,
        style="Big.TButton",
    )
    

    button_mysql.pack(anchor="center", fill=tk.X, padx=150)

    
    # Восстановление файла xampp-control.ini
    button_xampp_control = ttk.Button(
        window,
        text="Restore the file\n    xampp-control.ini",
        command=on_xampp_control_click,
        style="Big.TButton",
    )
    

    button_xampp_control.pack(anchor="center", fill=tk.X, padx=150)

    def close_window() -> None:
        print("Closing the window")
        window.destroy()

    def reset_timer() -> None:
        print("Resetting the timer")
        global timer
        window.after_cancel(timer)
        timer = window.after(10000, close_window)

    window.bind("<Any-Button>", reset_timer)

    timer = window.after(10000, close_window)


if __name__ == "__main__":
    bfiles_recovery()
