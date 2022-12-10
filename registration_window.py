# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets

con = mc.connect(host='Localhost',user='root',passwd='cadburychocolate123',db='2playergames')
class registration_window1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1391, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../pictures/login bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(930, 230, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 205, 141, 81))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(930, 290, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(835, 265, 141, 81))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(930, 350, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(755, 335, 181, 61))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # TEXT FOR INVALID USERNAME
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText('Username already exists')
        self.label_5.move(1150, 235)
        self.label_5.setStyleSheet("color: red")
        self.label_5.setHidden(True)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText('Username must be atleast 7 characters')
        self.label_7.move(1150, 235)
        self.label_7.setStyleSheet("color: red")
        self.label_7.setHidden(True)

        # TEXT FOR WRONG RE-ENTER
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText('Passwords do not match')
        self.label_6.move(1150, 360)
        self.label_6.setStyleSheet("color: red")
        self.label_6.setHidden(True)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText('Password must be atleast 7 characters')
        self.label_8.move(1150, 300)
        self.label_8.setStyleSheet("color: red")
        self.label_8.setHidden(True)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText('Successfully registered!')
        self.label_9.move(1100, 485)
        self.label_9.setStyleSheet("color: green")
        self.label_9.setHidden(True)

        # CONNECTING USER_AND_PASS METHOD TO LOGIN BUTTON
        self.pushButton.clicked.connect(self.user_and_pass)

    # METHOD TO VERIFY AND STORE USERNAME AND PASSWORD
    def user_and_pass(self):
        un = self.lineEdit.text()
        pw1 = self.lineEdit_2.text()
        pw2 = self.lineEdit_3.text()
        if len(un) <= 6:
            self.label_7.setHidden(False)
            self.label_5.setHidden(True)
            self.label_6.setHidden(True)
            self.label_8.setHidden(True)
            self.label_9.setHidden(True)
        elif len(pw1) <=6:
            self.label_8.setHidden(False)
            self.label_5.setHidden(True)
            self.label_6.setHidden(True)
            self.label_7.setHidden(True)
            self.label_9.setHidden(True)
        else:
            cr = con.cursor()
            a = cr.execute('select * from bank')
            a = cr.fetchall()
            count = 0
            for x in a:
                if un == x[0]:
                    count += 1
            if count == 0:
                if pw1 == pw2:
                    cr = con.cursor()
                    cr.execute('insert into bank values((%s),1000,0,(%s))',(un,pw1))
                    con.commit()
                    self.label_9.setHidden(False)
                else:
                    self.label_5.setHidden(True)
                    self.label_6.setHidden(False)
                    self.label_7.setHidden(True)
                    self.label_8.setHidden(True)
                    self.label_9.setHidden(True)

            else:
                self.label_5.setHidden(False)
                self.label_6.setHidden(True)
                self.label_7.setHidden(True)
                self.label_8.setHidden(True)
                self.label_9.setHidden(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Re-Enter Password</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = registration_window1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())