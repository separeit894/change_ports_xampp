import os
import sys
# new_port = sys.argv[1]

def change_port_ssl(new_port):
    with open("apache/conf/extra/httpd-ssl.conf", "r", encoding="utf-8") as file:
        src = file.readlines()

    if not os.path.exists("backup"):
        os.makedirs("backup")

    if not os.path.exists("backup/httpd-ssl.conf"):
        with open("backup/httpd-ssl.conf", "w", encoding="utf-8") as file:
            file.writelines(src)

    index_listen = None
    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "Listen" in src[i]:
                print(i, line)
                index_listen = i

    src[index_listen] = f"Listen {new_port}\n"


    index_virtualhost = None
    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "<VirtualHost _default_:" in src[i]:
                print(i, line)
                index_virtualhost = i

    src[index_virtualhost] = f"<VirtualHost _default_:{new_port}>\n"

    index_servername = None
    for i, line in enumerate(src):
        if not line.startswith("#"):
            if "ServerName" in src[i]:
                print(i, line)
                index_servername = i

    src[index_servername] = f"ServerName www.example.com:{new_port}\n"

    with open("apache/conf/extra/httpd-ssl.conf", "w", encoding="utf-8") as file:
        file.writelines(src)

if __name__ == "__main__":
    change_port_ssl()