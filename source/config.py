# для вывода в консоль
class Escape_Sequences:
    new_line = "\n"
    double_new_line = "\n\n"
    tab = "\t"


# Кодировка для чтения файлов
file_encoding = "cp1252"
version = "V-3.1"


def defining_value_mode():
    from .gui_or_console import mode_console_or_gui

    console, messagebox = mode_console_or_gui()
    return console, messagebox


if __name__ == "__main__":
    defining_value_mode()
