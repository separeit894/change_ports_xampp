from tkinter import Toplevel
from tkinter import CENTER
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime
import os
import logging
import traceback


def parametrs_button(root, style):
    try:
        window = Toplevel(root)
        window.title("Settings")
        window.geometry("500x250")
        from config import get_encoding
        encoding_label = ttk.Label(window, text=f"Сurrent Encoding : {get_encoding()}", font=("Arial", 12), width=30)
        encoding_label.pack(anchor=CENTER)
        
        enter_pole = ttk.Entry(window, width=20, font=("Arial", 16))
        enter_pole.pack(anchor=CENTER, pady=30)
        enter_pole.insert(0, get_encoding())
        
        from config import set_encoding
        submit_button = ttk.Button(
            window, text="Apply", command=lambda: set_encoding(enter_pole.get()), style="Small.TButton"
        )
        submit_button.pack()
        
    except Exception as e:
        tb = traceback.format_exc()
        print(f"An error has been detected!\n{tb}")
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : GUI : An error has been detected!\n{tb}")
    
    
if __name__ == "__main__":
    parametrs_button()