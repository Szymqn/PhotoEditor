import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton, QSlider, QVBoxLayout, QMainWindow, \
    QCheckBox
from PyQt6.QtGui import QPixmap, QImage, QColor, QPainter
from PyQt6.QtCore import pyqtSlot, Qt, QPoint, QSize


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'Photo Editor'
        self.left = 50
        self.top = 50
        self.width = 1250
        self.height = 800

        self.photo_w = 500
        self.photo_h = 400

        self.org_photo = None
        self.mod_photo = None
        self.upload_button = None
        self.brightness_slider = None
        self.darkness_slider = None
        self.negative_checkbox = None
        self.pixmap = None

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
            self.pixmap = pixmap.scaled(self.photo_w, self.photo_h)
            self.org_photo.setPixmap(self.pixmap)
            self.org_photo.adjustSize()
            self.mod_photo.setPixmap(self.pixmap)
            self.mod_photo.adjustSize()
            self.upload_button.setVisible(False)
            self.photoLabels()
            self.showBrightness()
            self.showDarkness()
            self.showNegative()

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
        self.brightness_slider.setMinimum(2)
        self.brightness_slider.setMaximum(5)
        self.brightness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.brightness_slider.setTickInterval(1)
        self.brightness_slider.valueChanged.connect(self.brightFactor)
        self.brightness_slider.show()

    def showDarkness(self):
        darkness_label = QLabel('Darkness factor', self)
        darkness_label.show()
        darkness_label.setGeometry(30, 550, 200, 30)

        self.darkness_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.darkness_slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.darkness_slider.setGeometry(30, 600, 200, 30)
        self.darkness_slider.setMinimum(2)
        self.darkness_slider.setMaximum(5)
        self.darkness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.darkness_slider.setTickInterval(1)
        self.darkness_slider.valueChanged.connect(self.darkFactor)
        self.darkness_slider.show()

    def showNegative(self):
        self.negative_checkbox = QCheckBox('Negative', self)
        self.negative_checkbox.toggled.connect(self.negative)
        self.negative_checkbox.move(30, 650)
        self.negative_checkbox.show()

    def brightFactor(self):
        factor = 1 + (self.sender().value() * 0.1)
        new_pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = list(
                    (int(colors[0] * factor), int(colors[1] * factor), int(colors[2] * factor), colors[3]))

                new_colors[0] = min(new_colors[0], 255)
                new_colors[1] = min(new_colors[1], 255)
                new_colors[2] = min(new_colors[2], 255)

                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def darkFactor(self):
        factor = 1 - (self.sender().value() * 0.1)
        new_pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = (int(colors[0] * factor), int(colors[1] * factor), int(colors[2] * factor), colors[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def negative(self):

        new_pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                if self.sender().isChecked():
                    new_colors = (int(255 - colors[0]), int(255 - colors[1]), int(255 - colors[2]), colors[3])
                else:
                    new_colors = (int(colors[0]), int(colors[1]), int(colors[2]), colors[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
