# -*- coding: utf-8 -*-
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from Ui_login import Ui_MainWindow
from main import MainWindow as mainww


import sys

import os.path


# sys.path.append("C:/cgteamwork/bin/base")
#
# import cgtw
#
# t_tw = cgtw.tw("192.168.199.95")

class MainWindow(QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent=None):
       
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.ui = mainww()

        if os.path.exists("./config/.powershell"):
            file = open('./config/.powershell', 'r')
            r = file.readline()
            data = r.split("=")
            self.lineEdit.setText(data[0])
            self.lineEdit_2.setText(data[1])
            file.close()


    @QtCore.Slot()
    def on_pushButton_clicked(self):
        self.account = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        if (self.account == "" or self.password == ""):
            print(QMessageBox.warning(self, "警告", "用户名和密码不可为空", QMessageBox.Yes, QMessageBox.Yes))
        else:
            self.hide()
            self.ui.show()
            # QMessageBox.information(self, "提示", "登录成功!", QMessageBox.Yes, QMessageBox.Yes)

        #     
        if self.checkBox.isChecked():
            file = open('./config/.powershell', 'w')
            file.write(self.account + "=" + self.password)
            file.close()
        # loginbool = t_tw.sys().login(self.account, self.password)
        # if loginbool:

        # else:
        #     print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
