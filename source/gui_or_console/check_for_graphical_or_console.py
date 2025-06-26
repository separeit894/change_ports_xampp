import sys
import importlib


def mode_console_or_gui():
    # Функция, проверяет - запущено приложение с параметром или нет
    console, messagebox = None, None
    if len(sys.argv) > 1:
        print(len(sys.argv))
        # Если условие верно, то запускается консольная версия
        if "--console" in sys.argv:
            console = True
            messagebox = None
        else:
            # Иначе GUI
            console = None
            messagebox = importlib.import_module("tkinter.messagebox")
    else:   
        console = None
        messagebox = importlib.import_module("tkinter.messagebox")

    return console, messagebox


if __name__ == "__main__":
    mode_console_or_gui()
