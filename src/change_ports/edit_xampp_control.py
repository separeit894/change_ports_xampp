from tkinter import messagebox
import ctypes
import traceback
import sys
import os
import re


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, os.path.abspath(sys.argv[0]), None, 1)
    sys.exit(0)

def edit_file_xampp_control(apache_port, apachessl_port, mysql_port):
    try:
        count = 0
        print(apache_port, apachessl_port, mysql_port)
        print("Функция edit_file_xampp_control запущена!")

        file_path = "xampp-control.ini"  # можно заменить на полный путь, если нужно

        with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

        # Если нету папки backup, то он её создает
        if not os.path.exists("backup"):
            os.makedirs("backup")

        # Если нету резервного файла, то он его создает
        if not os.path.exists("backup/xampp-control.ini"):
            with open("backup/xampp-control.ini", "w", encoding="utf-8") as file:
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
            with open("xampp-control.ini", "w", encoding="utf-8", errors="ignore") as file:
                file.writelines(lines)
            print("Запись файла")
            if count > 1:
                messagebox.showinfo("Информация","Порты изменены успешно!")
            else:
                messagebox.showinfo("Информация","Порт изменен успешно!")

        return True
        
    except BaseException as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        print("Переход в исключения")
        tb = traceback.format_exc()
        messagebox.showerror("Обнаружена ошибка", f"{tb}")
    
        

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        edit_file_xampp_control()
        messagebox.showinfo("Информация","Порт изменен успешно!")
    else:
        print("Ошибка: Требуются права администратора.")
        run_as_admin()