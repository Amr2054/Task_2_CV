import cv2
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt
from utils.converters import cv_to_pixmap
from controllers.canny_edge_detector_controller import Canny_EdgeDetector_Controller
from controllers.greedy_snake_controller import GreedySnakeController

class MainController:
    def __init__(self, ui, model, window):
        self.ui = ui
        self.model = model
        self.window = window

        self.canny_edge_detector = Canny_EdgeDetector_Controller(self.ui,self.model,self.display_processed_image)
        self.greedy_snake_controller = GreedySnakeController(self.ui, self.window)
        self._connect_signals()

    def _connect_signals(self):
        # Connect File -> Open
        self.ui.btnOpenImage.clicked.connect(self.load_image)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.window, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            # Read image via OpenCV and store in Model
            self.model.original_image = cv2.imread(file_path)
            self.model.processed_image = None

            # Display the original image on the left label
            self.display_original_image(self.model.original_image)

            # Clear the right label since we just loaded a new image
            self.ui.lblProcessed.clear()
            self.ui.lblProcessed.setText("Ready for processing.")

            # Set image for snake controller (convert to grayscale)
            gray_img = cv2.cvtColor(self.model.original_image, cv2.COLOR_BGR2GRAY)
            self.greedy_snake_controller.set_image(gray_img, self.model.original_image)

            self.ui.statusbar.showMessage(f"Loaded: {file_path}", 3000)


    def display_original_image(self, cv_img):
        if cv_img is None:
            return

        pixmap = cv_to_pixmap(cv_img)
        if pixmap:
            # Scale the pixmap to fit the label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.ui.lblOriginal.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.lblOriginal.setPixmap(scaled_pixmap)

    def display_processed_image(self, cv_img):

        if cv_img is None:
            return

        pixmap = cv_to_pixmap(cv_img)
        if pixmap:
            # Scale the pixmap to fit the label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.ui.lblProcessed.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.lblProcessed.setPixmap(scaled_pixmap)