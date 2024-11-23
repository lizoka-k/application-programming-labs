import cv2
import matplotlib.pyplot as plt
import pandas as pd

def read_csv_file(csv_file: str) -> pd.DataFrame:
    """
    Функция читает CSV-файл и создает DataFrame с абсолютными и относительными путями к изображениям.
    Parameters:
        csv_file (str): Путь к CSV-файлу с аннотацией изображений.
    Returns:
        pd.DataFrame: DataFrame с абсолютными и относительными путями.
    """
    df = pd.read_csv(csv_file)
    df.columns = ['Relative Path', 'Absolute Path']
    return df

def get_image_dimensions(absolute_path: str) -> (int, int, int):
    """
    Функция получает размеры изображения по абсолютному пути.
    Parameters:
        absolute_path (str): Абсолютный путь к изображению.
    Returns:
        (int, int, int): Высота, ширина и количество каналов изображения.
    """
    image = cv2.imread(absolute_path)
    if image is not None:
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2]
        return height, width, channels
    else:
        return None, None, None

def sort_dataframe_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция сортирует DataFrame по площади изображений.
    Parameters:
        df (pd.DataFrame): DataFrame с информацией о площадях изображений.
    Returns:
        pd.DataFrame: Отсортированный DataFrame.
    """
    return df.sort_values(by='Area')

def create_dataframe(csv_file: str) -> pd.DataFrame:
    """
    Функция создает DataFrame из CSV-файла с абсолютными и относительными путями к изображениям.
    Parameters:
        csv_file (str): Путь к CSV-файлу с аннотацией изображений.
    Returns:
        pd.DataFrame: DataFrame с абсолютными и относительными путями, размерами изображений и площадью.
    """
    df = read_csv_file(csv_file)

    heights = []
    widths = []
    channels = []

    for absolute_path in df['Absolute Path']:
        height, width, channel = get_image_dimensions(absolute_path)
        heights.append(height)
        widths.append(width)
        channels.append(channel)

    df['Height'] = heights
    df['Width'] = widths
    df['Channels'] = channels
    df['Area'] = df['Height'] * df['Width']

    df = sort_dataframe_by_area(df)

    return df

def filter_dataframe(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Функция фильтрует DataFrame по максимальной ширине и высоте изображений.
    Parameters:
        df (pd.DataFrame): Исходный DataFrame.
        max_width (int): Максимальная ширина изображения.
        max_height (int): Максимальная высота изображения.
    Returns:
        pd.DataFrame: Отфильтрованный DataFrame.
    """
    filtered_df = df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]
    return filtered_df

def plot_area_distribution(df: pd.DataFrame) -> None:
    """
    Функция строит гистограмму распределения площадей изображений.
    Parameters:
        df (pd.DataFrame): DataFrame с информацией о площадях изображений.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Area'].dropna(), bins=30, color='blue', alpha=0.7)
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения (пиксели)')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()

def display_statistics(df: pd.DataFrame) -> None:
    """
    Функция отображает статистическую информацию для столбцов с размерами изображений.
    Parameters:
        df (pd.DataFrame): DataFrame с размерами изображений.
    """
    print("Статистическая информация:")
    print(df[['Height', 'Width', 'Channels']].describe())
