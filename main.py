import pathlib
import os


def new_request():
    global request
    request = input("Введите номер файла/папки:\n")
    try:
        if request == "back":
            dir_content(dir_par)
            choice_dir(dir_par)
        elif request == "begin":
            dir_content(current_directory)
            choice_dir(current_directory)
        else:
            request = int(request)
            return request
    except ValueError:
        print("Неверный ввод.\t Введите число или команду 'back'.")
    finally:
        return request

def back_request(directory):
    new_dir = pathlib.Path.parent
    print(new_dir)

def dir_content(directory):
    for i, item in enumerate(directory.iterdir(), 1):
        print(f"{i}) {item.name}")


def choice_dir(directory):
    global dir_par
    new_request()
    try:
        choice = list(directory.iterdir())[request - 1]
        if choice.is_dir():
            dir_par = choice.parent
            dir_content(choice)
            choice_dir(choice)
        elif choice.is_file():
            with open(choice, 'r') as f:
                print(f.read())
    except IndexError:
        print("List index out of range.")


current_directory = pathlib.Path.cwd()
dir_content(current_directory)
choice_dir(current_directory)