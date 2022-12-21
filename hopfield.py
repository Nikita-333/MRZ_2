from functools import reduce

import numpy as np
import matplotlib.pyplot as plt


class Hopfield:
    def __init__(self, size_figure=(32, 32), select: bool = False,file: str = None):
        self.size_figure = size_figure
        self.name_file = file
        self.weight = self.select_weight(select)

    def set_file_name(self, name_file: str):
        try:
            if name_file == None:
                print("Не удаётся получить файл")
        finally:
            self.name_file = name_file

    def load_weight(self):
        with open(self.name_file, 'r') as file:
            return np.loadtxt(self.name_file)
        # try:
        # if not np.loadtxt(self.name_file):
        # print("Не удаётся прочитать файл")
        # finally:
        # return np.loadtxt(self.name_file)

    def select_weight(self, select: bool):
        if select == True:
            return self.load_weight()

        if select == False:
            return np.zeros(
                [self.size_figure[0] * self.size_figure[1],
                 self.size_figure[0] * self.size_figure[1]], dtype=np.float_)
        if select == None:
            print("Ошибка")

    def to_save_weight(self):
        with open(self.name_file, 'w') as file:
            list_change_w1 = self.weight.reshape(self.weight.shape[0], -1)
            np.savetxt(self.name_file, list_change_w1)

    def count_weight(self, practice_info):
        for one_pointer in range(practice_info.size):
            for two_pointer in range(practice_info.size):
                try:
                    if one_pointer != float(one_pointer) and two_pointer != float(two_pointer):
                        print("Неверные значения")
                finally:
                    self.weight[one_pointer][two_pointer] += practice_info[one_pointer] * practice_info[two_pointer]

    def append_practice_info(self, image_directory):
        # lst_avg = reduce(lambda x, y: x + y, inp_lst) /lst_len
        images = np.average(plt.imread(image_directory), axis=2)
        images = np.where(images < np.average(images), 1, -1)
        self.count_weight(practice_info=images.flatten())

    def division_by_n(self):
        for index, _ in enumerate(self.weight):
            for column, _ in enumerate(self.weight):
                turn_flot = float(self.weight[index][column])
                turn_flot *= 1 / self.size_figure[0]
                self.weight[index][column] = turn_flot

    def renew(self, status_el, index):
        status_el[index] = func_sign(self.weight[index] @ status_el)
        return status_el

    def predict(self, input_image, name_directory):
        print("Испорченное фото: ", name_directory)
        iter = 150
        async_iter = 1500
        try:
            if iter < 0 and async_iter < 0:
                print("Введите положительное число итера(50) и асинхронный итер(400)")
            elif input_image == None and name_directory == None:
                print("Проверьте данные")
        finally:
            input_shape_fig = input_image.shape
            input_image = np.where(input_image < 0.5, 1, -1)
            state = self.calc_predict(input_image)#, iter, async_iter)
            return np.where(state < 1, 0, 1).reshape(input_shape_fig)

    def calc_predict(self, input_image): #, iter, async_iter):
        energy_condition, status_el = self.energy_condition(input_image.flatten()), input_image.flatten()
        iter = 150
        async_iter = 1500
        for index_iter in range(iter):
            for _ in range(async_iter):
                index_el = np.random.randint(status_el.size)
                status_el = self.renew(status_el, index_el)
            new_energy_condition = self.energy_condition(status_el)
            print('Итерация: ', index_iter, '| Состояние энергии: ', new_energy_condition)
            try:
                if new_energy_condition != energy_condition:
                    index_el = np.random.randint(status_el.size)
                    status_el = self.renew(status_el, index_el)
                    new_energy_condition = self.energy_condition(status_el)
            finally:
                if new_energy_condition == energy_condition:
                    print('Новая энергия и старая энергия достигла стабильного состояния.')
                    break
            energy_condition = new_energy_condition
        return status_el

    def energy_condition(self, matr_calc):
        # E = −x0 * e.T = −x0 * W * y0.T
        return -0.5 * (matr_calc.transpose() @ self.weight) @ matr_calc

    def learn(self, list_photos: list):
        try:
            if list_photos == None:
                print("Добавьте фото")
        finally:
            for practice_info in list_photos:
                print('Обучение:', practice_info)
                self.append_practice_info(practice_info)
        self.division_by_n()
        fill_diagonal(self.weight)
        # np.fill_diagonal(self.weight, 0)
        print('Обучение закончено')


def func_sign(num):
    # return 1 if num >= 0 else -1
    return round(np.tanh(num))


def fill_diagonal(matrix):
    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            if rows == column:
                matrix[rows][column] = 0
    return matrix


def transposition(matrix):
    trans_matr = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_matr

# def mulmut(matrix1, matrix2):
