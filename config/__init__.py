import ctypes
# для вывода в консоль
class Escape_Sequences:
    new_line = "\n"
    double_new_line = "\n\n"
    tab = "\t"
    
# Цвета для вывода в консоль ( Ошибки и прочее )
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"

# Кодировка для чтения файлов
file_encoding = "cp1252"

# Версия скрипта
version = "V-4.2"

# Rights Administrator
rights_administrator = ctypes.windll.shell32.IsUserAnAdmin()


