import os
import sys
import logging

from datetime import datetime

from config import (
    Escape_Sequences,
    Colors
)

def is_admin() -> bool:
    # Проверяет запущена программа с правами администратора
    from config import get_value_rights_administrator
    
    result : bool = get_value_rights_administrator()
    return result
    


def run_as_admin() -> None:
    """Перезапускает скрипт с правами администратора."""
    import ctypes
    executable = sys.executable
    print("executable: ", executable)
    # Формируем строку аргументов: только флаги, без мусора
    args = []
    
    # Сохраняем только настоящие флаги (начинающиеся с -- или с -)
    print(f"sys.argv[1: ] :  {sys.argv[1:]}")
    for arg in sys.argv[1:]:
        if arg.startswith('--') == True or arg.startswith('-') == True:
            args.append(arg)
    
    # Собираем команду: python путь_к_скрипту [аргументы]
    cmd = ""
    if args:
        for i in args:
            cmd += i+" "
    
    print("cmd: ", cmd)
    # Запускаем от имени администратора
    ret = ctypes.windll.shell32.ShellExecuteW(
        None,           # hwnd
        "runas",        # действие: запуск от админа
        executable,     # программа (python.exe)
        os.path.abspath("") + "\main.py " + cmd if sys.argv[0].endswith(".py") else cmd,  # команда (с аргументами)
        None,           # рабочая папка
        1               # показать окно
    )
    
    # Если ошибка — например, отменили UAC
    if ret <= 32:
        print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}Не удалось запустить от имени администратора{Colors.RESET}{Escape_Sequences.new_line}")
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