#coding='utf-8'

from PyQt4 import QtCore, QtGui
import time

class LoginHandler(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self,  parent=None):
        super(LoginHandler,  self).__init__(parent)
        pass

    def run(self):
        time.sleep(6)
        self.finishSignal.emit(['hello,','world','!'])


#http://www.jyguagua.com/?p=2560   [分享]PyQt UI与后台逻辑操作线程分离(PyQt登陆窗口设计为例讲解)
