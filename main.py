import numpy as np
from hopfield import Hopfield
from func_support import get_arr_image, to_predict_file_directory_image

np.random.seed(1)

main_ = input("1 - Обучить\n"
              "2 - Использованные\n"
              "3 - Нет данных\n")

match main_:
    case "1":
        input_size_image = tuple(int(num) for num in input("Размер фото: ").split())
        model = Hopfield(input_size_image)
        entry_name_directory = input('Имя папки: ')
        if entry_name_directory != 'true_image':
            print("Введите имя папки эталоных картинок (true_image!)")
            entry_name_directory = input('Имя папки: ')

        entry_iter = int(input('Номер итерации: '))
        if entry_iter <= 0:
            print("Введите положительное целое число: ")
            entry_iter = int(input('Номер итерации: '))

        entry_asyn_iter = int(input('Номер асинхронной итерации: '))
        if entry_asyn_iter <= 0:
            print("Введите положительное целое число: ")
            entry_asyn_iter = int(input('Номер асинхронной итерации: '))

        model.learn(get_arr_image(entry_name_directory))

        select_repare = input("Один файл или папку?\n"
                              "1. Один файл\n"
                              "2. Папку\n")
        if select_repare != "1" and select_repare != "2":
            print("Введите 1 или 2")
            select_repare = input("Один файл или папку?\n"
                                  "1. Один файл\n"
                                  "2. Папку\n")
        match select_repare:
            case "1":
                name_ruined_image = input("Испорченное фотография: ")
                to_predict_file_directory_image(name_ruined_image, model,entry_iter, entry_asyn_iter)
            case "2":
                name_folder = input("Имя папки: ")
                if name_folder == "true_image":
                    print("Введите папку испорченных картинок")
                    name_folder = input("Имя папки: ")

                for name_ruined_image in get_arr_image(name_folder):
                    to_predict_file_directory_image(name_ruined_image, model,entry_iter, entry_asyn_iter)

        question = input("Сохранить веса?\n"
                         "1. Да\n"
                         "2. Нет\n")
        if question != "1" and select_repare != "2":
            print("Введите 1 или 2")
            question = input("Сохранить веса?\n"
                             "1. Да\n"
                             "2. Нет\n")
            if question != "1" and question != "2":
                print("Введите 1 или 2")
                question = input("Один файл или папку?\n"
                                 "1. Один файл\n"
                                 "2. Папку\n")
        match question:
            case "1":
                file = input("Название файла: ")
                model.set_file_name(name_file=file)
                model.to_save_weight()
    case "2":
        file = input("Название файла: ")
        model = Hopfield(select=True,file=file)
        select_repare = input("Один файл или папку?\n"
                              "1. Один файл\n"
                              "2. Папку\n")
        if select_repare != "1" and select_repare != "2":
            print("Введите 1 или 2")
            select_repare = input("Один файл или папку?\n"
                                  "1. Один файл\n"
                                  "2. Папку\n")

        entry_iter = int(input('Номер итерации: '))
        if entry_iter <= 0:
            print("Введите положительное целое число: ")
            entry_iter = int(input('Номер итерации: '))
        entry_asyn_iter = int(input('Асинхронный номер итерации: '))
        if entry_asyn_iter <= 0:
            print("Введите положительное целое число: ")
            entry_asyn_iter = int(input('Асинхронный номер итерации: '))
        match select_repare:
            case "1":
                name_ruined_image = input("Испорченное фото: ")
                to_predict_file_directory_image(name_ruined_image, model, entry_iter, entry_asyn_iter)
            case "2":
                name_folder = input("Имя папки: ")
                for name_ruined_image in get_arr_image(name_folder):
                    to_predict_file_directory_image(name_ruined_image, model, entry_iter, entry_asyn_iter)

    case "3":
        input_size_image = (32, 32)
        model = Hopfield(input_size_image)

        entry_name_directory = "true_image"
        entry_iter = 150
        entry_asyn_iter = 1500
        model.learn(get_arr_image(entry_name_directory))

        for name_ruined_image in get_arr_image("ruined_image"):
            to_predict_file_directory_image(name_ruined_image, model, entry_iter, entry_asyn_iter)
