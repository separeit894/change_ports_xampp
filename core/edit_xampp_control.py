import traceback
import os
import re
import logging

from config import get_mode_run

from .administrator_rights import (
    run_as_admin,
    is_admin
)

from datetime import datetime


def edit_file_xampp_control(apache_port, apachessl_port, mysql_port) -> bool:
    try:
        from core import Process
        from config import (
            get_value_disable_process_off,
            get_file_path_xampp_control_ini,
            get_encoding
        ) 
        
        if not get_value_disable_process_off():
            Process.xampp_control_process_off()

        count = 0

        file_path = get_file_path_xampp_control_ini()
        file_encoding = get_encoding()

        with open(file_path, "r", encoding=file_encoding) as file:
            lines = file.readlines()

        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        backup_path = "backup/xampp-control.ini"
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding=file_encoding) as file:
                file.writelines(lines)
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)}")

        in_section = False

        for i, line in enumerate(lines):
            line = line.strip()

            if line == "[ServicePorts]":
                in_section = True
                continue

            if in_section and line.startswith("["):
                break  

            if not in_section:
                continue
            
            def set_value_port(word: str, port: str) -> None:
                nonlocal count, line
    
                if not port == "None" and port != "":
                    if re.search(fr"\b{word}\b", line):
                        result = line.split("=")
                        result[1] = f"={port}"
                        line = "".join(result)
                        lines[i] = f"{line}\n"
                        print(f"Нашёл {word} на строке {i}: {lines[i]}")
                        count += 1
                        
            set_value_port("Apache", apache_port)
            set_value_port("ApacheSSL", apachessl_port)
            set_value_port("MySQL", mysql_port)


        with open(file_path, "w", encoding=file_encoding) as file:
            file.writelines(lines)
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : The port(s) change in xampp-control.ini was successful")
        return True
    

    except Exception:
        tb = traceback.format_exc()
        def show_error(tb):
            mode_run = get_mode_run()
            if mode_run == "CLI":
                print(f"Обнаружена ошибка : {tb}")
            else:
                print(f"Обнаружена ошибка : {tb}")
                from tkinter import messagebox
                messagebox.showerror("Обнаружена ошибка :", tb)
                
        show_error(tb)
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Error\n{tb}")
        return False


if __name__ == "__main__":
    if is_admin():
        edit_file_xampp_control()
    else:
        print("Error: Administrator privileges are required.")
        run_as_admin()
