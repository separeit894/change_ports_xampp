import requests
import webbrowser
import traceback
import importlib

from bs4 import BeautifulSoup

# from tkinter.messagebox import askyesno


from ..config import version
from ..config import defining_value_mode


def update():
    console, messagebox = defining_value_mode()
    try:
        # Функция проверяет последняя версия программы или нет, в случае если нет, то выходит меню с выбором,
        # если пользователь кликнул по кнопке "Да", то его перенаправляет на страницу с последней версией
        url = "https://github.com/separeit894/change_ports_xampp/releases"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")
        release_titles = soup.find(
            "div", "d-flex flex-column flex-md-row my-5 flex-justify-center"
        )

        main_release = release_titles.find("div", "col-md-9")
        text_release = main_release.find("span", "f1 text-bold d-inline mr-3")
        text = text_release.find("a").get("href")
        link = "github.com/" + text
        finally_text = text.split("-")[1]
        float_version = float(version.split("-")[1])
        if float(finally_text) > float_version:
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
            else:
                askyesno = messagebox.askyesno
                result = askyesno(
                    title="Обнаружена новая версия!", message="Вы хотите обновить?"
                )
                if result:
                    webbrowser.open(link)
                else:
                    pass
        else:
            print("Вы сейчас на последней версии")
    except BaseException:
        tb = traceback.format_exc()
        if console:
            print(f"Обнаружена ошибка: {tb}")
        else:
            messagebox.showinfo("Обнаружена ошибка!", f"{tb}")


if __name__ == "__main__":
    update()
