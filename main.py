import argparse

import mk_DataFrame


def get_args():
    parser = argparse.ArgumentParser(description='Обработка изображений и создание DataFrame.')
    parser.add_argument('-c', '--csv', required=True, help='Путь к CSV-файлу аннотации.')
    return parser.parse_args()

def main():
    args = get_args()

    try:
        df = mk_DataFrame.create_dataframe(args.csv)

        mk_DataFrame.display_statistics(df)

        max_width = int(input("Введите максимальную ширину: "))
        max_height = int(input("Введите максимальную высоту: "))

        filtered_df = mk_DataFrame.filter_dataframe(df, max_width, max_height)

        mk_DataFrame.plot_area_distribution(filtered_df)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()

