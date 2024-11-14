import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def calculate_histogram(img: np.ndarray) -> tuple:
    """
    Вычисляем гистограммы для трех цветовых каналов изображения.

    :param img: Цветное изображение в формате numpy.ndarray.
    :return: Кортеж из трех гистограмм (для красного, зеленого и синего каналов).
    """
    hist_b = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv.calcHist([img], [2], None, [256], [0, 256])
    return hist_r, hist_g, hist_b


def plot_histogram(hists: tuple) -> None:
    """
    Рисуем гистограммы для трех цветовых каналов.

    :param hists: Кортеж из трех гистограмм (для красного, зеленого и синего каналов).
    """
    plt.figure()
    plt.title("Гистограммы цветового изображения")
    plt.xlabel("Яркость")
    plt.ylabel("Количество пикселей")

    plt.plot(hists[0], color='red', label='Красный канал')
    plt.plot(hists[1], color='green', label='Зеленый канал')
    plt.plot(hists[2], color='blue', label='Синий канал')

    plt.xlim([0, 256])
    plt.legend()
    plt.show()
