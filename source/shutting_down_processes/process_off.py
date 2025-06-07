import subprocess


def apache_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "httpd.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name])


def apachessl_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "httpd.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name])


def mysql_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "mysqld.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name])


def xampp_control_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "xampp-control.exe"
    
    subprocess.run(["taskkill", "/F", "/IM", process_name])

if __name__ == "__main__":
    apache_process_off()
    apachessl_process_off()
    mysql_process_off()