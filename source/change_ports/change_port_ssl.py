import os
import sys
import traceback
import importlib

from ..shutting_down_processes import apachessl_process_off

console = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--console":
        console = True
else:
    messagebox = importlib.import_module("tkinter.messagebox")


def change_port_ssl(new_port):
    try:
        
        apachessl_process_off()

        # Сначала открываю файл, чтобы сделать его backup
        with open("apache/conf/extra/httpd-ssl.conf", "r", encoding="utf-8") as file:
            src = file.readlines()
        # Если нету папки backup, то он её создает
        if not os.path.exists("backup"):
            os.makedirs("backup")
        # Если нету резервного файла, то он его создает
        if not os.path.exists("backup/httpd-ssl.conf"):
            with open("backup/httpd-ssl.conf", "w", encoding="utf-8") as file:
                file.writelines(src)
        
        # Создаем переменную, в которой позже будем хранить значения нового порта
        index_listen = None

        
        # Цикл считывает файл, проходит по каждой строке
        # Внешнее условие проверяет - не начинается строка #, 
        # если он начинается #, то он пропускает строку файла
        # если нет, он начинает искать слово Listen,
        # и если он его находит, присваивает значения номера строки в переменную
        
        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "Listen" in src[i]:
                    print(i, line)
                    index_listen = i

        # В этой строке уже вводится новый порт, который ввел пользователь
        src[index_listen] = f"Listen {new_port}\n"

        # Новая переменная, которая будет хранить порт
        index_virtualhost = None

        
        # Тот же цикл, что и с 28 - 32 строку кода,
        # Так же проверяет не начинается строка #
        # если да, пропускает строку
        # если нет, переходит к внутреннему условие 
        # Но он уже ищет <VirtualHost _default_:
        # После : мы уже ставим другой порт
        
        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "<VirtualHost _default_:" in src[i]:
                    print(i, line)
                    index_virtualhost = i

        # Присваеваем переменной новый порт
        src[index_virtualhost] = f"<VirtualHost _default_:{new_port}>\n"

        # Переменная, которая будет хранить значение порта
        index_servername = None
        
        # Тот же самый цикл что и с 48 - 52 строку кода
        
        for i, line in enumerate(src):
            if not line.startswith("#"):
                if "ServerName" in src[i]:
                    print(i, line)
                    index_servername = i

        # Присваеваем строке, новый порт
        src[index_servername] = f"ServerName www.example.com:{new_port}\n"

        # Сохраняем изменный файл
        with open("apache/conf/extra/httpd-ssl.conf", "w", encoding="utf-8") as file:
            file.writelines(src)

        if console:
            print("Порт ApacheSSL изменен успешно!")
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
    change_port_ssl()