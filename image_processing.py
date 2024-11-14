import cv2 as cv
import numpy as np


def read_image(image_path: str) -> np.ndarray:
    """
    Считываем изображение из файла.

    :param image_path: Путь к файлу изображения.
    :return: Изображение в формате numpy.ndarray.
    """
    img = cv.imread(image_path)
    if img is None:
        raise ValueError(f"Не удалось прочитать изображение из {image_path}")
    return img


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    """
    Преобразуем цветное изображение в градации серого.

    :param img: Цветное изображение в формате numpy.ndarray.
    :return: Изображение в градациях серого в формате numpy.ndarray.
    """
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def save_image(save_path: str, img: np.ndarray) -> None:
    """
    Сохраняем изображение в файл.

    :param save_path: Путь к файлу для сохранения изображения.
    :param img: Изображение в формате numpy.ndarray, которое нужно сохранить.
    """
    cv.imwrite(save_path, img)
