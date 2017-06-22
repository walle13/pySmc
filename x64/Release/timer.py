#
# #coding=utf-8
#
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
#
# import threading
# from time import ctime,sleep
#
# def music(func):
#     for i in range(2):
#         print "I was listening to %s. %s" %(func,ctime())
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print "I was at the %s! %s" %(func,ctime())
#         sleep(5)
#
#
#
# if __name__ == '__main__':
#     music(u'爱情买卖')
#     move(u'阿凡达')
#
#     print "all over %s" %ctime()


# -*- coding: utf-8 -*-

from PyQt4.Qt import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time


class Backend(QThread):
    update_date = pyqtSignal(QString)
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            self.update_date.emit(QString(str(data)))
            time.sleep(1)


class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    b = Backend()
    w = Window()
    b.update_date.connect(w.handleDisplay)
    b.start()
    w.show()
    app.exec_()
