import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Photo Editor'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.label = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        upload_button = QPushButton('Upload photo', self)
        upload_button.setToolTip('This is load photo')
        upload_button.move(10, 10)
        upload_button.clicked.connect(self.on_click)

        self.label = QLabel(self)
        self.label.move(10, 50)

        self.show()

    @pyqtSlot()
    def on_click(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', 'photos', 'Image file(*.jpg)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(500, 400)
        self.label.setPixmap(pixmap)

        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
