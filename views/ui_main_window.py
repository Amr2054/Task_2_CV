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
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QTextEdit,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 685)
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
        self.groupBoxSnakeParams = QGroupBox(self.tabTask2)
        self.groupBoxSnakeParams.setObjectName(u"groupBoxSnakeParams")
        self.formLayoutSnake = QFormLayout(self.groupBoxSnakeParams)
        self.formLayoutSnake.setObjectName(u"formLayoutSnake")
        self.labelAlpha = QLabel(self.groupBoxSnakeParams)
        self.labelAlpha.setObjectName(u"labelAlpha")

        self.formLayoutSnake.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelAlpha)

        self.sliderAlpha = QSlider(self.groupBoxSnakeParams)
        self.sliderAlpha.setObjectName(u"sliderAlpha")
        self.sliderAlpha.setOrientation(Qt.Orientation.Horizontal)
        self.sliderAlpha.setMaximum(200)
        self.sliderAlpha.setValue(10)

        self.formLayoutSnake.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sliderAlpha)

        self.labelBeta = QLabel(self.groupBoxSnakeParams)
        self.labelBeta.setObjectName(u"labelBeta")

        self.formLayoutSnake.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelBeta)

        self.sliderBeta = QSlider(self.groupBoxSnakeParams)
        self.sliderBeta.setObjectName(u"sliderBeta")
        self.sliderBeta.setOrientation(Qt.Orientation.Horizontal)
        self.sliderBeta.setMaximum(200)
        self.sliderBeta.setValue(10)

        self.formLayoutSnake.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sliderBeta)

        self.labelGamma = QLabel(self.groupBoxSnakeParams)
        self.labelGamma.setObjectName(u"labelGamma")

        self.formLayoutSnake.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelGamma)

        self.sliderGamma = QSlider(self.groupBoxSnakeParams)
        self.sliderGamma.setObjectName(u"sliderGamma")
        self.sliderGamma.setOrientation(Qt.Orientation.Horizontal)
        self.sliderGamma.setMaximum(200)
        self.sliderGamma.setMinimum(0)
        self.sliderGamma.setValue(100)

        self.formLayoutSnake.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sliderGamma)


        self.verticalLayout_4.addWidget(self.groupBoxSnakeParams)

        self.btnApplySnake = QPushButton(self.tabTask2)
        self.btnApplySnake.setObjectName(u"btnApplySnake")

        self.verticalLayout_4.addWidget(self.btnApplySnake)

        self.btnClearContour = QPushButton(self.tabTask2)
        self.btnClearContour.setObjectName(u"btnClearContour")

        self.verticalLayout_4.addWidget(self.btnClearContour)


        self.btnCalcPerimeter = QPushButton(self.tabTask2)
        self.btnCalcPerimeter.setObjectName(u"btnCalcPerimeter")
        self.btnCalcPerimeter.setEnabled(False)
 
        self.verticalLayout_4.addWidget(self.btnCalcPerimeter)
 
        self.btnCalcArea = QPushButton(self.tabTask2)
        self.btnCalcArea.setObjectName(u"btnCalcArea")
        self.btnCalcArea.setEnabled(False)
 
        self.verticalLayout_4.addWidget(self.btnCalcArea)

        self.btnCalcChainCode = QPushButton(self.tabTask2)
        self.btnCalcChainCode.setObjectName(u"btnCalcChainCode")
        self.btnCalcChainCode.setEnabled(False)

        self.verticalLayout_4.addWidget(self.btnCalcChainCode)

        self.lblResult = QLabel(self.tabTask2)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResult.setStyleSheet(u"border: 1px solid gray; padding: 4px; border-radius: 4px;")
        self.lblResult.setText(u"")

        self.verticalLayout_4.addWidget(self.lblResult)

        self.txtChainCodeResult = QTextEdit(self.tabTask2)
        self.txtChainCodeResult.setObjectName(u"txtChainCodeResult")
        self.txtChainCodeResult.setReadOnly(True)
        self.txtChainCodeResult.setMinimumHeight(130)
        self.txtChainCodeResult.setStyleSheet(u"border: 1px solid gray; padding: 4px; border-radius: 4px;")

        self.verticalLayout_4.addWidget(self.txtChainCodeResult)



        self.verticalSpacerSnake = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacerSnake)

        self.tabWidget.addTab(self.tabTask2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 604, 619))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblOriginal = QLabel(self.scrollAreaWidgetContents)
        self.lblOriginal.setObjectName(u"lblOriginal")
        self.lblOriginal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblOriginal)

        self.lblProcessed = QLabel(self.scrollAreaWidgetContents)
        self.lblProcessed.setObjectName(u"lblProcessed")
        self.lblProcessed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblProcessed)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 23))
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
        self.groupBoxSnakeParams.setTitle(QCoreApplication.translate("MainWindow", u"Snake Parameters", None))
        self.labelAlpha.setText(QCoreApplication.translate("MainWindow", u"Alpha:", None))
        self.labelBeta.setText(QCoreApplication.translate("MainWindow", u"Beta:", None))
        self.labelGamma.setText(QCoreApplication.translate("MainWindow", u"Gamma:", None))
        self.btnApplySnake.setText(QCoreApplication.translate("MainWindow", u"Apply Snake", None))
        self.btnClearContour.setText(QCoreApplication.translate("MainWindow", u"Clear Contour", None))

        self.btnCalcPerimeter.setText(QCoreApplication.translate("MainWindow", u"Calculate Perimeter", None))
        self.btnCalcArea.setText(QCoreApplication.translate("MainWindow", u"Calculate Area", None))
        self.btnCalcChainCode.setText(QCoreApplication.translate("MainWindow", u"Calculate Chain Code", None))
        self.txtChainCodeResult.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chain Code output will appear here...", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTask2), QCoreApplication.translate("MainWindow", u"Active Contours", None))
        self.lblOriginal.setText(QCoreApplication.translate("MainWindow", u"Original Image", None))
        self.lblProcessed.setText(QCoreApplication.translate("MainWindow", u"Processed Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

