from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import pyodbc

class Ui_addPassenger(QtWidgets.QWidget):
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
        # conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_isean;pwd=JrR4jH7m74FEmY4m')
        # cur = conn.cursor()
        self.submitPassenger.clicked.connect(self.showdialog)

    def showdialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        try:
            cnxn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_isean;pwd=JrR4jH7m74FEmY4m')
            cursor = cnxn.cursor()
            firstName = self.first_name.text()
            lastName = self.last_name.text()
            last_id = cursor.execute("SELECT MAX(passenger_id) FROM Passenger").fetchone()
            print ("Last ID was " + str(last_id[0]))
            curId = int(last_id[0]) + 1
            sql = """
            INSERT INTO Passenger(passenger_id, first_name, last_name, miles)
            VALUES(?, ?, ?, 0)
            """
            cursor.execute(sql, curId, str(firstName), str(lastName))
            lone = cursor.execute("SELECT * FROM Passenger")
            for lo in lone:
                print (lo.passenger_id, lo.first_name, lo.last_name, lo.miles)
            # cnxn.commit()
            message="The profile for passenger "+ firstName + " "+ lastName +" was created"

        except:
            message="The profile for passenger "+ firstName + " "+ lastName + " failed to be created"
        msg.setText(message)
        msg.setWindowTitle("Good looking popup")
        msg.setDetailedText("If it didn't work:\n- Cypress might be down again for the 71984234th time")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)

        retval = msg.exec_()
        print ("value of pressed message box button:", retval)

    def msgbtn(i):
        print ("Button pressed is:")
