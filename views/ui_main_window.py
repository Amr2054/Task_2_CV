# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 685)
        self.actionOpen_Image = QAction(MainWindow)
        self.actionOpen_Image.setObjectName(u"actionOpen_Image")
        self.actionSave_Result = QAction(MainWindow)
        self.actionSave_Result.setObjectName(u"actionSave_Result")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMaximumSize(QSize(320, 16777215))
        self.sidebarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.sidebarFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabTask1 = QWidget()
        self.tabTask1.setObjectName(u"tabTask1")
        self.verticalLayout_2 = QVBoxLayout(self.tabTask1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBoxCanny = QGroupBox(self.tabTask1)
        self.groupBoxCanny.setObjectName(u"groupBoxCanny")
        self.formLayout = QFormLayout(self.groupBoxCanny)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBoxCanny)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.spinCannyMin = QSpinBox(self.groupBoxCanny)
        self.spinCannyMin.setObjectName(u"spinCannyMin")
        self.spinCannyMin.setMaximum(255)
        self.spinCannyMin.setValue(100)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinCannyMin)

        self.label_2 = QLabel(self.groupBoxCanny)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.spinCannyMax = QSpinBox(self.groupBoxCanny)
        self.spinCannyMax.setObjectName(u"spinCannyMax")
        self.spinCannyMax.setMaximum(255)
        self.spinCannyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinCannyMax.setValue(200)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinCannyMax)


        self.verticalLayout_2.addWidget(self.groupBoxCanny)

        self.groupBoxHough = QGroupBox(self.tabTask1)
        self.groupBoxHough.setObjectName(u"groupBoxHough")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxHough)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkLines = QCheckBox(self.groupBoxHough)
        self.checkLines.setObjectName(u"checkLines")

        self.verticalLayout_3.addWidget(self.checkLines)

        self.checkCircles = QCheckBox(self.groupBoxHough)
        self.checkCircles.setObjectName(u"checkCircles")

        self.verticalLayout_3.addWidget(self.checkCircles)

        self.checkEllipses = QCheckBox(self.groupBoxHough)
        self.checkEllipses.setObjectName(u"checkEllipses")

        self.verticalLayout_3.addWidget(self.checkEllipses)


        self.verticalLayout_2.addWidget(self.groupBoxHough)

        self.btnApplyShapes = QPushButton(self.tabTask1)
        self.btnApplyShapes.setObjectName(u"btnApplyShapes")

        self.verticalLayout_2.addWidget(self.btnApplyShapes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabTask1, "")
        self.tabTask2 = QWidget()
        self.tabTask2.setObjectName(u"tabTask2")
        self.verticalLayout_4 = QVBoxLayout(self.tabTask2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget.addTab(self.tabTask2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 649, 619))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.imageCanvas = QLabel(self.scrollAreaWidgetContents)
        self.imageCanvas.setObjectName(u"imageCanvas")
        self.imageCanvas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.imageCanvas)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 995, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Image)
        self.menuFile.addAction(self.actionSave_Result)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CV Assignment - Shape & Contour Detector", None))
        self.actionOpen_Image.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Image.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Result.setText(QCoreApplication.translate("MainWindow", u"Save Result", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Result.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBoxCanny.setTitle(QCoreApplication.translate("MainWindow", u"Canny Edge Detection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min Val:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Val:", None))
        self.groupBoxHough.setTitle(QCoreApplication.translate("MainWindow", u"Hough Transforms", None))
        self.checkLines.setText(QCoreApplication.translate("MainWindow", u"Detect Lines", None))
        self.checkCircles.setText(QCoreApplication.translate("MainWindow", u"Detect Circles", None))
        self.checkEllipses.setText(QCoreApplication.translate("MainWindow", u"Detect Ellipses", None))
        self.btnApplyShapes.setText(QCoreApplication.translate("MainWindow", u"Apply Shape Detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTask1), QCoreApplication.translate("MainWindow", u"Edge Detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTask2), QCoreApplication.translate("MainWindow", u"Active Contours", None))
        self.imageCanvas.setText(QCoreApplication.translate("MainWindow", u"Please load an image from the File menu.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

