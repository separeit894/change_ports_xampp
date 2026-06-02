from core import change_port_ssl
from config import (
    Escape_Sequences,
    Colors
)

from datetime import datetime

import traceback
import logging
import os


def apachessl_mode_console() -> None:
    try:
        while True:
            list_text_apachessl = [
                "Enter a new Apache SSL port:",
                "Go back to the main menu"
            ]
            for i, line in enumerate(list_text_apachessl):
                print(f"{i}. {line}")

            choise = int(input(f"Select a menu item ( 0 - {len(list_text_apachessl) - 1} ): "))
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : choise : {choise}")
            if choise == 0:
                new_port = str(input("Enter a new port: "))
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : The port ApacheSSL that the user entered : {new_port}")
                result = change_port_ssl(new_port)
                if result:
                    print(
                        f"{Escape_Sequences.double_new_line}{Colors.BOLD}ApacheSSL port changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                    )
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : ApacheSSL port changed successfully!")
                    
                break
            elif choise == 1:
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Return to the main menu")
                break
            else:
                print(f"{Escape_Sequences.double_new_line}{Colors.BOLD}There is no such number in this list! Сhose Again{Colors.RESET}{Escape_Sequences.new_line}")
                continue

    except Exception:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.BOLD}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : An error has been detected! : \n{tb}")


if __name__ == "__main__":
    apachessl_mode_console()
