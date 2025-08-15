import subprocess

# Службы
process_name_httpd = "httpd.exe"
process_name_mysqld = "mysqld.exe"
process_name_xampp_control = "xampp-control.exe"


class Process:
    def apache_process_off(self):
        # Если служба запущена, то мы её отключаем

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_httpd],
            stdout=subprocess.PIPE,  # Не выводит в консоль
            stderr=subprocess.PIPE,  # Не выводит ошибки
            creationflags=subprocess.CREATE_NO_WINDOW,  # Не создает окно
        )


    def apachessl_process_off(self):

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_httpd],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )


    def mysql_process_off(self):

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_mysqld],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )


    def xampp_control_process_off(self):

        subprocess.run(
            ["taskkill", "/F", "/IM", process_name_xampp_control],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )


if __name__ == "__main__":
    Process().apache_process_off()
    Process().apachessl_process_off()
    Process().mysql_process_off()
    Process().xampp_control_process_off()
