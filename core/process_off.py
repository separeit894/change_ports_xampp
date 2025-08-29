import subprocess
import logging
import os
from datetime import datetime

logging.basicConfig(filename="CPX.log", level=logging.DEBUG)


# Службы
process_name_httpd = "httpd.exe"
process_name_mysqld = "mysqld.exe"
process_name_xampp_control = "xampp-control.exe"


class Process:
    @staticmethod
    def apache_process_off() -> None:
        # Если служба запущена, то мы её отключаем

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_httpd],
            stdout=subprocess.PIPE,  # Не выводит в консоль
            stderr=subprocess.PIPE,  # Не выводит ошибки
            creationflags=subprocess.CREATE_NO_WINDOW,  # Не создает окно
        )
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Disabling the apache service")

    @staticmethod
    def apachessl_process_off() -> None:

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_httpd],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Termination of the ApacheSSL process")
        

    @staticmethod
    def mysql_process_off() -> None:

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_mysqld],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Disabling the MySQL process(s)")

    @staticmethod
    def xampp_control_process_off() -> None:

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_xampp_control],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        
        logging.info(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} : {os.path.basename(__file__)} : Disabling the xampp process")


if __name__ == "__main__":
    Process.apache_process_off()
    Process.apachessl_process_off()
    Process.mysql_process_off()
    Process.xampp_control_process_off()
