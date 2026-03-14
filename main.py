import sys


from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("GUI")
#         self.setGeometry(700,0,500,500)
#         # self.setWindowIcon(QIcon('icon.png'))
#         self.initUI()
#
#     def initUI(self):
#         self.label = QLabel(self)
#         self.label.setText("label")
#         self.label.move(50,50)
#
#         self.b1 = QPushButton("Button 1", self)
#         self.b1.clicked.connect(self.clicked)
#
#     def clicked(self):
#         self.label.setText("button pressed")
#         self.update()
#
#     def update(self):
#         self.label.adjustSize()

def main():
    app = QApplication()

    loader = QUiLoader()
    file = QFile("gui.ui")
    file.open(QFile.ReadOnly)

    window = loader.load(file)
    file.close()

    window.pushButton.clicked.connect(lambda:
                                      QMessageBox.information
                                      (window,'Message',window.lineEdit.text()))
    window.show()
    app.exec() #  waits for user inputs

if __name__ == '__main__':
    main()
