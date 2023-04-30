import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton, QSlider, QVBoxLayout, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSlot, Qt


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'Photo Editor'
        self.left = 50
        self.top = 50
        self.width = 1250
        self.height = 800

        self.org_photo = None
        self.mod_photo = None
        self.upload_button = None
        self.brightness_slider = None

        layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.org_photo = QLabel(self)
        self.org_photo.move(10, 50)

        self.mod_photo = QLabel(self)
        self.mod_photo.move(600, 50)

        self.uploadPhoto()

        self.show()

    def uploadPhoto(self):
        self.upload_button = QPushButton('Upload photo', self)
        self.upload_button.setToolTip('This is load photo')
        self.upload_button.move(10, 10)
        self.upload_button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', 'photos', 'Image file(*.jpg)')
        imagePath = image[0]
        if imagePath:
            pixmap = QPixmap(imagePath)
            pixmap = pixmap.scaled(500, 400)
            self.org_photo.setPixmap(pixmap)
            self.org_photo.adjustSize()
            self.mod_photo.setPixmap(pixmap)
            self.mod_photo.adjustSize()
            self.upload_button.setVisible(False)
            self.showBrightness()
            self.photoLabels()

    def photoLabels(self):
        photo1_label = QLabel('Original Photo', self)
        photo1_label.show()
        photo1_label.setGeometry(10, 20, 200, 20)

        photo2_label = QLabel('Modify Photo', self)
        photo2_label.show()
        photo2_label.setGeometry(600, 20, 200, 20)

    def showBrightness(self):
        brightness_label = QLabel('Brightness factor', self)
        brightness_label.show()
        brightness_label.setGeometry(30, 450, 200, 30)

        self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.brightness_slider.setGeometry(30, 500, 200, 30)
        self.brightness_slider.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
