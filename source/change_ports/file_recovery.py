import os
import sys
import ctypes
import traceback

from tkinter import messagebox

from ..change_ports.edit_xampp_control import run_as_admin

sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))


def file_recovery_apache():
    # Функция берет резервный файл, и записывает его данные в основной
    try:
        with open("backup/httpd.conf", "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        with open("apache/conf/httpd.conf", "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        print("Файл перезаписан")

    except BaseException as e:
        messagebox.showerror("Обнаружена ошибка", traceback.format_exc())

def file_recovery_apachessl():
    try:
        with open("backup/httpd-ssl.conf", "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        with open("apache/conf/extra/httpd-ssl.conf", "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        print("Файл перезаписан")
    except BaseException as e:
        messagebox.showerror("Обнаружена ошибка", traceback.format_exc())

def file_recovery_mysql():
    try:
        # Восстановление файла my.ini MySQL
        with open("backup/my.ini", "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        with open("mysql/bin/my.ini", "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        # Восстановление файла config.inc.php phpMyAdmin
        with open("backup/config.inc.php", "r", encoding="utf-8", errors="ignore") as file:
            src_config = file.readlines()

        with open("phpMyAdmin/config.inc.php", "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src_config)
        
        print("Файл перезаписан")

    except BaseException as e:
        messagebox.showerror("Обнаружена ошибка", traceback.format_exc())


def file_recovery_xampp_control():
    if ctypes.windll.shell32.IsUserAnAdmin():
        try:
            with open("backup/xampp-control.ini", "r", encoding="utf-8", errors="ignore") as file:
                src = file.readlines()

            with open("xampp-control.ini", "w", encoding="utf-8", errors="ignore") as file:
                file.writelines(src)
                
        except BaseException as e:
            messagebox.showerror("Обнаружена ошибка", traceback.format_exc())
    else:
        print("Ошибка: Требуются права администратора.")
        run_as_admin()


if __name__ == "__main__":
    file_recovery_apache()
    file_recovery_apachessl()
    file_recovery_mysql()
    file_recovery_xampp_control()
    