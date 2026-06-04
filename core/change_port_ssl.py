import os
import traceback
import logging

from config import (
    Escape_Sequences,
    Colors,
    get_mode_run
)

from datetime import datetime


def change_port_ssl(new_port) -> bool:
    try:
        from core import Process
        from config import (
            get_value_disable_process_off,
            get_file_path_ApacheSSL,
            get_encoding
        ) 
        
        if not get_value_disable_process_off():
            Process.apachessl_process_off()

        file_encoding = get_encoding()
        file_path = get_file_path_ApacheSSL()
        # Открыть файл, чтобы сделать его backup
        with open(file_path, "r", encoding=file_encoding) as file:
            src = file.readlines()
            
        # Если нету папки backup, то он её создает
        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        # Если нету резервного файла, то он его создает
        backup_path = "backup/httpd-ssl.conf"
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding=file_encoding) as file:
                file.writelines(src)
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Creating a backup of the http-ssl.conf file")

        # Создаем переменную, в которой позже будем хранить значения нового порта
        index_listen = None

        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "Listen" in src[i]:
                    print(i, line)
                    index_listen = i

        # Строка с новым портом
        src[index_listen] = f"Listen {new_port}\n"

        # Новая переменная, которая будет хранить порт
        index_virtualhost = None

        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "<VirtualHost _default_:" in src[i]:
                    print(i, line)
                    index_virtualhost = i

        # Строка с новым портом
        src[index_virtualhost] = f"<VirtualHost _default_:{new_port}>\n"

        # Переменная, которая будет хранить значение порта
        index_servername = None

        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "ServerName" in src[i]:
                    print(i, line)
                    index_servername = i

        # Новый порт
        src[index_servername] = f"ServerName www.example.com:{new_port}\n"

        # Сохранение
        with open(file_path, "w", encoding=file_encoding) as file:
            file.writelines(src)
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful modification of the ApacheSSL port")
        return True


    except Exception:

        # Переходим в исключения если возникла, какая нибудь ошибка
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
    change_port_ssl()
