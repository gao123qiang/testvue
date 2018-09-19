# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\simple project\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAccessibleName("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/新前缀/images/6.jpg);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 300, 40))
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:4px;\n"
"background-image: url(:/新前缀/images/login_bgx.gif);\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 270, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/新前缀/images/login_bgx.gif);\n"
"border-radius:4px;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 150, 300, 40))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/新前缀/images/login_bgx.gif);\n"
"border-radius:4px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 220, 100, 20))
        self.checkBox.setMinimumSize(QtCore.QSize(100, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/新前缀/images/login_bgx.gif);")
        self.checkBox.setIconSize(QtCore.QSize(18, 18))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请您输入用户名"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请您输入密码"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))

import images1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

