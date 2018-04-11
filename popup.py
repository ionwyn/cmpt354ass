import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def window():
   app = QtWidgets.QApplication(sys.argv)
   w = QtWidgets.QWidget()
   b = QtWidgets.QPushButton(w)
   b.setText("Show message!")

   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())

def showdialog():
   msg = QtWidgets.QMessageBox()
   msg.setIcon(QtWidgets.QMessageBox.Information)

   msg.setText("The profile for passenger was created")
   msg.setWindowTitle("Good looking popup")
   msg.setDetailedText("The details are as follows:\nasds")
   msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
   msg.buttonClicked.connect(msgbtn)

   retval = msg.exec_()
   print ("value of pressed message box button:", retval)

def msgbtn(i):
   print ("Button pressed is:",i.text())

if __name__ == '__main__':
   window()
