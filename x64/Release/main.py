# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore,  QtGui
import time

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

    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.pushButton_login.setDisabled(True)
        #采用单线程操作
        #time.sleep(6)
        #print("hello, world")
        #self.pushButton_login.setDisabled(False)

        #采用多线程操作
        from LoginHandler import LoginHandler
        self.login_process = LoginHandler()
        #登陆完成的信号绑定到登陆结束的槽函数
        self.login_process.finishSignal.connect(self.LoginEnd)
        #启动线程
        self.login_process.start()
        pass

    @pyqtSlot(list)
    def LoginEnd(self, words):
        for i in words:
            print(i)
        self.pushButton_login.setDisabled(False)
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
