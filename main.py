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
        self.width = 1500
        self.height = 960

        self.photo_w = 500
        self.photo_h = 400

        self.org_photo1 = None
        self.org_photo2 = None
        self.mod_photo = None
        self.upload_button1 = None
        self.upload_button2 = None
        self.brightness_slider_l = None
        self.brightness_slider_p = None
        self.darkness_slider_l = None
        self.darkness_slider_p = None
        self.negative_checkbox = None
        self.additive_checkbox = None
        self.pixmap1 = None
        self.pixmap2 = None

        layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.org_photo1 = QLabel(self)
        self.org_photo1.move(10, 50)

        self.org_photo2 = QLabel(self)
        self.org_photo2.move(10, 475)

        self.mod_photo = QLabel(self)
        self.mod_photo.move(600, 50)

        self.uploadPhoto()

        self.show()

    def uploadPhoto(self):
        self.upload_button1 = QPushButton('Upload photo', self)
        self.upload_button1.setToolTip('This is load photo')
        self.upload_button1.move(10, 10)
        self.upload_button1.clicked.connect(self.uploadFirst)

        self.upload_button2 = QPushButton('Upload photo', self)
        self.upload_button2.setToolTip('This is load photo')
        self.upload_button2.move(10, 450)
        self.upload_button2.clicked.connect(self.uploadSecond)

    @pyqtSlot()
    def uploadFirst(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', 'photos', 'Image file(*.jpg)')
        imagePath = image[0]
        if imagePath:
            pixmap = QPixmap(imagePath)
            self.pixmap1 = pixmap.scaled(self.photo_w, self.photo_h)
            self.org_photo1.setPixmap(self.pixmap1)
            self.org_photo1.adjustSize()
            self.mod_photo.setPixmap(self.pixmap1)
            self.mod_photo.adjustSize()
            self.upload_button1.setVisible(False)
            self.photoLabels()
            self.descLabels()
            self.showBrightness()
            self.showDarkness()
            self.showNegative()

    @pyqtSlot()
    def uploadSecond(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', 'photos', 'Image file(*.jpg)')
        imagePath = image[0]
        if imagePath:
            pixmap = QPixmap(imagePath)
            self.pixmap2 = pixmap.scaled(self.photo_w, self.photo_h)
            self.org_photo2.setPixmap(self.pixmap2)
            self.org_photo2.adjustSize()
            self.upload_button2.setVisible(False)
            self.mixedLabels()
            self.showMixed()

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

    def mixedLabels(self):
        mix_label = QLabel('Blending methods', self)
        mix_label.show()
        mix_label.setGeometry(1200, 20, 200, 20)

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

    def showMixed(self):
        self.additive_checkbox = QCheckBox('Additive', self)
        self.additive_checkbox.toggled.connect(self.mixPhoto)
        self.additive_checkbox.move(1200, 50)
        self.additive_checkbox.show()

        self.additive_checkbox = QCheckBox('Subtractive', self)
        self.additive_checkbox.toggled.connect(self.mixPhoto)
        self.additive_checkbox.move(1200, 80)
        self.additive_checkbox.show()

        self.additive_checkbox = QCheckBox('Difference', self)
        self.additive_checkbox.toggled.connect(self.mixPhoto)
        self.additive_checkbox.move(1200, 110)
        self.additive_checkbox.show()

    def brightFactorL(self):
        factor = 1 + (self.sender().value() * 0.1)
        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap1.toImage().pixel(i, j)
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
        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap1.toImage().pixel(i, j)
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
        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap1.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = (int(colors[0] * factor), int(colors[1] * factor), int(colors[2] * factor), colors[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def darkFactorP(self):
        factor = 1 - (self.sender().value() * 0.1)
        n = 0.8
        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap1.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                new_colors = (int(factor * colors[0] ** n), int(factor * colors[1] ** n), int(factor * colors[2] ** n), colors[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def negative(self):
        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c = self.pixmap1.toImage().pixel(i, j)
                colors = QColor(c).getRgb()
                if self.sender().isChecked():
                    new_colors = (int(255 - colors[0]), int(255 - colors[1]), int(255 - colors[2]), colors[3])
                else:
                    new_colors = (int(colors[0]), int(colors[1]), int(colors[2]), colors[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)

    def mixPhoto(self):
        global new_colors

        new_pixmap = QPixmap(self.pixmap1.size())
        painter = QPainter(new_pixmap)

        for i in range(self.photo_w):
            for j in range(self.photo_h):
                c1 = self.pixmap1.toImage().pixel(i, j)
                colors1 = QColor(c1).getRgb()
                c2 = self.pixmap2.toImage().pixel(i, j)
                colors2 = QColor(c2).getRgb()
                if self.sender().isChecked():
                    match self.sender().text():
                        case 'Additive':
                            new_colors = (int(min(colors1[0] + colors2[0], 255)), int(min(colors1[1] + colors2[1], 255)), int(min(colors1[2] + colors2[2], 255)), colors1[3])
                        case 'Subtractive':
                            new_colors = (int(min(colors1[0] + colors2[0] - 1, 255)), int(min(colors1[1] + colors2[1] - 1, 255)), int(min(colors1[2] + colors2[2] - 1, 255)), colors1[3])
                        case 'Difference':
                            new_colors = (int(min(abs(colors1[0] - colors2[0]), 255)), int(min(abs(colors1[1] - colors2[1]), 255)), int(min(abs(colors1[2] - colors2[2]), 255)), colors1[3])

                else:
                    new_colors = (int(colors1[0]), int(colors1[1]), int(colors1[2]), colors1[3])
                painter.setPen(QColor(*new_colors))
                painter.drawPoint(i, j)

        painter.end()
        self.mod_photo.setPixmap(new_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
