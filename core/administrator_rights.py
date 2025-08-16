import ctypes
import os
import sys

def is_admin():
    # Функция, которая проверяет запущена программа с правами администратора или нет
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """Перезапускает скрипт с правами администратора."""
    executable = sys.executable
    script = os.path.abspath(sys.argv[0])
    
    # Формируем строку аргументов: только флаги, без мусора
    args = []
    
    # Сохраняем только настоящие флаги (начинающиеся с --)
    for arg in sys.argv[1:]:
        if arg.startswith('--') or arg.startswith('-'):
            args.append(arg)
    
    # Собираем команду: python путь_к_скрипту [аргументы]
    cmd = f'"{executable}" "{script}"'
    if args:
        cmd += " " + " ".join(args)
    
    # Запускаем от имени администратора
    ret = ctypes.windll.shell32.ShellExecuteW(
        None,           # hwnd
        "runas",        # действие: запуск от админа
        executable,     # программа (python.exe)
        cmd,            # команда (с аргументами)
        None,           # рабочая папка
        1               # показать окно
    )
    
    # Если ошибка — например, отменили UAC
    if ret <= 32:
        print("❌ Не удалось запустить от имени администратора")
        sys.exit(1)
    
    sys.exit(0)
    
if __name__ == "__main__":
    try:
        is_admin()
        run_as_admin()
    except Exception as ex:
        print(ex)