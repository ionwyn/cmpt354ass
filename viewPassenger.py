from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import sys

class Ui_viewPassenger(QtWidgets.QWidget):
    def setupUi(self, viewPassenger):
        viewPassenger.setObjectName("viewPassenger")
        viewPassenger.resize(1250, 750)
        viewPassenger.setMinimumSize(QtCore.QSize(1250, 750))
        viewPassenger.setMaximumSize(QtCore.QSize(1250, 750))
        self.table_Passenger = QtWidgets.QTableWidget(viewPassenger)
        self.table_Passenger.setGeometry(QtCore.QRect(0, 0, 561, 751))
        self.table_Passenger.setRowCount(100)
        self.table_Passenger.setColumnCount(4)
        self.table_Passenger.setObjectName("table_Passenger")
        item = QtWidgets.QTableWidgetItem()
        self.table_Passenger.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Passenger.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Passenger.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Passenger.setItem(0, 3, item)
        self.label = QtWidgets.QLabel(viewPassenger)
        self.label.setGeometry(QtCore.QRect(560, 0, 691, 751))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Resources/Icons/empty.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(viewPassenger)
        self.lineEdit.setGeometry(QtCore.QRect(670, 370, 161, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(viewPassenger)
        self.dateEdit.setGeometry(QtCore.QRect(880, 370, 251, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 11, 17), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(viewPassenger)
        self.label_2.setGeometry(QtCore.QRect(670, 320, 391, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.submitSearch = QtWidgets.QPushButton(viewPassenger)
        self.submitSearch.setGeometry(QtCore.QRect(670, 450, 461, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.submitSearch.setFont(font)
        self.submitSearch.setObjectName("submitSearch")

        self.retranslateUi(viewPassenger)
        QtCore.QMetaObject.connectSlotsByName(viewPassenger)

    def retranslateUi(self, viewPassenger):
        _translate = QtCore.QCoreApplication.translate
        viewPassenger.setWindowTitle(_translate("viewPassenger", "View Passenger"))
        __sortingEnabled = self.table_Passenger.isSortingEnabled()
        self.table_Passenger.setSortingEnabled(False)
        item = self.table_Passenger.item(0, 0)
        item.setText(_translate("viewPassenger", "passenger_id"))
        item = self.table_Passenger.item(0, 1)
        item.setText(_translate("viewPassenger", "first_name"))
        item = self.table_Passenger.item(0, 2)
        item.setText(_translate("viewPassenger", "last_name"))
        item = self.table_Passenger.item(0, 3)
        item.setText(_translate("viewPassenger", "miles"))
        self.table_Passenger.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setPlaceholderText(_translate("viewPassenger", "flight_code"))
        self.dateEdit.setDisplayFormat(_translate("viewPassenger", "MM-dd-yyyy"))
        self.label_2.setText(_translate("viewPassenger", "Search for a flight instance:"))
        self.submitSearch.setText(_translate("viewPassenger", "Search"))

        self.submitSearch.clicked.connect(self.showdialog)

    def showdialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        try:
            cnxn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_isean;pwd=JrR4jH7m74FEmY4m')
            cursor = cnxn.cursor()
            dateTemp = self.dateEdit.date()
            sqlDate = str(dateTemp.toPyDate())
            flightCode = str(self.lineEdit.text())
            sqlStuff = """
            SELECT DISTINCT P.passenger_id, P.first_name, P.last_name, P.miles
            FROM Passenger P, Booking B, Flight_Instance F WHERE B.passenger_id = P.passenger_id and B.flight_code = ? and B.depart_date = ?
            """

            rows = cursor.execute(sqlStuff, flightCode, sqlDate).fetchall()

            sqlStuff = """
            SELECT COUNT(*) FROM (
            SELECT DISTINCT P.passenger_id, P.first_name, P.last_name, P.miles
            FROM Passenger P, Booking B, Flight_Instance F WHERE B.passenger_id = P.passenger_id and B.flight_code = ? and B.depart_date = ?)
            AS haha
            """
            count = cursor.execute(sqlStuff, flightCode, sqlDate).fetchone()
            count = int(count[0])
            for i in range(1, count + 1):
               for j in range(4):
                   self.table_Passenger.setItem(i, j, QtWidgets.QTableWidgetItem(str(rows[i-1][j])))
        except:
           message="Something went wrong... Cypress is probably down again..."
           print (message)

        sqlC = """
        SELECT available_seats from Flight_Instance
        WHERE flight_code = ? AND depart_date = ?
        """
        seats = cursor.execute(sqlC, flightCode, sqlDate).fetchone()
        seatCount = int(seats[0])
        msg.setText("There are " + str(seatCount) + " seat(s) left for flight " + str(flightCode) + " on " + str(sqlDate))
        msg.setWindowTitle("I hope you like the UI")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)

        retval = msg.exec_()
        print ("value of pressed message box button:", retval)

    def msgbtn(i):
       print ("Button pressed is:")
