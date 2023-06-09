import math
import sys
import funcs

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
        self.width = 1920
        self.height = 1080

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
        self.contrast_slider = None
        self.histogram_button = None
        self.roberts_h = None
        self.roberts_v = None
        self.prewitt_h = None
        self.prewitt_v = None
        self.sobel_h = None
        self.sobel_v = None
        self.laplace = None
        self.s_min = None
        self.s_max = None
        self.s_median = None
        self.pixmap1 = None
        self.pixmap2 = None

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
            self.showContrast()
            self.showHistogram()
            self.showFilters()
            self.showSFilters()

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
        mix_label.setGeometry(1500, 20, 200, 20)

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
        self.brightness_slider_l.valueChanged.connect(lambda: funcs.brightFactorL(self))
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
        self.brightness_slider_p.valueChanged.connect(lambda: funcs.brightFactorP(self))
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
        self.darkness_slider_l.valueChanged.connect(lambda: funcs.darkFactorL(self))
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
        self.darkness_slider_p.valueChanged.connect(lambda: funcs.darkFactorP(self))
        self.darkness_slider_p.show()

    def showNegative(self):
        self.negative_checkbox = QCheckBox('Negative', self)
        self.negative_checkbox.toggled.connect(lambda: funcs.negative(self))
        self.negative_checkbox.move(630, 750)
        self.negative_checkbox.show()

    def showContrast(self):
        contrast_label = QLabel('Contrast factor', self)
        contrast_label.show()
        contrast_label.setGeometry(1200, 20, 200, 30)

        self.contrast_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.contrast_slider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.contrast_slider.setGeometry(1200, 50, 200, 30)
        self.contrast_slider.setMinimum(-50)
        self.contrast_slider.setMaximum(50)
        self.contrast_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.contrast_slider.setTickInterval(50)
        self.contrast_slider.valueChanged.connect(lambda: funcs.contrast(self))
        self.contrast_slider.show()

    def showHistogram(self):
        self.histogram_button = QPushButton('Histogram', self)
        self.histogram_button.move(1200, 80)
        self.histogram_button.clicked.connect(lambda: funcs.generateHistogram(self))
        self.histogram_button.setVisible(True)

    def showFilters(self):
        filter_label = QLabel('Filters', self)
        filter_label.show()
        filter_label.setGeometry(1200, 120, 200, 30)

        self.roberts_h = QCheckBox('Roberts H', self)
        self.roberts_h.toggled.connect(lambda: funcs.filters(self))
        self.roberts_h.move(1200, 150)
        self.roberts_h.show()

        self.roberts_v = QCheckBox('Roberts V', self)
        self.roberts_v.toggled.connect(lambda: funcs.filters(self))
        self.roberts_v.move(1200, 180)
        self.roberts_v.show()

        self.prewitt_h = QCheckBox('Prewitt H', self)
        self.prewitt_h.toggled.connect(lambda: funcs.filters(self))
        self.prewitt_h.move(1200, 210)
        self.prewitt_h.show()

        self.prewitt_v = QCheckBox('Prewitt V', self)
        self.prewitt_v.toggled.connect(lambda: funcs.filters(self))
        self.prewitt_v.move(1200, 240)
        self.prewitt_v.show()

        self.sobel_h = QCheckBox('Sobel H', self)
        self.sobel_h.toggled.connect(lambda: funcs.filters(self))
        self.sobel_h.move(1200, 270)
        self.sobel_h.show()

        self.sobel_v = QCheckBox('Sobel V', self)
        self.sobel_v.toggled.connect(lambda: funcs.filters(self))
        self.sobel_v.move(1200, 300)
        self.sobel_v.show()

        self.laplace = QCheckBox('Laplace', self)
        self.laplace.toggled.connect(lambda: funcs.filters(self))
        self.laplace.move(1200, 330)
        self.laplace.show()

    def showSFilters(self):
        s_filter_label = QLabel('Statistical Filters', self)
        s_filter_label.show()
        s_filter_label.setGeometry(1200, 360, 200, 30)

        self.s_min = QCheckBox('Minimum', self)
        self.s_min.toggled.connect(lambda: funcs.sFilters(self))
        self.s_min.move(1200, 390)
        self.s_min.show()

        self.s_max = QCheckBox('Maximum', self)
        self.s_max.toggled.connect(lambda: funcs.sFilters(self))
        self.s_max.move(1200, 420)
        self.s_max.show()

        self.s_median = QCheckBox('Median', self)
        self.s_median.toggled.connect(lambda: funcs.sFilters(self))
        self.s_median.move(1200, 450)
        self.s_median.show()

    def showMixed(self):
        self.additive_checkbox = QCheckBox('Additive', self)
        self.additive_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.additive_checkbox.move(1500, 50)
        self.additive_checkbox.show()

        self.subtractive_checkbox = QCheckBox('Subtractive', self)
        self.subtractive_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.subtractive_checkbox.move(1500, 80)
        self.subtractive_checkbox.show()

        self.difference_checkbox = QCheckBox('Difference', self)
        self.difference_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.difference_checkbox.move(1500, 110)
        self.difference_checkbox.show()

        self.multiply_checkbox = QCheckBox('Multiply', self)
        self.multiply_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.multiply_checkbox.move(1500, 140)
        self.multiply_checkbox.show()

        self.screen_checkbox = QCheckBox('Screen', self)
        self.screen_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.screen_checkbox.move(1500, 170)
        self.screen_checkbox.show()

        self.negation_checkbox = QCheckBox('Negation', self)
        self.negation_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.negation_checkbox.move(1500, 200)
        self.negation_checkbox.show()

        self.darken_checkbox = QCheckBox('Darken', self)
        self.darken_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.darken_checkbox.move(1500, 230)
        self.darken_checkbox.show()

        self.lighten_checkbox = QCheckBox('Lighten', self)
        self.lighten_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.lighten_checkbox.move(1500, 260)
        self.lighten_checkbox.show()

        self.exclusion_checkbox = QCheckBox('Exclusion', self)
        self.exclusion_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.exclusion_checkbox.move(1500, 290)
        self.exclusion_checkbox.show()

        self.overlay_checkbox = QCheckBox('Overlay', self)
        self.overlay_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.overlay_checkbox.move(1500, 320)
        self.overlay_checkbox.show()

        self.hard_light_checkbox = QCheckBox('Hard light', self)
        self.hard_light_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.hard_light_checkbox.move(1500, 350)
        self.hard_light_checkbox.show()

        self.soft_light_checkbox = QCheckBox('Soft light', self)
        self.soft_light_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.soft_light_checkbox.move(1500, 380)
        self.soft_light_checkbox.show()

        self.color_dodge_checkbox = QCheckBox('Color dodge', self)
        self.color_dodge_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.color_dodge_checkbox.move(1500, 410)
        self.color_dodge_checkbox.show()

        self.color_burn_checkbox = QCheckBox('Color burn', self)
        self.color_burn_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.color_burn_checkbox.move(1500, 440)
        self.color_burn_checkbox.show()

        self.reflect_checkbox = QCheckBox('Reflect', self)
        self.reflect_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.reflect_checkbox.move(1500, 470)
        self.reflect_checkbox.show()

        self.reflect_checkbox = QCheckBox('Transparency', self)
        self.reflect_checkbox.toggled.connect(lambda: funcs.mixPhoto(self))
        self.reflect_checkbox.move(1500, 500)
        self.reflect_checkbox.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
