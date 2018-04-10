# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPassenger.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addPassenger(object):
    def setupUi(self, addPassenger):
        addPassenger.setObjectName("addPassenger")
        addPassenger.resize(500, 500)
        addPassenger.setMinimumSize(QtCore.QSize(500, 500))
        addPassenger.setMaximumSize(QtCore.QSize(500, 500))
        addPassenger.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(addPassenger)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label.setMinimumSize(QtCore.QSize(500, 500))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Resources/Icons/empty.png"))
        self.label.setObjectName("label")
        self.submitPassenger = QtWidgets.QPushButton(addPassenger)
        self.submitPassenger.setGeometry(QtCore.QRect(160, 360, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.submitPassenger.setFont(font)
        self.submitPassenger.setObjectName("submitPassenger")
        self.first_name = QtWidgets.QLineEdit(addPassenger)
        self.first_name.setGeometry(QtCore.QRect(140, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.first_name.setFont(font)
        self.first_name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.first_name.setMaxLength(18)
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLineEdit(addPassenger)
        self.last_name.setGeometry(QtCore.QRect(140, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.last_name.setFont(font)
        self.last_name.setText("")
        self.last_name.setMaxLength(18)
        self.last_name.setObjectName("last_name")

        self.retranslateUi(addPassenger)
        QtCore.QMetaObject.connectSlotsByName(addPassenger)

    def retranslateUi(self, addPassenger):
        _translate = QtCore.QCoreApplication.translate
        addPassenger.setWindowTitle(_translate("addPassenger", "Add Passenger"))
        self.submitPassenger.setText(_translate("addPassenger", "Submit"))
        self.first_name.setPlaceholderText(_translate("addPassenger", "First name"))
        self.last_name.setPlaceholderText(_translate("addPassenger", "Last name"))

import rscConfig_rc
