import ctypes
import traceback

from .edit_xampp_control import run_as_admin
from .process_off import Process
from config import Escape_Sequences
from config import Colors
from config import file_encoding


class Recovery_Files:
    try:
        def file_recovery_apache(self) -> bool:
            # Функция берет резервный файл, и записывает его данные в основной
            try:
                Process().apache_process_off()

                backup_path = "backup/httpd.conf"
                with open(backup_path, "r", encoding=file_encoding) as file:
                    src = file.readlines()

                file_path = "apache/conf/httpd.conf"
                with open(file_path, "w", encoding=file_encoding) as file:
                    file.writelines(src)
                    
                return True

            except Exception as e:
                tb = traceback.format_exc()
                print(tb)
                return False


        def file_recovery_apachessl(self) -> bool:
            try:
                Process().apachessl_process_off()

                backup_path = "backup/httpd-ssl.conf"
                with open(backup_path, "r", encoding=file_encoding) as file:
                    src = file.readlines()

                file_path = "apache/conf/extra/httpd-ssl.conf"
                with open(file_path, "w", encoding=file_encoding) as file:
                    file.writelines(src)

                return True
                
            except Exception as e:
                tb = traceback.format_exc()
                print(tb)
                return False


        def file_recovery_mysql(self) -> bool:
            try:
                Process().mysql_process_off()

                # Восстановление файла my.ini MySQL
                backup_path_ini = "backup/my.ini"
                with open(backup_path_ini, "r", encoding=file_encoding) as file:
                    src = file.readlines()

                file_path_ini = "mysql/bin/my.ini"
                with open(file_path_ini, "w", encoding=file_encoding) as file:
                    file.writelines(src)

                # Восстановление файла config.inc.php phpMyAdmin
                backup_path_php = "backup/config.inc.php"
                with open(backup_path_php, "r", encoding=file_encoding) as file:
                    src_config = file.readlines()

                file_path_php = "phpMyAdmin/config.inc.php"
                with open(file_path_php, "w", encoding=file_encoding) as file:
                    file.writelines(src_config)

                return True

            except Exception as e:
                tb = traceback.format_exc()
                print(tb)
                return False


        def file_recovery_xampp_control(self) -> bool:
            if ctypes.windll.shell32.IsUserAnAdmin():
                try:
                    Process().xampp_control_process_off()

                    backup_path = "backup/xampp-control.ini"
                    with open(backup_path, "r", encoding=file_encoding) as file:
                        src = file.readlines()

                    file_path = "xampp-control.ini"
                    with open(file_path, "w", encoding=file_encoding) as file:
                        file.writelines(src)

                    return True

                except Exception as e:
                    tb = traceback.format_exc()
                    print(tb)
                    return False
                    
            else:
                print("Error: Administrator privileges are required.")
                run_as_admin()
                
    except Exception:
        tb = traceback.format_exc()
        print(tb)

if __name__ == "__main__":
    Recovery_Files().file_recovery_apache()
    Recovery_Files().file_recovery_apachessl()
    Recovery_Files().file_recovery_mysql()
    Recovery_Files().file_recovery_xampp_control()
    
