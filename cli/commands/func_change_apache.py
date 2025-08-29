import traceback
import os
import logging

from config import Escape_Sequences
from config import Colors

from datetime import datetime

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)


def apache_mode_console() -> None:
    from core import change_port_apache

    try:
        while True:
            list_text_apache = [
                "Introduce a new Apache port:",
                "Go back to the main menu"
            ]
            for i, line in enumerate(list_text_apache):
                print(f"{i}. {line}")

            choise = int(input("Select a menu item ( 0 - 1 ): "))
            logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : choise : {choise}")
            if choise == 0:
                new_port = str(input("Enter a new port: "))
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : The port Apache that the user entered : {new_port}")
                result = change_port_apache(new_port)
                if result:
                    print(
                        f"{Escape_Sequences.double_new_line}{Colors.GREEN}Apache port changed successfully!{Colors.RESET}{Escape_Sequences.new_line}"
                    )
                    logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Apache port changed successfully!")
                
                break
            elif choise == 1:
                logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : Return to the main menu")
                break

    except Exception as e:
        tb = traceback.format_exc()
        print(
            f"{Escape_Sequences.double_new_line}{Colors.RED}An error has been detected!{Escape_Sequences.new_line}{tb}{Colors.RESET}{Escape_Sequences.new_line}"
        )
        logging.error(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : CLI : An error has been detected! : \n{tb}")

if __name__ == "__main__":
    apache_mode_console()
