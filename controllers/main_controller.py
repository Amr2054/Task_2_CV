import cv2
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt
from utils.converters import cv_to_pixmap
from controllers.canny_edge_detector_controller import Canny_EdgeDetector_Controller

class MainController:
    def __init__(self, ui, model, window):
        self.ui = ui
        self.model = model
        self.window = window

        self.canny_edge_detector = Canny_EdgeDetector_Controller(self.ui,self.model,self.display_image)

        self._connect_signals()

    def _connect_signals(self):
        # Connect File -> Open
        self.ui.actionOpen_Image.triggered.connect(self.load_image)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.window, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            # Read image via OpenCV and store in Model
            self.model.original_image = cv2.imread(file_path)
            self.model.processed_image = None
            self.display_image(self.model.original_image)


    def display_image(self, cv_img):
        pixmap = cv_to_pixmap(cv_img)
        if pixmap:
            # Scale the pixmap to fit the label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.ui.imageCanvas.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.imageCanvas.setPixmap(scaled_pixmap)