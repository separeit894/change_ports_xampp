from datetime import datetime
from config import set_mode_run

import io
import os
import sys
import ctypes
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, filename="CPX.log")

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
        

def main():
    try:
        ensure_stdio()
        parser = argparse.ArgumentParser(
            description=
            "Change xampp ports for a program that can replace Apache, ApacheSSL, MySQL ports in XAMPP\n\
            Read on more Github: https://github.com/separeit894/change_ports_xampp\n\n"
        )
        

        parser.add_argument(
            '--console',
            action='store_true',
            help='Runs the program in CLI mode.'
        )
        
        parser.add_argument(
            '-v',
            '--version',
            action='store_true',
            help='Show the program version.'
        )
        
        parser.add_argument(
            '--no-admin',
            action='store_true',
            help='Remove the Administrator startup mode.'
        )
        
        parser.add_argument(
            '-e',
            '--encoding',
            type=str,
            help="Specifies the encoding to be used for reading and writing. The default is \"cp1251\""
        )
        
        
        # Парсим аргументы
        args = parser.parse_args()
        
        buf_help = io.StringIO()
        parser.print_help(file=buf_help)
        help_msg = buf_help.getvalue()
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --help : \n{help_msg}")
        
            
        if args.version:
            from config import version
            print(f"Change Ports Xampp : {version}")
            
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --version : {version}")
            sys.exit(0)
            
        if args.no_admin:
            import config
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --no_admin : disabling restart with administrator rights")
            config.rights_administrator = True
        
        if args.encoding:
            from config import set_encoding
            set_encoding(args.encoding)
            
            
        if args.console:
            from cli import CLI
            create_console()
            set_mode_run("CLI")
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : The program started in CLI mode")
            CLI().run_app()
            
        else:
            from gui import GUI
            set_mode_run("GUI")
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : The program started in GUI mode")
            GUI().run_app()
           
    except Exception as ex:
        import traceback
        print(traceback.format_exc())
    
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : Exception : main.py : \n{ex}")


if __name__ == "__main__":
    main()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : Close program")
        
    