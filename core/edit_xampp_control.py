import ctypes
import traceback
import sys
import os
import re

import argparse

from config import Escape_Sequences
from config import file_encoding
from config import Colors


def is_admin():
    # Функция, которая проверяет запущена программа с правами администратора или нет
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    # Функция перезапускает скрипт в случае если скрипт до этого был запущен без прав администратора

    parser = argparse.ArgumentParser(
        description="Change Ports XAMPP — меняет порты Apache, MySQL и др."
    )
    
    # Добавляем опцию --console
    parser.add_argument(
        '--console',
        action='store_true',
        help='Запустить в консольном режиме (CLI)'
    )

    # Парсим аргументы
    args = parser.parse_args()

    if args.console:
        print(f"{os.path.abspath(sys.argv[0])} --console")
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            f"{os.path.abspath(sys.argv[0])} --console",
            None,
            1,
        )
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, os.path.abspath(sys.argv[0]), None, 1
        )
    sys.exit(0)

def edit_file_xampp_control(apache_port, apachessl_port, mysql_port) -> bool:
    try:
        from core import Process
        Process().xampp_control_process_off()

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
            
            def set_value_port(word: str, port: str):
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
        return True
    

    except BaseException as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        print("Entering exceptions")
        tb = traceback.format_exc()
        print(tb)
        return False

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        edit_file_xampp_control()
    else:
        print("Error: Administrator privileges are required.")
        run_as_admin()
