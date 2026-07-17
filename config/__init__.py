import codecs
import os
import sys
import logging
import json 

from datetime import datetime


# для вывода в консоль
class Escape_Sequences:
    new_line = "\n"
    double_new_line = "\n\n"
    tab = "\t"
    
# Цвета для вывода в консоль ( Ошибки и прочее )
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"

FILE_CONFIG = "config.json"         

file_encoding = "cp1252"

def set_encoding(encoding: str):
    global file_encoding
    try:
        codecs.lookup(encoding)
        file_encoding = encoding
        def show_info():
            mode_run = get_mode_run()
            result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful encoding change: {file_encoding}{Colors.RESET}{Escape_Sequences.new_line}"
            if mode_run == "CLI":
                print(result)
            else:
                print(result)
                from tkinter import messagebox
                messagebox.showinfo("Результат", f"Successful encoding change: {file_encoding}")
                
        show_info()
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful encoding change")
            
    except Exception:
        print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}There is no such encoding: {encoding}{Colors.RESET}{Escape_Sequences.new_line}")
        import traceback
        tb =traceback.format_exc()
        def show_error(tb):
            mode_run = get_mode_run()
            result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Обнаружена ошибка : {tb}{Colors.RESET}{Escape_Sequences.new_line}"
            if mode_run == "CLI":
                print(result)
            else:
                print(result)
                from tkinter import messagebox
                messagebox.showerror("Обнаружена ошибка :", tb)
                
        show_error(tb)
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : There is no such encoding")
        
        
def get_encoding() -> str:
    return file_encoding
    
# Версия скрипта
version = "v-4.5.6"

# Режим, в котором запущена программа (GUI\CLI). По умолчанию GUI
mode_run = "GUI"

def set_mode_run(mode: str) -> str:
    global mode_run
    mode_run = mode
    return mode_run

def get_mode_run() -> str:
    return mode_run

rights_administrator = None

def create_value_rights_administrator():
    global rights_administrator
    import ctypes 
    rights_administrator = ctypes.windll.shell32.IsUserAnAdmin()

def set_value_rights_administrator(value: bool):
    global rights_administrator
    rights_administrator = value
   
def get_value_rights_administrator():
    return rights_administrator

# Apache

file_path_Apache = "apache/conf/httpd.conf" 

def set_file_path_Apache(file_path: str):
    global file_path_Apache
    
    file_path_Apache = file_path
    def show_info():
        mode_run = get_mode_run()
        result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful Apache Path change: {file_path_Apache}{Colors.RESET}{Escape_Sequences.new_line}"
        if mode_run == "CLI":
            print(result)
        else:
            print(result)
            from tkinter import messagebox
            messagebox.showinfo("Результат", f"Successful Apache path change: {file_path_Apache}")
            
    show_info()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful change apache path")
    
    
def get_file_path_Apache() -> str:
    return file_path_Apache

file_path_ApacheSSL = "apache/conf/extra/httpd-ssl.conf" 

def set_file_path_ApacheSSL(file_path: str):
    global file_path_ApacheSSL
    
    file_path_ApacheSSL = file_path
    def show_info():
        mode_run = get_mode_run()
        result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful ApacheSSL path change: {file_path_ApacheSSL}{Colors.RESET}{Escape_Sequences.new_line}"
        if mode_run == "CLI":
            print(result)
        else:
            print(result)
            from tkinter import messagebox
            messagebox.showinfo("Результат", f"Successful ApacheSSL path change: {file_path_ApacheSSL}")
            
    show_info()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful change apacheSSL path")
    
def get_file_path_ApacheSSL() -> str:
    return file_path_ApacheSSL

file_path_mysql_ini = "mysql/bin/my.ini" 

def set_file_path_MySQLIni(file_path: str):
    global file_path_mysql_ini
    
    file_path_mysql_ini = file_path
    def show_info():
        mode_run = get_mode_run()
        result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful MySQL INI path change: {file_path_mysql_ini}{Colors.RESET}{Escape_Sequences.new_line}"
        if mode_run == "CLI":
            print(result)
        else:
            print(result)
            from tkinter import messagebox
            messagebox.showinfo("Результат", f"Successful MySQL INI path change: {file_path_mysql_ini}")
            
    show_info()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful change MySQL INI path")


def get_file_path_MySQLINI() -> str:
    return file_path_mysql_ini

file_path_php = "phpMyAdmin/config.inc.php" 

def set_file_path_PhpMyAdminConfig(file_path: str):
    global file_path_php
    
    file_path_php = file_path
    def show_info():
        mode_run = get_mode_run()
        result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful PhpMyAdmin Config path change: {file_path_php}{Colors.RESET}{Escape_Sequences.new_line}"
        if mode_run == "CLI":
            print(result)
        else:
            print(result)
            from tkinter import messagebox
            messagebox.showinfo("Результат", f"Successful PhpMyAdmin Config path change: {file_path_php}")
            
    show_info()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful change PhpMyAdmin Config path")


def get_file_path_PhpMyAdminConfig() -> str:
    return file_path_php

file_path_xampp_control_ini = "xampp-control.ini" 

def set_file_path_xampp_control_ini(file_path: str):
    global file_path_xampp_control_ini
    
    file_path_xampp_control_ini = file_path
    def show_info():
        mode_run = get_mode_run()
        result = f"{Escape_Sequences.double_new_line}{Colors.BOLD}Successful xampp control ini path change: {file_path_xampp_control_ini}{Colors.RESET}{Escape_Sequences.new_line}"
        if mode_run == "CLI":
            print(result)
        else:
            print(result)
            from tkinter import messagebox
            messagebox.showinfo("Результат", f"Successful xampp control ini path change: {file_path_xampp_control_ini}")
            
    show_info()
    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Successful change xampp control ini path")


def get_file_path_xampp_control_ini() -> str:
    return file_path_xampp_control_ini

def create_config_json():
    if os.path.exists(FILE_CONFIG):
        print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}Config file {FILE_CONFIG} exists here, Pass...{Colors.RESET}{Escape_Sequences.new_line}")
        
    else:
        with open(FILE_CONFIG, "w") as f:
            json.dump(
                {
                    "Auto-Load": "n",
                    "Encoding": get_encoding(),
                    "Apache Path": get_file_path_Apache(),
                    "ApacheSSL Path": get_file_path_ApacheSSL(),
                    "MySQL Path": get_file_path_MySQLINI(),
                    "PhpMyAdmin Config": get_file_path_PhpMyAdminConfig(),
                    "Xampp Control INI": get_file_path_xampp_control_ini()
                },
                f,
                indent=4
            ),
        return False

def use_config_json(config_file: str, get_auto_load_value: str = 'n'):
    try:
        if os.path.exists(config_file):
            global file_encoding, file_path_Apache, file_path_ApacheSSL, file_path_mysql_ini, file_path_php, file_path_xampp_control_ini
            print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}A config file with this name exists{Colors.RESET}{Escape_Sequences.new_line}")
            with open(config_file, "r") as f:
                result: dict = json.load(f)
            
            print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}RESULT LOAD CONFIG FILE : {config_file}{Colors.RESET}{Escape_Sequences.new_line}{result}{Escape_Sequences.new_line}")
            
            if get_auto_load_value == 'y':

                auto_load_config_file = result.get("Auto-Load")
                print(f"auto_load_config_file : {auto_load_config_file}")
                if auto_load_config_file == 'y': 
                    return True
                else: return False
                
            else: pass
            
            
            file_encoding = result.get("Encoding")
            # Проверяет на существование кодировки
            codecs.lookup(file_encoding)
            
            file_path_Apache = result.get("Apache Path")
            file_path_ApacheSSL = result.get("ApacheSSL Path")
            file_path_mysql_ini = result.get("MySQL Path")
            file_path_php = result.get("PhpMyAdmin Config")
            file_path_xampp_control_ini = result.get("Xampp Control INI")
        else:
            print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}A config file with this name {config_file} does not exist!{Colors.RESET}{Escape_Sequences.new_line}")
            sys.exit(1)
    
    except LookupError:
        print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}Encoding : {file_encoding} is incorrect or does not exist.{Colors.RESET}{Escape_Sequences.new_line}")
        sys.exit(1)
            
def check_platform(get_system: bool = False):
    from platform import system
    os_name = system()
    if not get_system:
        if os_name == "Windows":
            from core import is_admin
            return is_admin()
        elif os_name == "Linux":
            return True
        else:
            return True
    else:
        return os_name
    
if check_platform(True) == "Windows":
    # print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}Значение переменной rights administrator задано{Colors.RESET}{Escape_Sequences.new_line}")
    create_value_rights_administrator()
else:
    rights_administrator = True

disable_process_off = False

def set_value_disable_process_off(value: bool):
    global disable_process_off
    disable_process_off = value

def get_value_disable_process_off() -> bool:
    return disable_process_off


__all__ = [
    "Escape_Sequences",
    "Colors",
    "get_value_rights_administrator",
    "set_value_rights_administrator,"
    "set_file_path_apache",
    "get_file_path_apache",
    "set_file_path_ApacheSSL",
    "get_file_path_ApacheSSL",
    "set_file_path_MySQLIni",
    "get_file_path_MySQLINI",
    "get_file_path_xampp_control_ini",
    "set_file_path_xampp_control_ini",
    "create_config_json",
    "use_config_json",
    "check_platform",
    "set_value_disable_process_off",
    "get_value_disable_process_off"
]



