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
        self.brightness_slider_l = None
        self.brightness_slider_p = None
        self.darkness_slider_l = None
        self.darkness_slider_p = None
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
            self.descLabels()
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

    def descLabels(self):
        desc1_label = QLabel('Liner methods', self)
        desc1_label.show()
        desc1_label.setGeometry(630, 475, 200, 30)

        desc2_label = QLabel('Power methods', self)
        desc2_label.show()
        desc2_label.setGeometry(950, 475, 200, 30)

    def showBrightness(self):
        # liner
        brightness_label_l = QLabel('Brightness factor', self)
        brightness_label_l.show()
        brightness_label_l.setGeometry(630, 550, 200, 30)

        self.brightness_slider_l = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider_l.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.brightness_slider_l.setGeometry(630, 600, 200, 30)
        self.brightness_slider_l.setMinimum(2)
        self.brightness_slider_l.setMaximum(5)
        self.brightness_slider_l.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.brightness_slider_l.setTickInterval(1)
        self.brightness_slider_l.valueChanged.connect(self.brightFactorL)
        self.brightness_slider_l.show()

        # power
        brightness_label_p = QLabel('Brightness factor', self)
        brightness_label_p.show()
        brightness_label_p.setGeometry(950, 550, 200, 30)

        self.brightness_slider_p = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider_p.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.brightness_slider_p.setGeometry(950, 600, 200, 30)
        self.brightness_slider_p.setMinimum(2)
        self.brightness_slider_p.setMaximum(5)
        self.brightness_slider_p.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.brightness_slider_p.setTickInterval(1)
        self.brightness_slider_p.valueChanged.connect(self.brightFactorP)
        self.brightness_slider_p.show()

    def showDarkness(self):
        # liner
        darkness_label_l = QLabel('Darkness factor', self)
        darkness_label_l.show()
        darkness_label_l.setGeometry(630, 650, 200, 30)

        self.darkness_slider_l = QSlider(Qt.Orientation.Horizontal, self)
        self.darkness_slider_l.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.darkness_slider_l.setGeometry(630, 700, 200, 30)
        self.darkness_slider_l.setMinimum(2)
        self.darkness_slider_l.setMaximum(5)
        self.darkness_slider_l.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.darkness_slider_l.setTickInterval(1)
        self.darkness_slider_l.valueChanged.connect(self.darkFactorL)
        self.darkness_slider_l.show()

        # power
        darkness_label_p = QLabel('Darkness factor', self)
        darkness_label_p.show()
        darkness_label_p.setGeometry(950, 650, 200, 30)

        self.darkness_slider_p = QSlider(Qt.Orientation.Horizontal, self)
        self.darkness_slider_p.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.darkness_slider_p.setGeometry(950, 700, 200, 30)
        self.darkness_slider_p.setMinimum(2)
        self.darkness_slider_p.setMaximum(5)
        self.darkness_slider_p.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.darkness_slider_p.setTickInterval(1)
        self.darkness_slider_p.valueChanged.connect(self.darkFactorP)
        self.darkness_slider_p.show()

    def showNegative(self):
        self.negative_checkbox = QCheckBox('Negative', self)
        self.negative_checkbox.toggled.connect(self.negative)
        self.negative_checkbox.move(630, 750)
        self.negative_checkbox.show()

    def brightFactorL(self):
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

    def brightFactorP(self):
        factor = (self.sender().value() / 10)
        n = 1.33
        new_pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = list(
                    (int(factor * colors[0] ** n), int(factor * colors[1] ** n), int(factor * colors[2] ** n), colors[3]))

                new_colors[0] = min(new_colors[0], 255)
                new_colors[1] = min(new_colors[1], 255)
                new_colors[2] = min(new_colors[2], 255)

                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def darkFactorL(self):
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

    def darkFactorP(self):
        factor = 1 - (self.sender().value() * 0.1)
        n = 0.8
        new_pixmap = QPixmap(self.pixmap.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = (int(factor * colors[0] ** n), int(factor * colors[1] ** n), int(factor * colors[2] ** n), colors[3])
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
