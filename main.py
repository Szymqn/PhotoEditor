import math
import sys

from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtGui import QPixmap, QColor, QPainter
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton, QSlider, QVBoxLayout, QMainWindow, \
    QCheckBox


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
        self.subtractive_checkbox = None
        self.difference_checkbox = None
        self.multiply_checkbox = None
        self.screen_checkbox = None
        self.negation_checkbox = None
        self.darken_checkbox = None
        self.lighten_checkbox = None
        self.exclusion_checkbox = None
        self.overlay_checkbox = None
        self.hard_light_checkbox = None
        self.soft_light_checkbox = None
        self.color_dodge_checkbox = None
        self.color_burn_checkbox = None
        self.reflect_checkbox = None
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

        self.subtractive_checkbox = QCheckBox('Subtractive', self)
        self.subtractive_checkbox.toggled.connect(self.mixPhoto)
        self.subtractive_checkbox.move(1200, 80)
        self.subtractive_checkbox.show()

        self.difference_checkbox = QCheckBox('Difference', self)
        self.difference_checkbox.toggled.connect(self.mixPhoto)
        self.difference_checkbox.move(1200, 110)
        self.difference_checkbox.show()

        self.multiply_checkbox = QCheckBox('Multiply', self)
        self.multiply_checkbox.toggled.connect(self.mixPhoto)
        self.multiply_checkbox.move(1200, 140)
        self.multiply_checkbox.show()

        self.screen_checkbox = QCheckBox('Screen', self)
        self.screen_checkbox.toggled.connect(self.mixPhoto)
        self.screen_checkbox.move(1200, 170)
        self.screen_checkbox.show()

        self.negation_checkbox = QCheckBox('Negation', self)
        self.negation_checkbox.toggled.connect(self.mixPhoto)
        self.negation_checkbox.move(1200, 200)
        self.negation_checkbox.show()

        self.darken_checkbox = QCheckBox('Darken', self)
        self.darken_checkbox.toggled.connect(self.mixPhoto)
        self.darken_checkbox.move(1200, 230)
        self.darken_checkbox.show()

        self.lighten_checkbox = QCheckBox('Lighten', self)
        self.lighten_checkbox.toggled.connect(self.mixPhoto)
        self.lighten_checkbox.move(1200, 260)
        self.lighten_checkbox.show()

        self.exclusion_checkbox = QCheckBox('Exclusion', self)
        self.exclusion_checkbox.toggled.connect(self.mixPhoto)
        self.exclusion_checkbox.move(1200, 290)
        self.exclusion_checkbox.show()

        self.overlay_checkbox = QCheckBox('Overlay', self)
        self.overlay_checkbox.toggled.connect(self.mixPhoto)
        self.overlay_checkbox.move(1200, 320)
        self.overlay_checkbox.show()

        self.hard_light_checkbox = QCheckBox('Hard light', self)
        self.hard_light_checkbox.toggled.connect(self.mixPhoto)
        self.hard_light_checkbox.move(1200, 350)
        self.hard_light_checkbox.show()

        self.soft_light_checkbox = QCheckBox('Soft light', self)
        self.soft_light_checkbox.toggled.connect(self.mixPhoto)
        self.soft_light_checkbox.move(1200, 380)
        self.soft_light_checkbox.show()

        self.color_dodge_checkbox = QCheckBox('Color dodge', self)
        self.color_dodge_checkbox.toggled.connect(self.mixPhoto)
        self.color_dodge_checkbox.move(1200, 410)
        self.color_dodge_checkbox.show()

        self.color_burn_checkbox = QCheckBox('Color burn', self)
        self.color_burn_checkbox.toggled.connect(self.mixPhoto)
        self.color_burn_checkbox.move(1200, 440)
        self.color_burn_checkbox.show()

        self.reflect_checkbox = QCheckBox('Reflect', self)
        self.reflect_checkbox.toggled.connect(self.mixPhoto)
        self.reflect_checkbox.move(1200, 470)
        self.reflect_checkbox.show()

        self.reflect_checkbox = QCheckBox('Transparency', self)
        self.reflect_checkbox.toggled.connect(self.mixPhoto)
        self.reflect_checkbox.move(1200, 500)
        self.reflect_checkbox.show()

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
                            new_colors = (
                                int(min(colors1[0] + colors2[0], 255)),
                                int(min(colors1[1] + colors2[1], 255)),
                                int(min(colors1[2] + colors2[2], 255)),
                                colors1[3])
                        case 'Subtractive':
                            new_colors = (
                                int(min(colors1[0] + colors2[0] - 1, 255)),
                                int(min(colors1[1] + colors2[1] - 1, 255)),
                                int(min(colors1[2] + colors2[2] - 1, 255)),
                                colors1[3])
                        case 'Difference':
                            new_colors = (
                                int(min(abs(colors1[0] - colors2[0]), 255)),
                                int(min(abs(colors1[1] - colors2[1]), 255)),
                                int(min(abs(colors1[2] - colors2[2]), 255)),
                                colors1[3])
                        case 'Multiply':
                            new_colors = (
                                int(min(colors1[0] * colors2[0], 255)),
                                int(min(colors1[1] * colors2[1], 255)),
                                int(min(colors1[2] * colors2[2], 255)),
                                colors1[3])
                        case 'Screen':
                            new_colors = (
                                int(255 - (255 - colors1[0]) * (255 - colors2[0])),
                                int(255 - (255 - colors1[1]) * (255 - colors2[1])),
                                int(255 - (255 - colors1[2]) * (255 - colors2[2])),
                                colors1[3])
                        case 'Negation':
                            new_colors = (
                                int(255 - abs(255 - colors1[0] - colors2[0])),
                                int(255 - abs(255 - colors1[1] - colors2[1])),
                                int(255 - abs(255 - colors1[2] - colors2[2])),
                                colors1[3])
                        case 'Darken':
                            new_colors = (
                                int(colors1[0] if colors1[0] < colors2[0] else colors2[0]),
                                int(colors1[1] if colors1[1] < colors2[1] else colors2[1]),
                                int(colors1[2] if colors1[2] < colors2[2] else colors2[2]),
                                colors1[3])
                        case 'Lighten':
                            new_colors = (
                                int(colors1[0] if colors1[0] > colors2[0] else colors2[0]),
                                int(colors1[1] if colors1[1] > colors2[1] else colors2[1]),
                                int(colors1[2] if colors1[2] > colors2[2] else colors2[2]),
                                colors1[3])
                        case 'Exclusion':
                            new_colors = (
                                int(colors1[0] + colors2[0] - (2 * colors1[0] * colors2[0] / 255)),
                                int(colors1[1] + colors2[1] - (2 * colors1[1] * colors2[1] / 255)),
                                int(colors1[2] + colors2[2] - (2 * colors1[2] * colors2[2] / 255)),
                                colors1[3])
                        case 'Overlay':
                            new_colors = (
                                int(2 * colors1[0] * colors2[0] / 255 if colors1[0] / 255 < 0.5 else 1 - 2 * (1 - colors1[0] / 255) * (1 - colors2[0] / 255) * 255),
                                int(2 * colors1[1] * colors2[1] / 255 if colors1[1] / 255 < 0.5 else 1 - 2 * (1 - colors1[1] / 255) * (1 - colors2[1] / 255) * 255),
                                int(2 * colors1[2] * colors2[2] / 255 if colors1[2] / 255 < 0.5 else 1 - 2 * (1 - colors1[2] / 255) * (1 - colors2[2] / 255) * 255),
                                colors1[3])
                        case 'Hard light':
                            new_colors = (
                                int(2 * colors1[0] * colors2[0] / 255 if colors2[0] / 255 < 0.5 else 1 - 2 * (1 - colors1[0] / 255) * (1 - colors2[0] / 255) * 255),
                                int(2 * colors1[1] * colors2[1] / 255 if colors2[1] / 255 < 0.5 else 1 - 2 * (1 - colors1[1] / 255) * (1 - colors2[1] / 255) * 255),
                                int(2 * colors1[2] * colors2[2] / 255 if colors2[2] / 255 < 0.5 else 1 - 2 * (1 - colors1[2] / 255) * (1 - colors2[2] / 255) * 255),
                                colors1[3])
                        case 'Soft light':
                            new_colors = (
                                int(2 * colors1[0] * colors2[0] / 255 + (colors1[0] ** 2) * (1 - 2 * colors2[0] / 255) / 255 if colors2[0] / 255 < 0.5 else math.sqrt(colors1[0] / 255) * (2 * colors2[0] / 255 - 1) + (2 * colors1[0] / 255) * (1 - colors2[0] / 255) * 255),
                                int(2 * colors1[1] * colors2[1] / 255 + (colors1[1] ** 2) * (1 - 2 * colors2[1] / 255) / 255 if colors2[1] / 255 < 0.5 else math.sqrt(colors1[1] / 255) * (2 * colors2[1] / 255 - 1) + (2 * colors1[1] / 255) * (1 - colors2[1] / 255) * 255),
                                int(2 * colors1[2] * colors2[2] / 255 + (colors1[2] ** 2) * (1 - 2 * colors2[2] / 255) / 255 if colors2[2] / 255 < 0.5 else math.sqrt(colors1[2] / 255) * (2 * colors2[2] / 255 - 1) + (2 * colors1[2] / 255) * (1 - colors2[2] / 255) * 255),
                                colors1[3])
                        case 'Color dodge':
                            new_colors = (
                                int(255 if colors1[0] == 255 else min((colors2[0] << 8) / (255 - colors1[0]), 255)),
                                int(255 if colors1[1] == 255 else min((colors2[1] << 8) / (255 - colors1[1]), 255)),
                                int(255 if colors1[2] == 255 else min((colors2[2] << 8) / (255 - colors1[2]), 255)),
                                colors1[3])
                        case 'Color burn':
                            new_colors = (
                                int(0 if colors1[0] == 0 else max(255 - int((255 - colors2[0]) << 8) / colors1[0], 0)),
                                int(0 if colors1[1] == 0 else max(255 - int((255 - colors2[1]) << 8) / colors1[1], 0)),
                                int(0 if colors1[2] == 0 else max(255 - int((255 - colors2[2]) << 8) / colors1[2], 0)),
                                colors1[3])
                        case 'Reflect':
                            new_colors = (
                                int(255 - abs(255 - colors1[0] - colors2[0])),
                                int(255 - abs(255 - colors1[1] - colors2[1])),
                                int(255 - abs(255 - colors1[2] - colors2[2])),
                                colors1[3]
                            )
                        case 'Transparency':
                            new_colors = (
                                int(255 - abs(255 - colors1[0] - colors2[0])),
                                int(255 - abs(255 - colors1[1] - colors2[1])),
                                int(255 - abs(255 - colors1[2] - colors2[2])),
                                int(0.5 * colors1[3] + 0.5 * colors2[3])
                            )
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
