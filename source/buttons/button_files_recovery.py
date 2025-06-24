import os
import sys

from tkinter import Toplevel
from tkinter import ttk
import tkinter as tk

from ..change_ports.file_recovery import *


sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))


def bfiles_recovery(root, style):
    window = Toplevel(root)
    window.title("Меню восстановление файлов")
    window.geometry("500x300")

    # Восстановления файла Apache
    spaces_for_apache = "           "
    button_apache = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apache}Apache",
        command=file_recovery_apache,
        style="Big.TButton",
    )

    button_apache.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файла ApacheSSL
    spaces_for_apachessl = "        "
    button_apachessl = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_apachessl}ApacheSSL",
        command=file_recovery_apachessl,
        style="Big.TButton",
    )

    button_apachessl.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файлов MySQL
    spaces_for_mysql = "           "
    button_mysql = ttk.Button(
        window,
        text=f"Восстановить файл\n{spaces_for_mysql}MySQL",
        command=file_recovery_mysql,
        style="Big.TButton",
    )

    button_mysql.pack(anchor="center", fill=tk.X, padx=150)

    # Восстановление файла xampp-control.ini
    button_xampp_control = ttk.Button(
        window,
        text="Восстановить файл\n    xampp-control.ini",
        command=file_recovery_xampp_control,
        style="Big.TButton",
    )

    button_xampp_control.pack(anchor="center", fill=tk.X, padx=150)


if __name__ == "__main__":
    bfiles_recovery()
