import os
import sys


def change_port_mysql(new_port):

    # Сначала открываю файл, чтобы сделать его backup
    with open("mysql/bin/my.ini", "r", encoding="utf-8") as file:
        src = file.readlines()

    # Если нету папки backup, то он её создает
    if not os.path.exists("backup"):
        os.makedirs("backup")

    # Если нету резервного файла, то он его создает
    if not os.path.exists("backup/my.ini"):
        with open("backup/my.ini", "w", encoding="utf-8") as file:
            file.writelines(src)


    # Цикл считывает каждую строку файла
    for i, line in enumerate(src):
        # Если строка не начинается с #, то он переходит к внутреннему условию
        if not line.startswith("#"):
            # Если он находит слово port, присваевает новый порт 
            if "port" in src[i]:
                print(i, line)
                src[i] = f"port={new_port}\n"

    # Сохраняет измененный файл
    with open("mysql/bin/my.ini", "w", encoding="utf-8") as file:
        file.writelines(src)

    # Считываем другой файл
    with open("phpMyAdmin/config.inc.php", "r", encoding="utf-8") as file:
        src = file.readlines()

    # Если нету первого резервного файла, то он его создает
    if not os.path.exists("backup/config.inc.php"):
        with open("backup/config.inc.php", "w", encoding="utf-8") as file:
            file.writelines(src)


    # Новая переменная, которая будет в себе содержать измененное содержимое строки с портом
    index_cfg_server = None

    # Цикл считывает файл
    for i, line in enumerate(src):
        # Если строка не начинается с #, то он переходит к внутреннему условию
        if not line.startswith("#"):
            # Дальше он ищет $cfg['Servers'][$i]['port'], чтобы присвоить номер строки переменной
            if "$cfg['Servers'][$i]['port']" in src[i]:
                print(i, line)
                # Присваеваем значение этой строки
                index_cfg_server = i
                # меняем порт
                src[i] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

    """ 
    В случае, если переменная пустая, то есть так и не нашла эту строку ( см. 52 строку кода )
    то он эту строку создаст по умолчанию на 21 строке кода ( не знаю почему на 21, мне просто так захотелось )
    """
    if index_cfg_server is None:
        src[21] = f"$cfg['Servers'][$i]['port'] = '{new_port}';\n"

    # Сохраняем результат
    with open("phpMyAdmin/config.inc.php", "w", encoding="utf-8") as file:
        file.writelines(src)

if __name__ == "__main__":
    change_port_mysql()