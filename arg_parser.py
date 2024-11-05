import argparse


def get_args() -> tuple[str, str]:
    """
    Считываем аргументы командной строки.

    :return: Кортеж из двух строк: путь к изображению и путь для сохранения.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", type=str, required=True,
                        help="Путь к изображению для преобразования")
    parser.add_argument("-s", "--save_dir", type=str, required=True,
                        help="Путь для сохранения преобразованного изображения")
    return parser.parse_args().image_path, parser.parse_args().save_dir
