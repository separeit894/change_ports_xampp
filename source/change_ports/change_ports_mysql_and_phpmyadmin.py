import os
import sys
import traceback
import importlib

from ..shutting_down_processes import mysql_process_off
from ..color_output import Colors
from ..config import Escape_Sequences
from ..config import file_encoding
from ..config import defining_value_mode

console, messagebox = None, None


def change_port_mysql(new_port):
    console, messagebox = defining_value_mode()
    try:
        mysql_process_off()

        # Сначала открываю файл, чтобы сделать его backup
        file_path = "mysql/bin/my.ini"
        with open(file_path, "r", encoding=file_encoding) as file:
            src = file.readlines()

        # Если нету папки backup, то он её создает
        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        # Если нету резервного файла, то он его создает
        backup_path_ini = "backup/my.ini"
        if not os.path.exists(backup_path_ini):
            with open(backup_path_ini, "w", encoding=file_encoding) as file:
                file.writelines(src)

        # Цикл считывает каждую строку файла
        for i, line in enumerate(src):
            # Если строка не начинается с #, то он переходит к внутреннему условию
            if not line.startswith("#"):
                # Если он находит слово port, присваевает новый порт
                if "port" in src[i]:
                    print(i, line)
                    src[i] = f"port={new_port}\n"

        # Сохраняет измененный файл
        with open(file_path, "w", encoding=file_encoding) as file:
            file.writelines(src)

        # Считываем другой файл
        file_path_php = "phpMyAdmin/config.inc.php"
        with open(file_path_php, "r", encoding=file_encoding) as file:
            src = file.readlines()

        # Если нету первого резервного файла, то он его создает
        backup_path_php = "backup/config.inc.php"
        if not os.path.exists(backup_path_php):
            with open(backup_path_php, "w", encoding=file_encoding) as file:
                file.writelines(src)

        # Новая переменная, которая будет в себе содержать измененное содержимое строки с портом
        index_cfg_server = None

        # Цикл считывает файл
        for i, line in enumerate(src):
            # Если строка не начинается с #, то он переходит к внутреннему условию
            if not line.startswith("#"):
                # Дальше он ищет $cfg['Servers'][$i]['port'], чтобы присвоить номер строки переменной
                if "$cfg['Servers'][$i]['port']" in src[i]:
                    print(i, line)
                    # Присваеваем значение этой строки
                    index_cfg_server = i
                    # меняем порт
                    src[i] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

        # В случае, если переменная пустая, то есть так и не нашла эту строку ( см. 52 строку кода )
        # то он эту строку создаст по умолчанию на 21 строке кода ( не знаю почему на 21, мне просто так захотелось )

        if index_cfg_server is None:
            src[21] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

        # Сохраняем результат
        with open(file_path_php, "w", encoding=file_encoding) as file:
            file.writelines(src)

        if console:
            print(
                f"{Escape_Sequences.double_new_line}{Colors.GREEN}MySQL port changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
            )
        else:
            messagebox.showinfo("Информация", "Порт изменен успешно!")

    except BaseException as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        print("Entering exceptions")
        tb = traceback.format_exc()

        if console:
            print(
                f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
            )
        else:
            messagebox.showerror("Обнаружена ошибка!", f"{tb}")


if __name__ == "__main__":
    change_port_mysql()
