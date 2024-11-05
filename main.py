import cv2 as cv
import matplotlib.pyplot as plt

from arg_parser import get_args
from image_processing import read_image, convert_to_grayscale, save_image
from histogram import calculate_histogram, plot_histogram


def main():
    img_path, save_dir = get_args()

    try:
        img = read_image(img_path)
        print(f"Размер изображения: {img.shape[1]} x {img.shape[0]} пикселей")

        gray_img = convert_to_grayscale(img)
        save_image(save_dir, gray_img)

        hist_r, hist_g, hist_b = calculate_histogram(img)
        plot_histogram((hist_r, hist_g, hist_b))

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.title("Исходное изображение")
        plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title("Преобразованное изображение (полутоновое)")
        plt.imshow(gray_img, cmap='gray')
        plt.axis('off')

        plt.show()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()


