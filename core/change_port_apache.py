import os
import traceback
import logging

from datetime import datetime


def change_port_apache(new_port) -> bool:
    try:
        from .process_off import Process
        from config import (
            get_value_disable_process_off,
            get_encoding,
            get_file_path_Apache
        )
        
        if not get_value_disable_process_off():
            Process.apache_process_off()
        
        file_encoding = get_encoding()
        file_path = get_file_path_Apache()

        # Считывает файл, чтобы сделать backup
        with open(file_path, "r", encoding=file_encoding) as file:
            src = file.readlines()

        # Если нету папки backup, то он её создает
        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        # Первоначальный бэкап менятся не будет
        backup_path = "backup/httpd.conf"
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding=file_encoding) as file:
                file.writelines(src)
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Creating an http.conf backup")
        
        # Создаем переменную, в которую будем вводить порт
        index_port_listen = None

        # Проходясь по циклу, скрипт ищет строку #Listen
        for i, line in enumerate(src):
            # Проверям не начинается строка с #, в ином случае просто игнорируем строку
            if not line.startswith("#"):
                # Если # нету, то он ищет слово Listen
                if "Listen" in src[i]:
                    print(i, line)
                    # Присваиваем переменную номер строки файла
                    index_port_listen = i

        # Меняем порт
        src[index_port_listen] = f"Listen {new_port}\n"

        # Создаем вторую переменную, в которую позже будем хранить новое значения порта
        index_port_servername = None

        for i, line in enumerate(src):
            if not line.startswith("#"):
                # если нет, то он продолжает считывать строку, иская слово ServerName
                if "ServerName" in src[i]:
                    print(i, line)
                    # Присваиваем номер строки файла в переменную
                    index_port_servername = i

        src[index_port_servername] = src[index_port_servername].split(":")
        src[index_port_servername][1] = f":{new_port}\n"
        result = "".join(src[index_port_servername])

        src[index_port_servername] = result

        # Сохраняем уже измененный файл
        with open(file_path, "w", encoding=file_encoding) as file:
            file.writelines(src)
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} :  Apache port change was successful")
        return True
        

    except Exception:
        # Переходим в исключения если возникла, какая нибудь ошибка

        tb = traceback.format_exc()
        def show_error(tb):
            from config import get_mode_run
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
    change_port_apache()
