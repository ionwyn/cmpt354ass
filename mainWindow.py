# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_Passenger = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Resources/Icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Passenger.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.actionAdd_Passenger.setFont(font)
        self.actionAdd_Passenger.setObjectName("actionAdd_Passenger")
        self.actionView_Passengers = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Resources/Icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Passengers.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.actionView_Passengers.setFont(font)
        self.actionView_Passengers.setObjectName("actionView_Passengers")
        self.actionAdd_Booking = QtWidgets.QAction(MainWindow)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wakanda Airline"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAdd_Passenger.setText(_translate("MainWindow", "Add Passenger"))
        self.actionAdd_Passenger.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionView_Passengers.setText(_translate("MainWindow", "View Passengers"))
        self.actionView_Passengers.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionAdd_Booking.setText(_translate("MainWindow", "Add Booking"))

import rscConfig_rc
