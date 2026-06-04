import os
import traceback
import logging

from datetime import datetime

from config import get_mode_run


def change_port_mysql(new_port) -> bool:
    try:
        from core import Process
        from config import (
            get_value_disable_process_off,
            get_file_path_MySQLINI,
            get_file_path_PhpMyAdminConfig,
            get_encoding
        )
        
        if not get_value_disable_process_off():
            Process.mysql_process_off()


        file_path = get_file_path_MySQLINI()
        file_encoding = get_encoding()

        # Открыть файл, чтобы сделать его backup ( MySQL )
        with open(file_path, "r", encoding=file_encoding) as file:
            src = file.readlines()

        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        backup_path_ini = "backup/my.ini"
        if not os.path.exists(backup_path_ini):
            with open(backup_path_ini, "w", encoding=file_encoding) as file:
                file.writelines(src)
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Creating a backup of my.ini MySQL file")

        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "port" in src[i]:
                    print(i, line)
                    src[i] = f"port={new_port}\n"

        # Сохраняет измененный файл
        with open(file_path, "w", encoding=file_encoding) as file:
            file.writelines(src)

        # Считываем другой файл (PhpMyAdmin)

        file_path_php = get_file_path_PhpMyAdminConfig()

        with open(file_path_php, "r", encoding=file_encoding) as file:
            src = file.readlines()

        backup_path_php = "backup/config.inc.php"
        if not os.path.exists(backup_path_php):
            with open(backup_path_php, "w", encoding=file_encoding) as file:
                file.writelines(src)
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Creating a backup config.ini.php the phpMyAdmin file")

        # Новая переменная, которая будет в себе содержать измененное содержимое строки с портом
        index_cfg_server = None

        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "$cfg['Servers'][$i]['port']" in src[i]:
                    print(i, line)
                    index_cfg_server = i
                    
                    src[i] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

        """
        В случае, если переменная пустая,
        то он эту строку создаст по умолчанию на 21 строке кода
        """

        if index_cfg_server is None:
            src[21] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

        # Сохраняем результат
        with open(file_path_php, "w", encoding=file_encoding) as file:
            file.writelines(src)
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : MySQL port change was successful")
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
    change_port_mysql()
