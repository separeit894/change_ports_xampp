import os
import sys
import ctypes
import traceback
import importlib


console = False

if len(sys.argv) > 1:
    if sys.argv[1] == "--console":
        console = True
else:
    messagebox = importlib.import_module("tkinter.messagebox")


from ..change_ports.edit_xampp_control import run_as_admin
from ..shutting_down_processes import apache_process_off
from ..shutting_down_processes import apachessl_process_off
from ..shutting_down_processes import mysql_process_off
from ..shutting_down_processes import xampp_control_process_off

sys.path.append(os.path.join(os.path.dirname(__file__), "..\.."))


def file_recovery_apache():
    # Функция берет резервный файл, и записывает его данные в основной
    try:

        apache_process_off()

        backup_path = "backup/httpd.conf"
        with open(backup_path, "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        file_path = "apache/conf/httpd.conf"
        with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        print("File overwritten")

    except BaseException as e:
        if console:
            print(f"An error has been detected\n{traceback.format_exc()}")
        else:
            messagebox.showerror("Обнаружена ошибка", traceback.format_exc())

def file_recovery_apachessl():
    try:

        apachessl_process_off()

        backup_path = "backup/httpd-ssl.conf"
        with open(backup_path, "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        file_path = "apache/conf/extra/httpd-ssl.conf"
        with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        print("File overwritten")
    except BaseException as e:
        if console:
            print(f"An error has been detected\n{traceback.format_exc()}")
        else:
            messagebox.showerror("Обнаружена ошибка", traceback.format_exc())

def file_recovery_mysql():
    try:

        mysql_process_off()

        # Восстановление файла my.ini MySQL
        backup_path_ini = "backup/my.ini"
        with open(backup_path_ini, "r", encoding="utf-8", errors="ignore") as file:
            src = file.readlines()

        file_path_ini = "mysql/bin/my.ini"
        with open(file_path_ini, "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src)

        # Восстановление файла config.inc.php phpMyAdmin
        backup_path_php = "backup/config.inc.php" 
        with open(backup_path_php, "r", encoding="utf-8", errors="ignore") as file:
            src_config = file.readlines()

        file_path_php = "phpMyAdmin/config.inc.php"
        with open(file_path_php, "w", encoding="utf-8", errors="ignore") as file:
            file.writelines(src_config)
        
        print("File overwritten")

    except BaseException as e:
        if console:
            print(f"An error has been detected\n{traceback.format_exc()}")
        else:
            messagebox.showerror("Обнаружена ошибка", traceback.format_exc())


def file_recovery_xampp_control():
    if ctypes.windll.shell32.IsUserAnAdmin():
        try:
            
            xampp_control_process_off()

            backup_path = "backup/xampp-control.ini"
            with open(backup_path, "r", encoding="utf-8", errors="ignore") as file:
                src = file.readlines()

            file_path = "xampp-control.ini"
            with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
                file.writelines(src)
                
        except BaseException as e:
            if console:
                print(f"An error has been detected\n{traceback.format_exc()}")
            else:
                messagebox.showerror("Обнаружена ошибка", traceback.format_exc())
    else:
        print("Error: Administrator privileges are required.")
        run_as_admin()


if __name__ == "__main__":
    file_recovery_apache()
    file_recovery_apachessl()
    file_recovery_mysql()
    file_recovery_xampp_control()
    