# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addBooking.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 800))
        Form.setMaximumSize(QtCore.QSize(500, 800))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Resources/Icons/empty.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 330, 171, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passenger_id = QtWidgets.QLineEdit(Form)
        self.passenger_id.setGeometry(QtCore.QRect(240, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.passenger_id.setFont(font)
        self.passenger_id.setObjectName("passenger_id")
        self.bool_singletrip = QtWidgets.QRadioButton(Form)
        self.bool_singletrip.setGeometry(QtCore.QRect(70, 390, 141, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.bool_singletrip.setFont(font)
        self.bool_singletrip.setCheckable(True)
        self.bool_singletrip.setChecked(False)
        self.bool_singletrip.setObjectName("bool_singletrip")
        self.bool_multicity = QtWidgets.QRadioButton(Form)
        self.bool_multicity.setGeometry(QtCore.QRect(230, 390, 131, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.bool_multicity.setFont(font)
        self.bool_multicity.setObjectName("bool_multicity")
        self.flight_code1 = QtWidgets.QLineEdit(Form)
        self.flight_code1.setGeometry(QtCore.QRect(211, 467, 191, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.flight_code1.setFont(font)
        self.flight_code1.setObjectName("flight_code1")
        self.date_departure1 = QtWidgets.QDateEdit(Form)
        self.date_departure1.setGeometry(QtCore.QRect(210, 520, 201, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.date_departure1.setFont(font)
        self.date_departure1.setObjectName("date_departure1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(101, 447, 91, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(101, 567, 91, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 630, 121, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.flight_code2 = QtWidgets.QLineEdit(Form)
        self.flight_code2.setGeometry(QtCore.QRect(211, 587, 191, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.flight_code2.setFont(font)
        self.flight_code2.setObjectName("flight_code2")
        self.date_departure2 = QtWidgets.QDateEdit(Form)
        self.date_departure2.setGeometry(QtCore.QRect(210, 640, 201, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.date_departure2.setFont(font)
        self.date_departure2.setObjectName("date_departure2")
        self.btn_addBooking = QtWidgets.QPushButton(Form)
        self.btn_addBooking.setGeometry(QtCore.QRect(140, 710, 191, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.btn_addBooking.setFont(font)
        self.btn_addBooking.setObjectName("btn_addBooking")
        self.label_2.setBuddy(self.passenger_id)
        self.label_3.setBuddy(self.flight_code1)
        self.label_4.setBuddy(self.date_departure1)
        self.label_5.setBuddy(self.flight_code1)
        self.label_6.setBuddy(self.date_departure1)

        self.retranslateUi(Form)
        self.bool_singletrip.clicked.connect(self.label_5.hide)
        self.bool_singletrip.clicked.connect(self.label_6.hide)
        self.bool_singletrip.clicked.connect(self.flight_code2.hide)
        self.bool_singletrip.clicked.connect(self.date_departure2.hide)
        self.bool_multicity.clicked.connect(self.label_5.show)
        self.bool_multicity.clicked.connect(self.flight_code2.show)
        self.bool_multicity.clicked.connect(self.date_departure2.show)
        self.bool_multicity.clicked.connect(self.label_6.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Add a flight for"))
        self.passenger_id.setPlaceholderText(_translate("Form", "passenger_id"))
        self.bool_singletrip.setText(_translate("Form", "Single trip"))
        self.bool_multicity.setText(_translate("Form", "Multi-city"))
        self.flight_code1.setPlaceholderText(_translate("Form", "flight_code"))
        self.date_departure1.setDisplayFormat(_translate("Form", "MM-dd-yyyy"))
        self.label_3.setText(_translate("Form", "Flight 1:"))
        self.label_4.setText(_translate("Form", "Departure 1:"))
        self.label_5.setText(_translate("Form", "Flight 2:"))
        self.label_6.setText(_translate("Form", "Departure 2:"))
        self.flight_code2.setPlaceholderText(_translate("Form", "flight_code"))
        self.date_departure2.setDisplayFormat(_translate("Form", "MM-dd-yyyy"))
        self.btn_addBooking.setText(_translate("Form", "Add booking"))

import rscConfig_rc
