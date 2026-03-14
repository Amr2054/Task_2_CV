from PySide6.QtGui import QImage, QPixmap


def cv_to_pixmap(cv_img):
    height, width, channel = cv_img.shape
    bytes_per_line = 3 * width
    q_img = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
    return QPixmap.fromImage(q_img)