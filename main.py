from datetime import datetime
from config import (
    set_mode_run,
    create_config_json,
    use_config_json
)

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
        
        parser.add_argument(
            '--create-config',
            action="store_true",
            help="Creates a config in which you can enter the encoding and location of files. It will load it every time the program is started, if the configuration file is present. Not if it doesn't exist"
        )
        
        parser.add_argument(
            '--use-config',
            type=str,
            help="Creates a config in which you can enter the encoding and location of files. It will load it every time the program is started, if the configuration file is present. Not if it doesn't exist"
        )
        
        parser.add_argument(
            '--dpoff',
            '--disable-process-off',
            action="store_true",
            help="The argument disables shutting down processes"
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
            from config import set_value_rights_administrator
            
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : --no_admin : disabling restart with administrator rights")
            set_value_rights_administrator(True)
        
        if args.encoding:
            from config import set_encoding
            set_encoding(args.encoding)
        
        if args.create_config:
            create_config_json()
            sys.exit()
        
        if args.use_config:
            use_config_json(args.use_config)
        
        if args.dpoff:
            from config import set_value_disable_process_off
            set_value_disable_process_off(True)
                
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
        
    