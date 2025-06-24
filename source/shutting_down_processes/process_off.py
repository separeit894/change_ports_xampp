import subprocess


def apache_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "httpd.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)


def apachessl_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "httpd.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)


def mysql_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "mysqld.exe"

    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)


def xampp_control_process_off():
    # Если служба запущена, то мы её отключаем
    process_name = "xampp-control.exe"
    
    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == "__main__":
    apache_process_off()
    apachessl_process_off()
    mysql_process_off()