import ctypes
import os
import sys
import logging

from datetime import datetime

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)

def is_admin() -> bool:
    # Функция, которая проверяет запущена программа с правами администратора или нет
    from config import rights_administrator
    try:
        return bool(rights_administrator)
    except:
        return False


def run_as_admin() -> None:
    """Перезапускает скрипт с правами администратора."""
    
    executable = sys.executable
    # print("executable: ", executable)
    
    
    # Формируем строку аргументов: только флаги, без мусора
    args = []
    
    # Сохраняем только настоящие флаги (начинающиеся с --)
    #print("sys.argv[1: ] : ", sys.argv[1:])
    for arg in sys.argv[1:]:
        if arg.startswith('--') == True or arg.startswith('-') == True:
            args.append(arg)
    
    # Собираем команду: python путь_к_скрипту [аргументы]
    
    cmd = ""
    if args:
        for i in args:
            cmd += i+" "
    
    #print("cmd: ", cmd)
    # Запускаем от имени администратора

   
    ret = ctypes.windll.shell32.ShellExecuteW(
        None,           # hwnd
        "runas",        # действие: запуск от админа
        executable,     # программа (python.exe)
        os.path.abspath(0) + "\main.py " + cmd if sys.argv[0].endswith(".py") else cmd,  # команда (с аргументами)
        None,           # рабочая папка
        1               # показать окно
    )
    
    
    # Если ошибка — например, отменили UAC
    if ret <= 32:
        print("❌ Не удалось запустить от имени администратора")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : ❌ Не удалось запустить от имени администратора : ret = {ret} ")
        sys.exit(1)
        
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Restarting with adaministrator rights")
    sys.exit(0)
    
if __name__ == "__main__":
    try:
        is_admin()
        run_as_admin()
    except Exception as ex:
        print(ex)