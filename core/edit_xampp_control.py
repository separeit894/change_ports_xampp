import traceback
import os
import re
import logging

from config import Escape_Sequences
from config import file_encoding
from config import Colors
from .administrator_rights import run_as_admin
from .administrator_rights import is_admin

from datetime import datetime

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)


def edit_file_xampp_control(apache_port, apachessl_port, mysql_port) -> bool:
    try:
        from core import Process
        Process.xampp_control_process_off()

        count = 0
        file_path = "xampp-control.ini"  # можно заменить на полный путь, если нужно

        with open(file_path, "r", encoding=file_encoding) as file:
            lines = file.readlines()

        # Если нету папки backup, то он её создает
        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        # Если нету резервного файла, то он его создает
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
                break  # выходим из раздела

            if not in_section:
                continue
            
            def set_value_port(word: str, port: str) -> None:
                nonlocal count, line
                # Если переменная не имеет значения None, то переходит к внутреннему условию
                if not port == "None" and port != "":
                # Находим строго слово word
                    if re.search(fr"\b{word}\b", line):
                        # Дальше уже изменяем порт
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
    

    except Exception as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        tb = traceback.format_exc()
        print(f"Error \n{tb}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Error\n{tb}")
        return False


if __name__ == "__main__":
    if is_admin():
        edit_file_xampp_control()
    else:
        print("Error: Administrator privileges are required.")
        run_as_admin()
