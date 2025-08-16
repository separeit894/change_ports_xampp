from cli import CLI
from gui import GUI
import os
import sys

import ctypes

import argparse



def ensure_stdio():
    """Восстанавливает sys.stdout и sys.stderr, если они None (актуально для pythonw)"""
    if sys.stdout is None or not hasattr(sys.stdout, "write"):
        try:
            sys.stdout = open("CONOUT$", "w", encoding="utf-8") if os.name == "nt" else open("/dev/tty", "w")
        except:
            sys.stdout = open(os.path.devnull, "w")
    if sys.stderr is None or not hasattr(sys.stderr, "write"):
        try:
            sys.stderr = open("CONOUT$", "w", encoding="utf-8") if os.name == "nt" else open("/dev/tty", "w")
        except:
            sys.stderr = sys.stdout or open(os.path.devnull, "w")

def create_console():
    ctypes.windll.kernel32.AllocConsole()
    sys.stdout = open("CONOUT$", "w")  
    sys.stderr = open("CONOUT$", "w")
    sys.stdin = open("CONIN$", "r")
        
# Функция проверяет запущена CLI или GUI
def main():
    try:
        
        ensure_stdio()
        #print("="*50)
        #print("DEBUG: sys.argv =", sys.argv)
        #print("DEBUG: len(sys.argv) =", len(sys.argv))
        #print("="*50)
        #input("Нажмите Enter...")  # чтобы окно не закрылось
        parser = argparse.ArgumentParser(
            description="Change Ports XAMPP — меняет порты Apache, MySQL и др."
        )
        
        # Добавляем опцию --console
        parser.add_argument(
            '--console',
            action='store_true',
            help='Запустить в консольном режиме (CLI)'
        )
        #print("sys.argv =", sys.argv)
        filtered_args = [arg for arg in sys.argv[1:] if arg != sys.argv[0]]
        # Парсим аргументы
        args = parser.parse_args(filtered_args)

        # Решаем, что запускать
        if args.console:
            create_console()
            CLI().run_app()
            
        else:
            
            GUI().run_app()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        print(f"🚨 Критическая ошибка:\n{traceback.format_exc()}")
        