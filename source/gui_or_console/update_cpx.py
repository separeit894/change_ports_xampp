import requests
import webbrowser
import traceback

from bs4 import BeautifulSoup

from tkinter import ttk

from ..config import version
from ..config import defining_value_mode
from ..config import Escape_Sequences
from ..color_output import Colors

link = None

def checking_for_update():
    # Функция проверяет последняя версия программы или нет, в случае если нет, то выходит меню с выбором,
    # если пользователь кликнул по кнопке "Да", то его перенаправляет на страницу с последней версией
    update = False
    url = "https://github.com/separeit894/change_ports_xampp/releases"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")
    release_titles = soup.find(
        "div", "d-flex flex-column flex-md-row my-5 flex-justify-center"
    )

    main_release = release_titles.find("div", "col-md-9")
    text_release = main_release.find("span", "f1 text-bold d-inline mr-3")
    text = text_release.find("a").get("href")
    global link
    link = "github.com" + text
    finally_text = text.split("-")[1]
    float_version = float(version.split("-")[1])
    if float(finally_text) > float_version:
         update = True
         return update
    else:
         update = False
         print(f"{Escape_Sequences.double_new_line}{Colors.GREEN}Вы находитесь на последней версии{Colors.RESET}{Escape_Sequences.new_line}")
         return update

def update_console():
    console, messagebox = defining_value_mode()
    try:
        if console:
                while True:
                    new_version = str(
                        input("Обнаружена новая версия! Вы хотите обновить? (y/n) : ")
                    )
                    if new_version == "y" or new_version == "Y":
                        webbrowser.open(link)
                        break
                    elif new_version == "n" or new_version == "N":
                        break
                    else:
                        print("Нужно Y или N!")             

    except BaseException:
        tb = traceback.format_exc()
        if console:
            print(f"Обнаружена ошибка: {tb}")
        else:
            messagebox.showinfo("Обнаружена ошибка!", f"{tb}")



def update_gui(root, style):
    console, messagebox = defining_value_mode()
    try:
        Frame_New_Version = ttk.Frame(root)
        Frame_New_Version.pack(anchor="sw", padx=250, pady=30)

        def open_link():
            webbrowser.open(link)

        Button_New_Version = ttk.Button(Frame_New_Version, text="Доступна новая\n        версия",command=open_link)
        Button_New_Version.pack()
        
    except BaseException:
        tb = traceback.format_exc()
        if console:
            print(f"Обнаружена ошибка: {tb}")
        else:
            messagebox.showinfo("Обнаружена ошибка!", f"{tb}")


if __name__ == "__main__":
    checking_for_update()
    update_gui()
