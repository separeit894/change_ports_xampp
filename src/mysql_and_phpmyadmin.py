import os
import sys

# new_port = sys.argv[1]

def change_port_mysql(new_port):
    with open("mysql/bin/my.ini", "r", encoding="utf-8") as file:
        src = file.readlines()

    if not os.path.exists("backup"):
        os.makedirs("backup")

    if not os.path.exists("backup/my.ini"):
        with open("backup/my.ini", "w", encoding="utf-8") as file:
            file.writelines(src)

    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "port" in src[i]:
                print(i, line)
                src[i] = f"port={new_port}\n"


    with open("mysql/bin/my.ini", "w", encoding="utf-8") as file:
        file.writelines(src)

    with open("phpMyAdmin/config.inc.php", "r", encoding="utf-8") as file:
        src = file.readlines()

    if not os.path.exists("backup/config.inc.php"):
        with open("backup/config.inc.php", "w", encoding="utf-8") as file:
            file.writelines(src)

    index_cfg_server = None
    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "$cfg['Servers'][$i]['port']" in src[i]:
                print(i, line)
                index_cfg_server = i
                src[i] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

    if index_cfg_server is None:
        src[21] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"


    with open("phpMyAdmin/config.inc.php", "w", encoding="utf-8") as file:
        file.writelines(src)

if __name__ == "__main__":
    change_port_mysql()