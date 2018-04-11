from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime as dt
import sys

class Ui_addBooking(QtWidgets.QWidget):
    def setupUi(self, addBooking):
        addBooking.setObjectName("addBooking")
        addBooking.resize(500, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addBooking.sizePolicy().hasHeightForWidth())
        addBooking.setSizePolicy(sizePolicy)
        addBooking.setMinimumSize(QtCore.QSize(500, 800))
        addBooking.setMaximumSize(QtCore.QSize(500, 800))
        self.label = QtWidgets.QLabel(addBooking)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Resources/Icons/empty.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addBooking)
        self.label_2.setGeometry(QtCore.QRect(70, 330, 171, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passenger_id = QtWidgets.QLineEdit(addBooking)
        self.passenger_id.setGeometry(QtCore.QRect(240, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.passenger_id.setFont(font)
        self.passenger_id.setObjectName("passenger_id")
        self.bool_singletrip = QtWidgets.QRadioButton(addBooking)
        self.bool_singletrip.setGeometry(QtCore.QRect(70, 390, 141, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.bool_singletrip.setFont(font)
        self.bool_singletrip.setCheckable(True)
        self.bool_singletrip.setChecked(False)
        self.bool_singletrip.setObjectName("bool_singletrip")
        self.bool_multicity = QtWidgets.QRadioButton(addBooking)
        self.bool_multicity.setGeometry(QtCore.QRect(230, 390, 131, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.bool_multicity.setFont(font)
        self.bool_multicity.setObjectName("bool_multicity")
        self.flight_code1 = QtWidgets.QLineEdit(addBooking)
        self.flight_code1.setGeometry(QtCore.QRect(211, 467, 191, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.flight_code1.setFont(font)
        self.flight_code1.setObjectName("flight_code1")
        self.date_departure1 = QtWidgets.QDateEdit(addBooking)
        self.date_departure1.setGeometry(QtCore.QRect(210, 520, 201, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.date_departure1.setFont(font)
        self.date_departure1.setObjectName("date_departure1")
        self.label_3 = QtWidgets.QLabel(addBooking)
        self.label_3.setGeometry(QtCore.QRect(101, 447, 91, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(addBooking)
        self.label_4.setGeometry(QtCore.QRect(70, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(addBooking)
        self.label_5.setGeometry(QtCore.QRect(101, 567, 91, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(addBooking)
        self.label_6.setGeometry(QtCore.QRect(70, 630, 121, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.flight_code2 = QtWidgets.QLineEdit(addBooking)
        self.flight_code2.setGeometry(QtCore.QRect(211, 587, 191, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.flight_code2.setFont(font)
        self.flight_code2.setObjectName("flight_code2")
        self.date_departure2 = QtWidgets.QDateEdit(addBooking)
        self.date_departure2.setGeometry(QtCore.QRect(210, 640, 201, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.date_departure2.setFont(font)
        self.date_departure2.setObjectName("date_departure2")
        self.btn_addBooking = QtWidgets.QPushButton(addBooking)
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

        self.retranslateUi(addBooking)
        self.bool_singletrip.clicked.connect(self.label_5.hide)
        self.bool_singletrip.clicked.connect(self.label_6.hide)
        self.bool_singletrip.clicked.connect(self.flight_code2.hide)
        self.bool_singletrip.clicked.connect(self.date_departure2.hide)
        self.bool_multicity.clicked.connect(self.label_5.show)
        self.bool_multicity.clicked.connect(self.flight_code2.show)
        self.bool_multicity.clicked.connect(self.date_departure2.show)
        self.bool_multicity.clicked.connect(self.label_6.show)
        QtCore.QMetaObject.connectSlotsByName(addBooking)

    def retranslateUi(self, addBooking):
        _translate = QtCore.QCoreApplication.translate
        addBooking.setWindowTitle(_translate("addBooking", "Add Booking"))
        self.label_2.setText(_translate("addBooking", "Add a flight for"))
        self.passenger_id.setPlaceholderText(_translate("addBooking", "passenger_id"))
        self.bool_singletrip.setText(_translate("addBooking", "Single trip"))
        self.bool_multicity.setText(_translate("addBooking", "Multi-city"))
        self.flight_code1.setPlaceholderText(_translate("addBooking", "flight_code"))
        self.date_departure1.setDisplayFormat(_translate("addBooking", "yyyy-MM-dd"))
        self.label_3.setText(_translate("addBooking", "Flight 1:"))
        self.label_4.setText(_translate("addBooking", "Departure 1:"))
        self.label_5.setText(_translate("addBooking", "Flight 2:"))
        self.label_6.setText(_translate("addBooking", "Departure 2:"))
        self.flight_code2.setPlaceholderText(_translate("addBooking", "flight_code"))
        self.date_departure2.setDisplayFormat(_translate("addBooking", "yyyy-MM-dd"))
        self.btn_addBooking.setText(_translate("addBooking", "Add booking"))

        self.btn_addBooking.clicked.connect(self.makeBooking)

    def makeBooking(self):

        if (self.bool_singletrip.isChecked()):
            pid = str(self.passenger_id.text())
            fc1 = str(self.flight_code1.text())
            de1 = str(self.date_departure1.date().toPyDate())

            try:
                cnxn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_isean;pwd=JrR4jH7m74FEmY4m')
                cursor = cnxn.cursor()
                test2 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 F.flight_code FROM Flight_Instance F WHERE F.flight_code = ?) AS b", fc1).fetchone()
                test2 = int(test2[0])

                test4 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 a.depart_date FROM Flight_Instance a WHERE a.depart_date = ?) AS C", de1).fetchone()
                test4 = int(test4[0])

                test6 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 P.passenger_id FROM Passenger P WHERE P.passenger_id = ?) AS b", pid).fetchone()
                test6 = int(test6[0])
                print (test6)


                if (not(test6)):
                    errMsg = "passenger_id does not exist"
                    self.showdialog(errMsg=errMsg)

                if(not(test2)):
                    errMsg = "Flight 1 does not exist"
                    self.showdialog(errMsg=errMsg)


                elif(not(test4)):
                    errMsg = "Flight 1 date does not exist"
                    self.showdialog(errMsg=errMsg)

                if (test6 and test2 and test4):
                    cursor.execute("INSERT INTO Booking(flight_code, depart_date, passenger_id) VALUES(?, ?, ?)", fc1, de1, pid)
                    rows = cursor.execute("SELECT * FROM Booking").fetchall()
                    for row in rows:
                        print (row.flight_code, row.depart_date, row.passenger_id)
                    # cnxn.commit()
                    print("FUCK YESSS")


            except:
                errMsg1 = "CSIL Cypress is probably down for the 124789123rd time"
                self.showdialog(errMsg=errMsg1)

        elif (self.bool_multicity.isChecked()):
            pid = str(self.passenger_id.text())
            fc1 = str(self.flight_code1.text())
            de1 = str(self.date_departure1.date().toPyDate())
            fc2 = str(self.flight_code2.text())
            de2 = str(self.date_departure2.date().toPyDate())

            a = dt.strptime(de1, "%Y-%m-%d")
            b = dt.strptime(de2, "%Y-%m-%d")


            if (a > b):
                errMsg1 = "Flight 1 departure date must not be later than Flight 2 departure date"
                print (errMsg1)
                self.showdialog(errMsg=errMsg1)
                test1 = 0

            test1 = 1

            try:
                cnxn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_isean;pwd=JrR4jH7m74FEmY4m')
                cursor = cnxn.cursor()
                test2 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 F.flight_code FROM Flight_Instance F WHERE F.flight_code = ?) AS b", fc1).fetchone()
                test2 = int(test2[0])

                test3 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 a.flight_code FROM Flight_Instance a WHERE a.flight_code = ?) AS C", fc2).fetchone()
                test3 = int(test3[0])

                test4 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 a.depart_date FROM Flight_Instance a WHERE a.depart_date = ?) AS C", de1).fetchone()
                test4 = int(test4[0])


                test5 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 a.depart_date FROM Flight_Instance a WHERE a.depart_date = ?) AS C", de2).fetchone()
                test5 = int(test5[0])

                test6 = cursor.execute("SELECT COUNT(*) FROM (SELECT TOP 1 P.passenger_id FROM Passenger P WHERE P.passenger_id = ?) AS b", pid).fetchone()
                test6 = int(test6[0])


                if (not(test6)):
                    errMsg = "passenger_id does not exist"
                    self.showdialog(errMsg=errMsg)

                if (not(test2 or test3)):
                    errMsg = "Both Flight 1 and Flight 2 do not exist"
                    self.showdialog(errMsg=errMsg)

                elif(not(test2)):
                    errMsg = "Flight 1 does not exist"
                    self.showdialog(errMsg=errMsg)

                elif(not(test3)):
                    errMsg = "Flight 2 does not exist"
                    self.showdialog(errMsg=errMsg)

                if (not(test4 or test5)):
                    errMsg = "Both Flight 1 and Flight 2 dates do not exist"
                    self.showdialog(errMsg=errMsg)

                elif(not(test4)):
                    errMsg = "Flight 1 date does not exist"
                    self.showdialog(errMsg=errMsg)

                elif(not(test5)):
                    errMsg = "Flight 2 date does not exist"
                    self.showdialog(errMsg=errMsg)

                print(test1)
                print(test2)
                print(test3)
                print(test4)
                print(test5)
                print(test6)

                if (test1 and test2 and test3 and test4 and test5 and test6):
                    params = [ (fc1, de1, pid), (fc2, de2, pid)]
                    cursor.executemany("INSERT INTO Booking(flight_code, depart_date, passenger_id) VALUES(?, ?, ?)", params)
                    # cursor.execute("INSERT INTO Booking(flight_code, depart_date, passenger_id) VALUES(?, ?, ?)", fc2, de2, pid)
                    # cnxn.commit()
                    rows = cursor.execute("SELECT * FROM Booking").fetchall()
                    for row in rows:
                        print (row.flight_code, row.depart_date, row.passenger_id)
                    print ("HELLO")

            except:
                errMsg1 = "CSIL Cypress is probably down for the 124789123rd time"
                self.showdialog(errMsg=errMsg1)

        else:
            errMsg1 = "Please choose flight type (single or multicity)"
            self.showdialog(errMsg=errMsg1)

    def showdialog(self, errMsg):
       msg = QtWidgets.QMessageBox()
       msg.setIcon(QtWidgets.QMessageBox.Warning)

       msg.setText(errMsg)
       msg.setWindowTitle("Good looking popup")
       msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
       msg.buttonClicked.connect(self.msgbtn)

       retval = msg.exec_()
       print ("value of pressed message box button:", retval)

    def msgbtn(self):
       print ("Button pressed is:")
