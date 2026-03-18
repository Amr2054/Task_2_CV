from PySide6.QtWidgets import QMainWindow
from core.canny_edge_detection import apply_canny
from controllers.hough_controller import HoughController


class Canny_EdgeDetector_Controller(QMainWindow):
    def __init__(self, ui, model, display_callback):
        self.ui = ui
        self.model = model
        self.display_callback = display_callback  # Function passed from MainController to update the canvas
        self.hough_controller = HoughController(ui, model, display_callback)
        self._connect_signals()

    def _connect_signals(self):
        # Connect the Apply button from the UI to the method in this class
        self.ui.btnApplyShapes.clicked.connect(self.run_shape_detection)

    def run_shape_detection(self):
        # 1. Validation
        if self.model.original_image is None:
            self.ui.statusbar.showMessage("Please load an image first!", 3000)
            return

        # 2. Get parameters from the View's spinboxes
        min_val = self.ui.spinCannyMin.value()
        max_val = self.ui.spinCannyMax.value()

        # 3. Run Core logic (Your custom Canny NumPy implementation)
        edges = apply_canny(self.model.original_image, min_val, max_val)

        self.model.processed_image = edges
        self.hough_controller.run_hough(edges)