import ctypes
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
    print(apache_port, apachessl_port, mysql_port)
    print("Функция edit_file_xampp_control запущена!")

    file_path = "xampp-control.ini"  # можно заменить на полный путь, если нужно

    if not os.path.exists(file_path):
        print(f"[Ошибка] Файл {file_path} не найден!")
        return

    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

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
        if not apache_port == "None":
            # Находим строго слово "Apache" и так далее
            if re.search(r'\bApache\b', line):
                apache_line_index = i
                result = line.split("=")
                result[1] = f"={apache_port}"
                line = "".join(result)
                lines[i] = f"{line}\n"
                print(f"Нашёл Apache на строке {i}: {lines[i]}")

        if not apachessl_port == "None":
            if re.search(r'\bApacheSSL\b', line):
                apachessl_line_index = i
                result = line.split("=")
                result[1] = f"={apachessl_port}"
                line = "".join(result)
                lines[i] = f"{line}\n"
                print(f"Нашёл ApacheSSL на строке {i}: {lines[i]}")
                
        if not mysql_port == "None":      
            if re.search(r'\bMySQL\b', line):
                mysql_line_index = i
                result = line.split("=")
                result[1] = f"={mysql_port}"
                line = "".join(result)
                lines[i] = f"{line}\n"
                print(f"Нашёл MySQL на строке {i}: {lines[i]}")

    # Записываем изменения в файл
    with open("xampp-control.ini", "w", encoding="utf-8") as file:
        file.writelines(lines)
    print("Запись файла")


if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        edit_file_xampp_control()
    else:
        print("Ошибка: Требуются права администратора.")
        run_as_admin()