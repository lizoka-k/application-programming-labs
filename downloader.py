import os

from icrawler.builtin import BingImageCrawler

def download_images(keyword: str, number: int, imgdir: str) -> None:
    """
    Функция скачивает изображения из Bing по заданному слову и сохраняет их в указанной директории.
    Также очищает директорию каждый раз при запуске скрипта.
    Parameter (keyword): Ключевое слово для поиска изображений.
    Parameter (number): Количество изображений, которое хотим скачать(от 50 до 1000).
    Parameter (imgdir): Директория для сохранения изображений.
    """
    if not os.path.isdir(imgdir):
        os.mkdir(imgdir)
    else:
        # Очищаем директорию от старых изображений
        for filename in os.listdir(imgdir):
            os.remove(os.path.join(imgdir, filename))

    crawler = BingImageCrawler(
        storage={"root_dir": imgdir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )
    crawler.crawl(keyword=keyword, max_num=number)
