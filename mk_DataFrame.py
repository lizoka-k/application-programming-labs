import cv2
import matplotlib.pyplot as plt
import pandas as pd


def create_dataframe(csv_file):
    """
    Функция создает DataFrame из CSV-файла с абсолютными и относительными путями к изображениям.

    Parameter:
        csv_file (str): Путь к CSV-файлу с аннотацией изображений.

    Returns:
        pd.DataFrame: DataFrame с абсолютными и относительными путями, размерами изображений и площадью.
    """
    df = pd.read_csv(csv_file)
    df.columns = ['Relative Path', 'Absolute Path']

    heights = []
    widths = []
    channels = []

    for absolute_path in df['Absolute Path']:
        image = cv2.imread(absolute_path)
        if image is not None:
            height, width, channel = image.shape
            heights.append(height)
            widths.append(width)
            channels.append(channel)
        else:
            heights.append(None)
            widths.append(None)
            channels.append(None)

    df['Height'] = heights
    df['Width'] = widths
    df['Channels'] = channels
    df['Area'] = df['Height'] * df['Width']

    df = df.sort_values(by='Area')

    return df


def filter_dataframe(df, max_width, max_height):
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


def plot_area_distribution(df):
    """
    Функция строит гистограмму распределения площадей изображений.

    Parameter:
        df (pd.DataFrame): DataFrame с информацией о площадях изображений.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Area'].dropna(), bins=30, color='blue', alpha=0.7)
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения (пиксели)')
    plt.ylabel('Частота')
    plt.grid()
    plt.show()


def display_statistics(df):
    """
    Функция отображает статистическую информацию для столбцов с размерами изображений.

    Parameter:
        df (pd.DataFrame): DataFrame с размерами изображений.
    """
    print("Статистическая информация:")
    print(df[['Height', 'Width', 'Channels']].describe())
