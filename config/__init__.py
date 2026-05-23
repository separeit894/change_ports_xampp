import ctypes
import codecs
import sys
import os
import logging

from datetime import datetime

logging.basicConfig(level=logging.DEBUG, filename="CPX.log")

# для вывода в консоль
class Escape_Sequences:
    new_line = "\n"
    double_new_line = "\n\n"
    tab = "\t"
    
# Цвета для вывода в консоль ( Ошибки и прочее )
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"

file_encoding = "cp1252"

def set_encoding(encoding: str):
    global file_encoding
    try:
        codecs.lookup(encoding)
        file_encoding = encoding
        print("Successful encoding change")
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful encoding change")
    except LookupError:
        print("There is no such encoding")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : There is no such encoding")
        sys.exit(1)
        
def get_encoding() -> str:
    return file_encoding
    
# Версия скрипта
version = "v-4.4.1"

# Режим, в котором запущена программа (GUI\CLI) По умолчанию GUI
mode_run = "GUI"

def set_mode_run(mode: str) -> str:
    global mode_run
    mode_run = mode
    return mode_run

def get_mode_run() -> str:
    return mode_run

# Rights Administrator
rights_administrator = ctypes.windll.shell32.IsUserAnAdmin()

__all__ = [
    "Escape_Sequences",
    "Colors",
    "file_encoding",
    "rights_administrator"
]



