import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from img_iterator import ImageIterator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Настраивает пользовательский интерфейс главного окна.
        Parameter MainWindow (QMainWindow): Главное окно приложения.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 30, 116, 105))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_image.setFont(font)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.Download_image = QtWidgets.QPushButton(self.widget)
        self.Download_image.setObjectName("Download_image")
        self.verticalLayout.addWidget(self.Download_image)
        self.Delete_image = QtWidgets.QPushButton(self.widget)
        self.Delete_image.setObjectName("Delete_image")
        self.verticalLayout.addWidget(self.Delete_image)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Устанавливает текст на элементах интерфейса.
        Parameter MainWindow (QMainWindow): Главное окно приложения.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_image.setText(_translate("MainWindow", "TextLabel"))
        self.Download_image.setText(_translate("MainWindow", "PushButton"))
        self.Delete_image.setText(_translate("MainWindow", "PushButton"))

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Конструктор класса MainWindow. Инициализирует главное окно приложения.
        """
        super().__init__()
        self.setWindowTitle("Image Viewer")

        # Создаем виджеты
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(800, 600)

        self.next_button = QPushButton("Next Image", self)
        self.next_button.clicked.connect(self.show_next_image)

        self.load_button = QPushButton("Load Dataset", self)
        self.load_button.clicked.connect(self.load_dataset)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.next_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.image_iterator = None

    def load_dataset(self):
        """
        Метод для загрузки набора данных.
        Открывает диалоговое окно для выбора CSV файла и загружает пути к изображениям.
        """
        try:
            file, _ = QFileDialog.getOpenFileName(
                parent=self,
                caption="Выберите CSV файл аннотации",
                directory="C:/Users/lizak/PycharmProjects",
                filter="CSV Files (*.csv)"
            )
            if file:
                if not QtCore.QFile.exists(file):
                    self.show_message_critical("Файл не найден")
                    return

                self.image_iterator = ImageIterator(file)
                self.show_next_image()
            else:
                self.show_message_critical("Пожалуйста, выберите корректный CSV файл")
        except Exception as e:
            self.show_message_critical(f"Произошла ошибка при открытии файла: {e}")

    def show_next_image(self):
        """
        Метод для отображения следующего изображения.
        Проверяет, загружен ли итератор изображений, и отображает следующее изображение.
        """
        if not self.image_iterator:
            self.show_message_critical("Сначала загрузите CSV файл")
            return

        try:
            # Получаем следующий путь изображения
            self.current_image_path = next(self.image_iterator)
            pixmap = QPixmap(self.current_image_path)

            if pixmap.isNull():
                self.show_message_warning("Изображение не найдено")
            else:
                scaled_pixmap = pixmap.scaled(self.image_label.size(),
                                              QtCore.Qt.KeepAspectRatio,
                                              QtCore.Qt.SmoothTransformation)
                self.image_label.setPixmap(scaled_pixmap)
        except StopIteration:
            self.image_label.setText("Больше нет изображений.")
        except Exception as e:
            self.show_message_critical(f"Произошла ошибка: {e}")

    def show_message_warning(self, text: str):
        """
        Метод для отображения предупреждающего сообщения.
        Parameter(text): Текст сообщения.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Предупреждение")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def show_message_critical(self, text: str):
        """
        Метод для отображения сообщения об ошибке.
        Parameter:
        text (str): Текст сообщения.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())