import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from views.ui_main_window import Ui_MainWindow
from models.image_model import ImageModel
from controllers.main_controller import MainController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup for the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 1. Create the View
    window = MainWindow()

    # 2. Create the Model
    model = ImageModel()

    # 3. Create the Controller, passing the UI, Model, and Window
    controller = MainController(window.ui, model, window)

    window.show()
    sys.exit(app.exec())