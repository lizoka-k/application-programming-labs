import argparse

def get_args() -> tuple[str, int, str, str]:
    """
    Функция для получения аргументов командной строки.
    Return: Кортеж с ключевым словом, количеством изображений, директорией для сохранения и путем к файлу аннотации.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Ключевое слово для поиска изображений")
    parser.add_argument("-n", "--number", type=int, required=True,
                        help="Количество изображений для скачивания (от 50 до 1000)")
    parser.add_argument("-d", "--imgdir", type=str, required=True, help="Директория для сохранения изображений")
    parser.add_argument("-f", "--annotation_file", type=str, required=True, help="Путь к файлу аннотации")

    arguments = parser.parse_args()

    if not (50 <= arguments.number <= 1000):
        raise ValueError("Количество изображений должно быть от 50 до 1000.")

    return arguments.keyword, arguments.number, arguments.imgdir, arguments.annotation_file
