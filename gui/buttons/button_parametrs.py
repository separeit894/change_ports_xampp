import tkinter as tk

from tkinter import (
    Toplevel,
    CENTER,
    ttk,
    messagebox
)
from datetime import datetime

import os
import logging
import traceback
from config import (
    get_encoding, 
    set_encoding, 
    get_file_path_Apache, 
    set_file_path_Apache,
    set_file_path_ApacheSSL,
    get_file_path_ApacheSSL,
    get_file_path_MySQLINI,
    set_file_path_MySQLIni,
    get_file_path_PhpMyAdminConfig,
    set_file_path_PhpMyAdminConfig,
    get_file_path_xampp_control_ini,
    set_file_path_xampp_control_ini
)

def parametrs_button(root, style):
    try:
        window = Toplevel(root)
        window.title("Settings")
        window.geometry("650x450")
        
        
        encoding_label = ttk.Label(window, text=f"Current Encoding : {get_encoding()}", font=("Arial", 12), width=30)
        encoding_label.pack(anchor=CENTER)
        
        # Encoding Frame
        
        Frame_encoding = ttk.Frame(window)
        Frame_encoding.pack(pady=10, padx=40)
        
        label_encoding = ttk.Label(Frame_encoding, text="Encoding : ", font=("Arial", 12))
        label_encoding.pack(anchor="sw", side=tk.LEFT)
        
        enter_pole_encoding = ttk.Entry(Frame_encoding, width=20, font=("Arial", 16))
        enter_pole_encoding.pack(side=tk.LEFT)
        enter_pole_encoding.insert(0, get_encoding())
        
        # Apache Frame
        
        Frame_path_Apache = ttk.Frame(window)
        Frame_path_Apache.pack(pady=10)
        
        label_path_Apache = ttk.Label(Frame_path_Apache, text="Path Apache : ", font=("Arial", 12))
        label_path_Apache.pack(side=tk.LEFT)
        
        enter_pole_path_Apache = ttk.Entry(Frame_path_Apache, width=20, font=("Arial", 16))
        enter_pole_path_Apache.pack(side=tk.LEFT)
        enter_pole_path_Apache.insert(0, get_file_path_Apache())
        
        # ApacheSSL Frame
        
        Frame_path_ApacheSSL = ttk.Frame(window)
        Frame_path_ApacheSSL.pack(pady=10)
        
        label_path_ApacheSSL = ttk.Label(Frame_path_ApacheSSL, text="Path ApacheSSL : ", font=("Arial", 12))
        label_path_ApacheSSL.pack(side=tk.LEFT)
        
        enter_pole_path_ApacheSSL = ttk.Entry(Frame_path_ApacheSSL, width=20, font=("Arial", 16))
        enter_pole_path_ApacheSSL.pack(side=tk.LEFT)
        enter_pole_path_ApacheSSL.insert(0, get_file_path_ApacheSSL())
        
        # MySQL Frame
        
        Frame_path_MySQL = ttk.Frame(window)
        Frame_path_MySQL.pack(pady=10)
        
        label_path_MySQL = ttk.Label(Frame_path_MySQL, text="Path MySQL : ", font=("Arial", 12))
        label_path_MySQL.pack(side=tk.LEFT)
        
        enter_pole_path_MySQL = ttk.Entry(Frame_path_MySQL, width=20, font=("Arial", 16))
        enter_pole_path_MySQL.pack(side=tk.LEFT)
        enter_pole_path_MySQL.insert(0, get_file_path_MySQLINI())
        
        # PhpMyAdmin Frame
        
        Frame_path_PhpMyAdmin = ttk.Frame(window)
        Frame_path_PhpMyAdmin.pack(pady=10)
        
        label_path_PhpMyAdmin = ttk.Label(Frame_path_PhpMyAdmin, text="Path PhpMyAdmin : ", font=("Arial", 12))
        label_path_PhpMyAdmin.pack(side=tk.LEFT)
        
        enter_pole_path_PhpMyAdmin = ttk.Entry(Frame_path_PhpMyAdmin, width=20, font=("Arial", 16))
        enter_pole_path_PhpMyAdmin.pack(side=tk.LEFT)
        enter_pole_path_PhpMyAdmin.insert(0, get_file_path_PhpMyAdminConfig())
        
        # Xampp control ini Frame
        
        Frame_path_XamppControlINI = ttk.Frame(window)
        Frame_path_XamppControlINI.pack(pady=10)
        
        label_path_XamppControlINI = ttk.Label(Frame_path_XamppControlINI, text="Path XamppControlINI : ", font=("Arial", 12))
        label_path_XamppControlINI.pack(side=tk.LEFT)
        
        enter_pole_path_XamppControlINI = ttk.Entry(Frame_path_XamppControlINI, width=20, font=("Arial", 16))
        enter_pole_path_XamppControlINI.pack(side=tk.LEFT)
        enter_pole_path_XamppControlINI.insert(0, get_file_path_xampp_control_ini())
        
        # Encoding Button
        
        submit_button_encoding = ttk.Button(
            Frame_encoding, text="Apply", width=10,command=lambda: set_encoding(enter_pole_encoding.get()), style="BigText.TButton"
        )
        submit_button_encoding.pack()
        
        # Apache Button
        
        submit_button_apache = ttk.Button(
            Frame_path_Apache, text="Apply", width=10,command=lambda: set_file_path_Apache(enter_pole_path_Apache.get()), style="BigText.TButton"
        )
        submit_button_apache.pack()
        
        # ApacheSSL button
        
        submit_button_ApacheSSL = ttk.Button(
            Frame_path_ApacheSSL, text="Apply",command=lambda: set_file_path_ApacheSSL(enter_pole_path_ApacheSSL.get()), style="BigText.TButton"
        )
        submit_button_ApacheSSL.pack()
        
        # MySQL button
        
        submit_button_MySQL = ttk.Button(
            Frame_path_MySQL, text="Apply",command=lambda: set_file_path_MySQLIni(enter_pole_path_MySQL.get()), style="BigText.TButton"
        )
        submit_button_MySQL.pack()
        
        # PhpMyAdmin button 
        
        submit_button_PhpMyAdmin = ttk.Button(
            Frame_path_PhpMyAdmin, text="Apply",command=lambda: set_file_path_PhpMyAdminConfig(enter_pole_path_PhpMyAdmin.get()), style="BigText.TButton"
        )
        submit_button_PhpMyAdmin.pack()
        
        # Xampp control ini path button 
        
        submit_button_XamppControlINI = ttk.Button(
            Frame_path_XamppControlINI, text="Apply",command=lambda: set_file_path_xampp_control_ini(enter_pole_path_XamppControlINI.get()), style="BigText.TButton"
        )
        submit_button_XamppControlINI.pack()
        
    except Exception:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : An error has been detected!\n{tb}")
        messagebox.showerror("Обнаружена ошибка :", tb)
                
    
    
if __name__ == "__main__":
    parametrs_button()