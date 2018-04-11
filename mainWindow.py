# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from addPassenger import *
from viewPassenger import *
from addBooking import *

class Second(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

class Ui_mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(800, 800))
        mainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Resources/Icons/Untitled design.png"))
        self.label.setScaledContents(True)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_Passenger = QtWidgets.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Resources/Icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Passenger.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.actionAdd_Passenger.setFont(font)
        self.actionAdd_Passenger.setObjectName("actionAdd_Passenger")

        # self.actionAdd_Passenger.triggered.connect(self.on_pushButton_clicked)

        self.actionView_Passengers = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Resources/Icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Passengers.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.actionView_Passengers.setFont(font)
        self.actionView_Passengers.setObjectName("actionView_Passengers")
        self.actionAdd_Booking = QtWidgets.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Resources/Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Booking.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.actionAdd_Booking.setFont(font)
        self.actionAdd_Booking.setObjectName("actionAdd_Booking")
        self.toolBar.addAction(self.actionAdd_Passenger)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionView_Passengers)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Booking)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Wakanda Airline"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.actionAdd_Passenger.setText(_translate("mainWindow", "Add Passenger"))
        self.actionAdd_Passenger.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.actionView_Passengers.setText(_translate("mainWindow", "View Passengers"))
        self.actionView_Passengers.setShortcut(_translate("mainWindow", "Ctrl+P"))
        self.actionAdd_Booking.setText(_translate("mainWindow", "Add Booking"))

        self.actionAdd_Passenger.triggered.connect(self.openAddPassenger)
        self.actionView_Passengers.triggered.connect(self.openViewPassenger)
        self.actionAdd_Booking.triggered.connect(self.openAddBooking)

    def openAddPassenger(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_addPassenger()
        self.ui.setupUi(self.window)
        self.window.show()

    def openViewPassenger(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_viewPassenger()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddBooking(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_addBooking()
        self.ui.setupUi(self.window)
        self.window.show()
