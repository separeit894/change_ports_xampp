
from cli import CLI
from gui import GUI

import argparse


# Функция проверяет запущена CLI или GUI
def main():
    parser = argparse.ArgumentParser(
        description="Change Ports XAMPP — меняет порты Apache, MySQL и др."
    )
    
    # Добавляем опцию --console
    parser.add_argument(
        '--console',
        action='store_true',
        help='Запустить в консольном режиме (CLI)'
    )

    # Парсим аргументы
    args = parser.parse_args()

    # Решаем, что запускать
    if args.console:
        CLI().run_app()
    else:
        GUI().run_app()


if __name__ == "__main__":
    main()


