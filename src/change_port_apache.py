import os
import sys
# new_port = sys.argv[1]

def change_port_apache(new_port):
    with open("apache/conf/httpd.conf", 'r', encoding="utf-8") as file:
        src = file.readlines()

    if not os.path.exists("backup"):
        os.makedirs("backup")

    if not os.path.exists("backup/httpd.conf"):
        with open("backup/httpd.conf", "w", encoding="utf-8") as file:
            file.writelines(src)

    index_port_listen = None

    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "Listen" in src[i]:
                print(i, line)
                index_port_listen = i

    src[index_port_listen] = f"Listen {new_port}\n"

    index_port_servername = None

    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "ServerName" in src[i]:
                print(i, line)
                index_port_servername = i

    src[index_port_servername] = src[index_port_servername].split(":")
    src[index_port_servername][1] = f":{new_port}\n"
    result = "".join(src[index_port_servername])

    src[index_port_servername] = result

    with open("apache/conf/httpd.conf", "w", encoding="utf-8") as file:
        file.writelines(src)

if __name__ == "__main__":
    change_port_apache()