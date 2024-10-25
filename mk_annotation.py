import csv
import os

def create_annotation(imgdir: str, csv_path: str) -> None:
    """
    Функция создает CSV-файл аннотации с абсолютными и относительными путями к каждому изображению.
    Parameter (imgdir): Директория, в которой хранятся изображения.
    Parameter (csv_path): Путь к файлу аннотации.
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation_file:
        writer = csv.writer(annotation_file)
        headers = ['Relative path', 'Absolute path']
        writer.writerow(headers)

        for file in os.listdir(imgdir):
            if file.endswith(('.png', '.jpg', '.jpeg')):  # Убеждаемся, что это изображение
                relative_path = os.path.relpath(os.path.join(imgdir, file), start = os.path.dirname(csv_path))
                absolute_path = os.path.abspath(os.path.join(imgdir, file))
                writer.writerow([relative_path, absolute_path])
