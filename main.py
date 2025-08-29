from cli import CLI
from gui import GUI
from datetime import datetime
import os
import sys
import ctypes
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, filename="CPX.log")


executable = "CPX.exe" if sys.argv[0].endswith(".exe") or sys.argv[0].lower().endswith("x")  else "python main.py"
epilog = (
    f"Usage: {executable} [options]\n\n"
    "Description: \n"
    "  Change xampp ports for a program that can replace Apache, ApacheSSL, MySQL ports in XAMPP\n"
    "  Read on more Github: https://github.com/separeit894/change_ports_xampp\n\n"
    "Options: \n"
    "  --help, -h           Show this help message.\n"
    "  --version, -v        Show the program version.\n"
    "  --console            Runs the program in CLI mode.\n"
    "  --no_admin           Remove the Administrator startup mode.\n\n"
    "Examples: \n"
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
        parser = argparse.ArgumentParser(add_help=False)
        
        # Добавляем опцию --help
        parser.add_argument(
            "-h", 
            "--help", 
            action="store_true", 
            help="Show this message"
        )
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
        
        
        # Парсим аргументы
        
        args = parser.parse_args()
        if args.help:
            print(epilog)
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : main.py : --help : \n{epilog}")
            
            sys.exit(0)
            
            
        if args.version:
            from config import version
            print(f"Change Ports Xampp {version}")
            
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --version : {version}")
            sys.exit(0)
            
        if args.no_admin:
            import config
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --no_admin : disabling restart with administrator rights")
            config.rights_administrator = True

            
        #input("Нажмите Enter: ")

        # Решаем, что запускать
        if args.console:
            create_console()
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : The program started in CLI mode")
            CLI().run_app()
            #input("Нажмите Enter: ")
            
        else:
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : The program started in GUI mode")
            GUI().run_app()
            #input("Нажмите Enter: ")
           
    except Exception as ex:
        print(ex)
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : Exception : main.py : \n{ex}")
        # input("Нажмите Enter: ")


if __name__ == "__main__":
    try:
        main()
        # input("Нажмите Enter: ")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : Close program")
        
    except Exception as e:
        import traceback
        print(f"🚨 Критическая ошибка:\n{traceback.format_exc()}")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : Close Program with error\n{traceback.format_exc()}")
        # input("Нажмите Enter: ")
        