import csv

class ImageIterator:
    def __init__(self, csv_path: str) -> None:
        """
        Конструктор класса Image_Iterator. Загружает пути изображений из файла аннотации.
        Parameter (csv_path): Путь к файлу аннотации.
        """
        self.csv_path = csv_path
        self.path_list = self._load_csv()
        self.limit = len(self.path_list)
        self.counter = 0

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        """
        Метод для получения следующего изображения.
        Return: Путь к следующему изображению.
        """
        if self.counter < self.limit:
            next_element = self.path_list[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def _load_csv(self) -> list:
        """
        Загружает пути к изображениям из CSV-файла.
        Return: Список абсолютных путей к изображениям.
        """
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Пропускаем заголовок
            path_list = list(row[1] for row in reader)
            return path_list
