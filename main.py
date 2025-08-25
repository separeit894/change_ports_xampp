from cli import CLI
from gui import GUI
from datetime import datetime
import os
import sys
import ctypes
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, filename="CPX.log")

now = datetime.now()


executable = "CPX.exe" if sys.argv[0].endswith(".exe") or sys.argv[0].lower().endswith("x")  else "python main.py"
epilog = (
    "Examples:\n"
    f"  {executable}\n"
    f"  {executable} --no_admin\n"
    f"  {executable} --console\n"
    f"  {executable} --console --no_admin\n"
    f"  {executable} --version"
)

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
        #input("Нажмите Enter...")
        # print("="*50)
        # print("DEBUG: sys.argv =", sys.argv)
        # print("DEBUG: len(sys.argv) =", len(sys.argv))
        # print("="*50)
        # input("Нажмите Enter...")  # чтобы окно не закрылось
        parser = argparse.ArgumentParser(
            description="Change Ports XAMPP — меняет порты Apache, MySQL и др.",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=epilog
        )
        
        logging.info(parser.format_help())
        # Добавляем опцию --console
        parser.add_argument(
            '--console',
            action='store_true',
            help='Запустить в консольном режиме (CLI)'
        )
        
        # Добавляем опцию --version
        parser.add_argument(
            '-v',
            '--version',
            action='store_true',
            help='Узнать версию программы'
        )
        
        # Добавляем опцию --no-admin
        parser.add_argument(
            '--no_admin',
            action='store_true',
            help='Убрать режим запуска Администратора'
        )
        
        #print("sys.argv =", sys.argv)
        
        # Парсим аргументы
        
        args = parser.parse_args()
        if args.version:
            from config import version
            print(f"Change Ports Xampp {version}")
            
            logging.info(f"{now.strftime('%Y-%m-%d-%H-%M-%S')} : --version : {version}")
            sys.exit(0)
            
        if args.no_admin:
            import config
            logging.info(f"{now.strftime('%Y-%m-%d-%H-%M-%S')} : --no_admin : disabling restart with administrator rights")
            config.rights_administrator = True

            
        #input("Нажмите Enter: ")

        # Решаем, что запускать
        if args.console:
            create_console()
            logging.info("CLI run")
            CLI().run_app()
            #input("Нажмите Enter: ")
            
        else:
            logging.info("GUI run")
            GUI().run_app()
            #input("Нажмите Enter: ")
           
    except Exception as ex:
        print(ex)
        logging.info(f"{now.strftime('%Y-%m-%d-%H-%M-%S')} : Exception : main.py : \n{ex}")
        # input("Нажмите Enter: ")


if __name__ == "__main__":
    try:
        main()
        # input("Нажмите Enter: ")
        logging.info(f"{now.strftime('%Y-%m-%d-%H-%M-%S')} : Close program")
        
    except Exception as e:
        import traceback
        print(f"🚨 Критическая ошибка:\n{traceback.format_exc()}")
        logging.info(f"{now.strftime('%Y-%m-%d-%H-%M-%S')} : Close Program with error\n{traceback.format_exc()}")
        # input("Нажмите Enter: ")
        