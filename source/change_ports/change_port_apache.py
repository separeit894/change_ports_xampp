import os
import sys
import traceback
import importlib

console = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--console":
        console = True
else:
    messagebox = importlib.import_module("tkinter.messagebox")

from ..shutting_down_processes import apache_process_off


def change_port_apache(new_port):
    try:
        
        apache_process_off()

        # Cначала считываю файл, чтобы сделать backup
        with open("apache/conf/httpd.conf", 'r', encoding="utf-8") as file:
            src = file.readlines()

        # Если нету папки backup, то он её создает
        if not os.path.exists("backup"):
            os.makedirs("backup")
        
        # Если до этого порты менялись, то уже есть первоначальный бэкап,
        # и заменятся он не будет. Это делается для того чтобы сохранить рабочий вариант файла,
        # перезаписывание возможно приведет к неисправной обработке файла xampp
        
        if not os.path.exists("backup/httpd.conf"):
            with open("backup/httpd.conf", "w", encoding="utf-8") as file:
                file.writelines(src)

        # Создаем переменную в которую будем вводить порт
        index_port_listen = None

        # Проходясь по циклу, скрипт ищет строку #Listen
        # Чтобы затем заменить порт
        
        for i, line in enumerate(src):
            # Проверям не начинается строка с #, в ином случае просто игнорируем строку
            if not line.startswith("#"):
                # Если # нету, то он ищет слово Listen
                if "Listen" in src[i]:
                    print(i, line)
                    # Присваеваем переменную номер строки файла
                    index_port_listen = i

        # Меняем порт
        src[index_port_listen] = f"Listen {new_port}\n"

        # Создаем вторую переменную, в которую позже будем хранить новое значения порта
        index_port_servername = None

        # Цикл считывает строки файла,
        # в if проверяется не начинается файл с #, 
        # если да, то он пропускает строку
        # если нет, то он продолжает считывать строку, иская слово ServerName
        
        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "ServerName" in src[i]:
                    print(i, line)
                    # Присваевам номер строки файла в переменную
                    index_port_servername = i

        src[index_port_servername] = src[index_port_servername].split(":")
        src[index_port_servername][1] = f":{new_port}\n"
        result = "".join(src[index_port_servername])

        src[index_port_servername] = result

        # Сохраняем уже измененный файл
        with open("apache/conf/httpd.conf", "w", encoding="utf-8") as file:
            file.writelines(src)
        
        if console:
            print("Порт Apache изменен успешно!")
        else:
            messagebox.showinfo("Информация","Порт изменен успешно!")
        
        
    except BaseException as e:
        # Переходим в исключения если возникла, какая нибудь ошибка
        print("Переход в исключения")
        tb = traceback.format_exc()
        if console:
            print(f"Обнаружена ошибка!\n{tb}")
        else:
            messagebox.showerror("Обнаружена ошибка!", f"{tb}")
    


if __name__ == "__main__":
    change_port_apache()