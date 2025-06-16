import ctypes
import traceback
import sys
import os
import re
import importlib


from ..shutting_down_processes import xampp_control_process_off

console = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--console":
        console = True
else:
    messagebox = importlib.import_module("tkinter.messagebox")


def is_admin():
    # Функция, которая проверяет запущена программа с правами администратора или нет
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    # Функция перезапускает скрипт в случае если скрипт до этого был запущен без прав администратора
    if len(sys.argv) > 1:
        print(sys.argv[1])
        if "--console" in sys.argv:
            print("провериал условие")
            global console
            console = True

    if console:
        print("Запускаю консоль")
        print(f"{os.path.abspath(sys.argv[0])} --console")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"{os.path.abspath(sys.argv[0])} --console", None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.abspath(sys.argv[0]), None, 1)
    sys.exit(0)


def edit_file_xampp_control(apache_port, apachessl_port, mysql_port):
    try:
        
        xampp_control_process_off()

        count = 0
        file_path = "xampp-control.ini"  # можно заменить на полный путь, если нужно

        with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

        # Если нету папки backup, то он её создает
        backup = "backup"
        if not os.path.exists(backup):
            os.makedirs(backup)

        # Если нету резервного файла, то он его создает
        backup_path = "backup/xampp-control.ini"
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding="utf-8") as file:
                file.writelines(lines)

        in_section = False
        apache_line_index = apachessl_line_index = mysql_line_index = None

        for i, line in enumerate(lines):
            line = line.strip()

            if line == "[ServicePorts]":
                in_section = True
                continue

            if in_section and line.startswith("["):
                break  # выходим из раздела

            if not in_section:
                continue

            # Если переменная не имеет значения None, то переходит к внутреннему условию
            if not apache_port == "None" and apache_port != "":
                # Находим строго слово "Apache" и так далее
                if re.search(r'\bApache\b', line):
                    apache_line_index = i
                    result = line.split("=")
                    result[1] = f"={apache_port}"
                    line = "".join(result)
                    lines[i] = f"{line}\n"
                    print(f"Нашёл Apache на строке {i}: {lines[i]}")
                    count += 1

            if not apachessl_port == "None" and apachessl_port != "":
                if re.search(r'\bApacheSSL\b', line):
                    apachessl_line_index = i
                    result = line.split("=")
                    result[1] = f"={apachessl_port}"
                    line = "".join(result)
                    lines[i] = f"{line}\n"
                    print(f"Нашёл ApacheSSL на строке {i}: {lines[i]}")
                    count += 1
                    
            if not mysql_port == "None" and mysql_port != "":      
                if re.search(r'\bMySQL\b', line):
                    mysql_line_index = i
                    result = line.split("=")
                    result[1] = f"={mysql_port}"
                    line = "".join(result)
                    lines[i] = f"{line}\n"
                    print(f"Нашёл MySQL на строке {i}: {lines[i]}")

                    count += 1

        # Записываем изменения в файл
        if count > 0:
            with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
                file.writelines(lines)
            print("Writing file")
            if console:
                if count > 1:
                    print("Ports changed successfully!")
                else:
                    print("Port changed successfully!")

            else:
                if count > 1:
                    messagebox.showinfo("Информация","Порты изменены успешно!")
                else:
                    messagebox.showinfo("Информация","Порт изменен успешно!")
        
    except BaseException as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        print("Entering exceptions")
        tb = traceback.format_exc()

        if console:
            print(f"An error has been detected!\n{tb}")
        else:
            messagebox.showerror("Обнаружена ошибка", f"{tb}")
    
        

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        edit_file_xampp_control()
        messagebox.showinfo("Информация","Порт изменен успешно!")
    else:
        print("Error: Administrator privileges are required.")
        run_as_admin()