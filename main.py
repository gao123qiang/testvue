# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
# from PySide2 import pyside2Slot
from PySide2.QtCore import Qt, QPoint, QModelIndex
from PySide2.QtWidgets import QMainWindow, QMenu, QApplication, QAction
from PySide2 import QtGui, QtCore
# from qtpy import QtGui
# from qtpy import QtCore

from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.tableView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableView.addAction(QAction('test', self))
    
    # @pyqtSlot(QPoint)
    # def on_tableView_customContextMenuRequested(self, pos):
    #     """
    #     Slot documentation goes here.
    #
    #     @param pos DESCRIPTION
    #     @type QPoint
    #     """
    #     self.treeview.setContextMenuPolicy(Qt.CustomContextMenu)
    #     self.treeview.customContextMenuRequested.connect(self.showRightMenu)
    #     self.rightMenu = QMenu(self.treeview)
    #     self.rightMenu.addAction(self.upLoadAct)
    #     self.rightMenu.addAction(self.importAct)
    #     self.rightMenu.addAction(self.refreshAct)
    #     self.rightMenu.addAction(self.newFolderAct)
    #     self.rightMenu.addSeparator()
    #     # self.rightMenu.addAction(self.RenameAct)
    #     self.rightMenu.addAction(self.propertyAct)
    #     self.rightMenu.addAction(self.openfileAct)
    #     self.rightMenu.addAction(self.removeAct)
    #     self.rightMenu.addAction(self.OtherPlayAct)
    #     self.rightMenu.addAction(self.rebuildAct)
    
    # @pyqtSlot(QModelIndex)
    # def on_tableView_clicked(self, index):
    #     """
    #     Slot documentation goes here.
    #
    #     @param index DESCRIPTION
    #     @type QModelIndex
    #     """
    #     popMenu = QtGui.QMenu()
    #
    #     popMenu.addAction(QtGui.QAction(' 添加', self))
    #     popMenu.addAction(QtGui.QAction(' 删除', self) )
    #     popMenu.addAction(QtGui.QAction(' 修改', self))
    #     popMenu.exec_(QtGui.QCursor.pos())
        
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
    
