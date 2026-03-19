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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMaximumSize(QSize(340, 16777215))
        self.sidebarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnOpenImage = QPushButton(self.sidebarFrame)
        self.btnOpenImage.setObjectName(u"btnOpenImage")
        self.btnOpenImage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnOpenImage)

        self.tabWidget = QTabWidget(self.sidebarFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabTask1 = QWidget()
        self.tabTask1.setObjectName(u"tabTask1")
        self.verticalLayout_2 = QVBoxLayout(self.tabTask1)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBoxCanny = QGroupBox(self.tabTask1)
        self.groupBoxCanny.setObjectName(u"groupBoxCanny")
        self.formLayout = QFormLayout(self.groupBoxCanny)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
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
        self.spinCannyMax.setValue(200)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinCannyMax)


        self.verticalLayout_2.addWidget(self.groupBoxCanny)

        self.groupBoxHough = QGroupBox(self.tabTask1)
        self.groupBoxHough.setObjectName(u"groupBoxHough")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxHough)
        self.verticalLayout_3.setSpacing(10)
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
        self.btnApplyShapes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnApplyShapes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabTask1, "")
        self.tabTask2 = QWidget()
        self.tabTask2.setObjectName(u"tabTask2")
        self.verticalLayout_4 = QVBoxLayout(self.tabTask2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBoxSnakeParams = QGroupBox(self.tabTask2)
        self.groupBoxSnakeParams.setObjectName(u"groupBoxSnakeParams")
        self.formLayoutSnake = QFormLayout(self.groupBoxSnakeParams)
        self.formLayoutSnake.setObjectName(u"formLayoutSnake")
        self.labelAlpha = QLabel(self.groupBoxSnakeParams)
        self.labelAlpha.setObjectName(u"labelAlpha")

        self.formLayoutSnake.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelAlpha)

        self.sliderAlpha = QSlider(self.groupBoxSnakeParams)
        self.sliderAlpha.setObjectName(u"sliderAlpha")
        self.sliderAlpha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sliderAlpha.setMaximum(200)
        self.sliderAlpha.setValue(10)
        self.sliderAlpha.setOrientation(Qt.Orientation.Horizontal)

        self.formLayoutSnake.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sliderAlpha)

        self.labelBeta = QLabel(self.groupBoxSnakeParams)
        self.labelBeta.setObjectName(u"labelBeta")

        self.formLayoutSnake.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelBeta)

        self.sliderBeta = QSlider(self.groupBoxSnakeParams)
        self.sliderBeta.setObjectName(u"sliderBeta")
        self.sliderBeta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sliderBeta.setMaximum(200)
        self.sliderBeta.setValue(10)
        self.sliderBeta.setOrientation(Qt.Orientation.Horizontal)

        self.formLayoutSnake.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sliderBeta)

        self.labelGamma = QLabel(self.groupBoxSnakeParams)
        self.labelGamma.setObjectName(u"labelGamma")

        self.formLayoutSnake.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelGamma)

        self.sliderGamma = QSlider(self.groupBoxSnakeParams)
        self.sliderGamma.setObjectName(u"sliderGamma")
        self.sliderGamma.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sliderGamma.setMaximum(200)
        self.sliderGamma.setValue(100)
        self.sliderGamma.setOrientation(Qt.Orientation.Horizontal)

        self.formLayoutSnake.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sliderGamma)


        self.verticalLayout_4.addWidget(self.groupBoxSnakeParams)

        self.btnApplySnake = QPushButton(self.tabTask2)
        self.btnApplySnake.setObjectName(u"btnApplySnake")
        self.btnApplySnake.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnApplySnake)

        self.btnClearContour = QPushButton(self.tabTask2)
        self.btnClearContour.setObjectName(u"btnClearContour")
        self.btnClearContour.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnClearContour)

        self.btnCalcPerimeter = QPushButton(self.tabTask2)
        self.btnCalcPerimeter.setObjectName(u"btnCalcPerimeter")
        self.btnCalcPerimeter.setEnabled(False)
        self.btnCalcPerimeter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnCalcPerimeter)

        self.btnCalcArea = QPushButton(self.tabTask2)
        self.btnCalcArea.setObjectName(u"btnCalcArea")
        self.btnCalcArea.setEnabled(False)
        self.btnCalcArea.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnCalcArea)

        self.btnCalcChainCode = QPushButton(self.tabTask2)
        self.btnCalcChainCode.setObjectName(u"btnCalcChainCode")
        self.btnCalcChainCode.setEnabled(False)
        self.btnCalcChainCode.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnCalcChainCode)

        self.lblResult = QLabel(self.tabTask2)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setMinimumSize(QSize(0, 30))
        self.lblResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblResult)

        self.txtChainCodeResult = QTextEdit(self.tabTask2)
        self.txtChainCodeResult.setObjectName(u"txtChainCodeResult")
        self.txtChainCodeResult.setMinimumSize(QSize(0, 100))
        self.txtChainCodeResult.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.txtChainCodeResult)

        self.verticalSpacerSnake = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacerSnake)

        self.tabWidget.addTab(self.tabTask2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 713, 695))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblOriginal = QLabel(self.scrollAreaWidgetContents)
        self.lblOriginal.setObjectName(u"lblOriginal")
        self.lblOriginal.setMinimumSize(QSize(300, 300))
        self.lblOriginal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblOriginal)

        self.lblProcessed = QLabel(self.scrollAreaWidgetContents)
        self.lblProcessed.setObjectName(u"lblProcessed")
        self.lblProcessed.setMinimumSize(QSize(300, 300))
        self.lblProcessed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblProcessed)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CV Assignment - Shape & Contour Detector", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"    /* Global Styles */\n"
"    QMainWindow { background-color: #2b2b2b; color: #f0f0f0; }\n"
"    QWidget { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 10pt; }\n"
"    QLabel { color: #f0f0f0; }\n"
"\n"
"    /* Group Boxes */\n"
"    QGroupBox { font-weight: bold; border: 1px solid #555555; border-radius: 6px; margin-top: 15px; padding-top: 10px; }\n"
"    QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #4DA8DA; }\n"
"\n"
"    /* Standard Buttons */\n"
"    QPushButton { background-color: #4DA8DA; color: white; border-radius: 4px; padding: 8px; font-weight: bold; }\n"
"    QPushButton:hover { background-color: #3b8bb8; }\n"
"    QPushButton:pressed { background-color: #2a6a8c; }\n"
"    QPushButton:disabled { background-color: #444444; color: #777777; }\n"
"\n"
"    /* The NEW Giant Upload Button */\n"
"    #btnOpenImage {\n"
"    background-color: #2E8B57; /* SeaGreen Accent */\n"
"    border: 2px solid #3CB371;\n"
"    color: white;\n"
"    font-si"
                        "ze: 13pt;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"    border-radius: 8px;\n"
"    margin-bottom: 5px;\n"
"    }\n"
"    #btnOpenImage:hover { background-color: #3CB371; }\n"
"    #btnOpenImage:pressed { background-color: #228B22; border: 2px solid #228B22; }\n"
"\n"
"    /* Tabs */\n"
"    QTabWidget::pane { border: 1px solid #555555; border-radius: 4px; top: -1px; background-color: #333333; }\n"
"    QTabBar::tab { background: #222222; color: #aaaaaa; padding: 8px 16px; border: 1px solid #555555; border-bottom: none; border-top-left-radius: 4px; border-top-right-radius: 4px; margin-right: 2px; }\n"
"    QTabBar::tab:selected { background: #333333; color: #4DA8DA; font-weight: bold; }\n"
"    QTabBar::tab:hover:!selected { background: #2a2a2a; color: #ffffff; }\n"
"\n"
"    /* Inputs */\n"
"    QSpinBox, QSlider { background-color: #1e1e1e; color: white; border: 1px solid #555555; border-radius: 3px; padding: 3px; }\n"
"    QCheckBox { color: #f0f0f0; spacing: 8px; }\n"
"    QCheckBox::indicator "
                        "{ width: 16px; height: 16px; border-radius: 3px; border: 1px solid #555555; background: #1e1e1e; }\n"
"    QCheckBox::indicator:checked { background: #4DA8DA; }\n"
"\n"
"    /* Text Outputs */\n"
"    QTextEdit { background-color: #1e1e1e; color: #4DA8DA; border: 1px solid #555555; border-radius: 4px; padding: 4px; }\n"
"\n"
"    /* Scroll Area / Image Canvas */\n"
"    QScrollArea { background-color: #1e1e1e; border: 1px solid #111111; }\n"
"   ", None))
        self.btnOpenImage.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c1 Upload Image", None))
        self.groupBoxCanny.setTitle(QCoreApplication.translate("MainWindow", u"Canny Edge Detection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min Val:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Val:", None))
        self.groupBoxHough.setTitle(QCoreApplication.translate("MainWindow", u"Hough Transforms", None))
        self.checkLines.setText(QCoreApplication.translate("MainWindow", u"Detect Lines", None))
        self.checkCircles.setText(QCoreApplication.translate("MainWindow", u"Detect Circles", None))
        self.checkEllipses.setText(QCoreApplication.translate("MainWindow", u"Detect Ellipses", None))
        self.btnApplyShapes.setText(QCoreApplication.translate("MainWindow", u"Apply Shape Detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTask1), QCoreApplication.translate("MainWindow", u"Edge Detection", None))
        self.groupBoxSnakeParams.setTitle(QCoreApplication.translate("MainWindow", u"Snake Parameters", None))
        self.labelAlpha.setText(QCoreApplication.translate("MainWindow", u"Alpha:", None))
        self.labelBeta.setText(QCoreApplication.translate("MainWindow", u"Beta:", None))
        self.labelGamma.setText(QCoreApplication.translate("MainWindow", u"Gamma:", None))
        self.btnApplySnake.setText(QCoreApplication.translate("MainWindow", u"Apply Snake", None))
        self.btnClearContour.setText(QCoreApplication.translate("MainWindow", u"Clear Contour", None))
        self.btnCalcPerimeter.setText(QCoreApplication.translate("MainWindow", u"Calculate Perimeter", None))
        self.btnCalcArea.setText(QCoreApplication.translate("MainWindow", u"Calculate Area", None))
        self.btnCalcChainCode.setText(QCoreApplication.translate("MainWindow", u"Calculate Chain Code", None))
        self.lblResult.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #1e1e1e; border: 1px solid #555555; border-radius: 4px; font-weight: bold; color: #4DA8DA;", None))
        self.lblResult.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.txtChainCodeResult.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chain Code output will appear here...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTask2), QCoreApplication.translate("MainWindow", u"Active Contours", None))
        self.lblOriginal.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #1a1a1a; border: 2px dashed #444444; border-radius: 8px; color: #666666;", None))
        self.lblOriginal.setText(QCoreApplication.translate("MainWindow", u"Original Image", None))
        self.lblProcessed.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #1a1a1a; border: 2px dashed #444444; border-radius: 8px; color: #666666;", None))
        self.lblProcessed.setText(QCoreApplication.translate("MainWindow", u"Processed Image", None))
    # retranslateUi

