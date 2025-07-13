import requests
import webbrowser
import traceback

from bs4 import BeautifulSoup
from tkinter import ttk

from ..config import version
from ..config import Escape_Sequences
from ..config import Colors

link = None

class Update:
    def __init__(self, console, messagebox):
        self.console = console
        self.messagebox = messagebox
        
    # Функция, которая выполняет проверку последней версии приложения
    def checking_for_update(self):
        # Функция проверяет последняя версия программы или нет, в случае если нет, то выходит меню с выбором,
        # если пользователь кликнул по кнопке "Да", то его перенаправляет на страницу с последней версией
        try:
            self.update = False
            self.url = "https://github.com/separeit894/change_ports_xampp/releases"

            self.response = requests.get(self.url)

            self.soup = BeautifulSoup(self.response.text, "lxml")
            self.release_titles = self.soup.find(
                "div", "d-flex flex-column flex-md-row my-5 flex-justify-center"
            )

            self.main_release = self.release_titles.find("div", "col-md-9")
            self.text_release = self.main_release.find("span", "f1 text-bold d-inline mr-3")
            text = self.text_release.find("a").get("href")
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
        except BaseException as bs:
            tb = traceback.format_exc()
            print(f"tb: {tb}")

    # Функция, которая работает в консольном режиме
    def update_console(self):
        try:
            if self.console:
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
            if self.console:
                print(f"Обнаружена ошибка: {tb}")
            else:
                self.messagebox.showinfo("Обнаружена ошибка!", f"{tb}")



    # Функция, которая создает кнопку "Доступно новое обновление", при нажатии которой пользователь переходит на страницу браузера
    def update_gui(self, root, style):
        try:
            Frame_New_Version = ttk.Frame(root)
            Frame_New_Version.pack(anchor="sw", padx=250, pady=30)

            def open_link():
                webbrowser.open(link)

            Button_New_Version = ttk.Button(Frame_New_Version, text="Доступна новая\n        версия",command=open_link)
            Button_New_Version.pack()
            
        except BaseException:
            tb = traceback.format_exc()
            if self.console:
                print(f"Обнаружена ошибка: {tb}")
            else:
                self.messagebox.showinfo("Обнаружена ошибка!", f"{tb}")



if __name__ == "__main__":
    Update().checking_for_update()
    Update().update_gui()
    Update().update_console()
