from PyQt6.QtGui import QPixmap, QColor, QPainter


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
            new_colors = (
            int(factor * colors[0] ** n), int(factor * colors[1] ** n), int(factor * colors[2] ** n), colors[3])
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
