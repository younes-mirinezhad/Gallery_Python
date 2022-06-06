from PySide6.QtCore import Property, Signal, QPoint
from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtGui import QPainter, QImage


#--------------------------------------------------------------
# This ViewPort is using Opencv
import cv2
class ViewPort(QQuickPaintedItem):
    def __init__(self):
        super(ViewPort, self).__init__()
        self._picPath = ""

    def paint(self, painter: QPainter):
        _image = cv2.imread(self._picPath)
        if min(_image.shape[0], _image.shape[1]) <= 0: return
        out_w = self.size().toSize().width()
        out_h = self.size().toSize().height()
        img = self.image_resize(_image, out_w, out_h)

        height, width, channel = img.shape
        bytesPerLine = channel * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        x = (out_w - width) / 2.0
        y = (out_h - height) / 2.0
        _startPoint = QPoint(x, y)
        
        painter.drawImage(_startPoint, qImg)

    picPathChanged = Signal()
    @Property(str, notify=picPathChanged)
    def picPath(self):
        return self._picPath
    @picPath.setter
    def picPath(self, value):
        self._picPath = value
        self.update()
        self.picPathChanged.emit()

    def image_resize(self, image, out_w, out_h):
        h, w = image.shape[:2]
        w_ratio = float(out_w) / w
        h_ratio = float(out_h) / h
        ratio = min(w_ratio, h_ratio)
        dim = (int(w*ratio), int(h*ratio))

        # resized = cv2.resize(image, dsize=(0, 0), fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
        resized = cv2.resize(image, dim, cv2.INTER_AREA)

        return resized

#--------------------------------------------------------------
# This ViewPort is using just QImage
# from PySide6.QtGui import Qt
# class ViewPort(QQuickPaintedItem):
#     def __init__(self):
#         super(ViewPort, self).__init__()
#         self._picPath = ""

#     def paint(self, painter: QPainter):
#         _image = QImage(self._picPath)
#         if _image.isNull(): return

#         w = self.size().toSize().width()
#         h = self.size().toSize().height()
#         img = _image.scaled(w, h, Qt.KeepAspectRatio)
#         x = (w - img.width()) / 2.0
#         y = (h - img.height()) / 2.0
#         _startPoint = QPoint(x, y)

#         painter.drawImage(_startPoint, img)

#     picPathChanged = Signal()
#     @Property(str, notify=picPathChanged)
#     def picPath(self):
#         return self._picPath
#     @picPath.setter
#     def picPath(self, value):
#         self._picPath = value
#         self.update()
#         self.picPathChanged.emit()
