# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smc_py.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

from PyQt4.Qt import *

from PyQt4.QtCore import *
import time

#UI相关
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MicroValve(object):
    def setupUi(self, MicroValve):
        MicroValve.setObjectName(_fromUtf8("MicroValve"))
        MicroValve.resize(600, 456)
        self.pushButton_connect = QtGui.QPushButton(MicroValve)
        self.pushButton_connect.setGeometry(QtCore.QRect(220, 350, 81, 71))
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.pushButton_microValve = QtGui.QPushButton(MicroValve)
        self.pushButton_microValve.setGeometry(QtCore.QRect(40, 350, 81, 71))
        self.pushButton_microValve.setObjectName(_fromUtf8("pushButton_microValve"))
        self.pushButton_yHome = QtGui.QPushButton(MicroValve)
        self.pushButton_yHome.setGeometry(QtCore.QRect(310, 160, 81, 41))
        self.pushButton_yHome.setObjectName(_fromUtf8("pushButton_yHome"))
        self.pushButton_xPul2 = QtGui.QPushButton(MicroValve)
        self.pushButton_xPul2.setGeometry(QtCore.QRect(40, 190, 81, 71))
        self.pushButton_xPul2.setObjectName(_fromUtf8("pushButton_xPul2"))
        self.pushButton_stop = QtGui.QPushButton(MicroValve)
        self.pushButton_stop.setGeometry(QtCore.QRect(310, 350, 81, 71))
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.pushButton_16 = QtGui.QPushButton(MicroValve)
        self.pushButton_16.setGeometry(QtCore.QRect(130, 350, 81, 71))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_xPul1 = QtGui.QPushButton(MicroValve)
        self.pushButton_xPul1.setGeometry(QtCore.QRect(40, 110, 81, 71))
        self.pushButton_xPul1.setObjectName(_fromUtf8("pushButton_xPul1"))
        self.pushButton_yPul1 = QtGui.QPushButton(MicroValve)
        self.pushButton_yPul1.setGeometry(QtCore.QRect(130, 110, 81, 71))
        self.pushButton_yPul1.setObjectName(_fromUtf8("pushButton_yPul1"))
        self.pushButton_zPul1 = QtGui.QPushButton(MicroValve)
        self.pushButton_zPul1.setGeometry(QtCore.QRect(220, 110, 81, 71))
        self.pushButton_zPul1.setObjectName(_fromUtf8("pushButton_zPul1"))
        self.pushButton_out4 = QtGui.QPushButton(MicroValve)
        self.pushButton_out4.setGeometry(QtCore.QRect(310, 270, 81, 71))
        self.pushButton_out4.setObjectName(_fromUtf8("pushButton_out4"))
        self.pushButton_xHome = QtGui.QPushButton(MicroValve)
        self.pushButton_xHome.setGeometry(QtCore.QRect(310, 110, 81, 41))
        self.pushButton_xHome.setObjectName(_fromUtf8("pushButton_xHome"))
        self.pushButton_yPul2 = QtGui.QPushButton(MicroValve)
        self.pushButton_yPul2.setGeometry(QtCore.QRect(130, 190, 81, 71))
        self.pushButton_yPul2.setObjectName(_fromUtf8("pushButton_yPul2"))
        self.listView = QtGui.QListView(MicroValve)
        self.listView.setGeometry(QtCore.QRect(40, 30, 351, 71))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_out1 = QtGui.QPushButton(MicroValve)
        self.pushButton_out1.setGeometry(QtCore.QRect(40, 270, 81, 71))
        self.pushButton_out1.setObjectName(_fromUtf8("pushButton_out1"))
        self.pushButton_out2 = QtGui.QPushButton(MicroValve)
        self.pushButton_out2.setGeometry(QtCore.QRect(130, 270, 81, 71))
        self.pushButton_out2.setObjectName(_fromUtf8("pushButton_out2"))
        self.pushButton_out3 = QtGui.QPushButton(MicroValve)
        self.pushButton_out3.setGeometry(QtCore.QRect(220, 270, 81, 71))
        self.pushButton_out3.setObjectName(_fromUtf8("pushButton_out3"))
        self.pushButton_zHome = QtGui.QPushButton(MicroValve)
        self.pushButton_zHome.setGeometry(QtCore.QRect(310, 220, 81, 41))
        self.pushButton_zHome.setObjectName(_fromUtf8("pushButton_zHome"))
        self.pushButton_zPul2 = QtGui.QPushButton(MicroValve)
        self.pushButton_zPul2.setGeometry(QtCore.QRect(220, 190, 81, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(9)
        self.pushButton_zPul2.setFont(font)
        self.pushButton_zPul2.setObjectName(_fromUtf8("pushButton_zPul2"))
        self.label = QtGui.QLabel(MicroValve)
        self.label.setGeometry(QtCore.QRect(420, 282, 280, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(MicroValve)
        self.textBrowser.setGeometry(QtCore.QRect(410, 30, 121, 231))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_Y = QtGui.QLabel(MicroValve)
        self.label_Y.setGeometry(QtCore.QRect(420, 310, 81, 20))
        self.label_Y.setObjectName(_fromUtf8("label_Y"))
        self.label_Z = QtGui.QLabel(MicroValve)
        self.label_Z.setGeometry(QtCore.QRect(420, 340, 81, 20))
        self.label_Z.setObjectName(_fromUtf8("label_Z"))

        self.retranslateUi(MicroValve)
        self.displayUi(MicroValve)
        QtCore.QObject.connect(MicroValve, QtCore.SIGNAL(_fromUtf8("accepted()")), self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MicroValve)
        # self.input = setText(self)

    def retranslateUi(self, MicroValve):
        MicroValve.setWindowTitle(_translate("MicroValve", "Dialog", None))
        self.pushButton_connect.setText(_translate("MicroValve", "connect", None))
        self.pushButton_microValve.setText(_translate("MicroValve", "Micro Valve", None))
        self.pushButton_yHome.setText(_translate("MicroValve", "Y home", None))
        self.pushButton_xPul2.setText(_translate("MicroValve", "X-", None))
        self.pushButton_stop.setText(_translate("MicroValve", "stop", None))
        self.pushButton_16.setText(_translate("MicroValve", ".", None))
        self.pushButton_xPul1.setText(_translate("MicroValve", "X+", None))
        self.pushButton_yPul1.setText(_translate("MicroValve", "Y+", None))
        self.pushButton_zPul1.setText(_translate("MicroValve", "Z+", None))
        self.pushButton_out4.setText(_translate("MicroValve", "OUT4", None))
        self.pushButton_xHome.setText(_translate("MicroValve", "X home", None))
        self.pushButton_yPul2.setText(_translate("MicroValve", "Y-", None))
        self.pushButton_out1.setText(_translate("MicroValve", "OUT1", None))
        self.pushButton_out2.setText(_translate("MicroValve", "OUT2", None))
        self.pushButton_out3.setText(_translate("MicroValve", "OUT3", None))
        self.pushButton_zHome.setText(_translate("MicroValve", "Z home", None))
        self.pushButton_zPul2.setText(_translate("MicroValve", "Z-", None))
        self.label.setText(_translate("MicroValve", "Textlabel_X", None))
        self.label_Y.setText(_translate("MicroValve", "Textlabel_Y", None))
        self.label_Z.setText(_translate("MicroValve", "Textlabel_Z", None))

        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL("clicked()"), self.connect),
        QtCore.QObject.connect(self.pushButton_xPul1, QtCore.SIGNAL("clicked()"), self.xPul1),
        QtCore.QObject.connect(self.pushButton_xPul2, QtCore.SIGNAL("clicked()"), self.xPul2),
        QtCore.QObject.connect(self.pushButton_yPul1, QtCore.SIGNAL("clicked()"), self.yPul1),
        QtCore.QObject.connect(self.pushButton_yPul2, QtCore.SIGNAL("clicked()"), self.yPul2),
        QtCore.QObject.connect(self.pushButton_zPul1, QtCore.SIGNAL("clicked()"), self.zPul1),
        QtCore.QObject.connect(self.pushButton_zPul2, QtCore.SIGNAL("clicked()"), self.zPul2),
        QtCore.QObject.connect(self.pushButton_xHome, QtCore.SIGNAL("clicked()"), self.xHome),
        QtCore.QObject.connect(self.pushButton_yHome, QtCore.SIGNAL("clicked()"), self.yHome),
        QtCore.QObject.connect(self.pushButton_zHome, QtCore.SIGNAL("clicked()"), self.zHome),
        QtCore.QObject.connect(self.pushButton_out1, QtCore.SIGNAL("clicked()"), self.out1),
        QtCore.QObject.connect(self.pushButton_out2, QtCore.SIGNAL("clicked()"), self.out2),
        QtCore.QObject.connect(self.pushButton_out3, QtCore.SIGNAL("clicked()"), self.out3),
        QtCore.QObject.connect(self.pushButton_out4, QtCore.SIGNAL("clicked()"), self.out4),
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL("clicked()"), self.stop),
        QtCore.QObject.connect(self.pushButton_16, QtCore.SIGNAL("clicked()"), self.delete),

    def connect(self):
        print(dll.pySMCOpenEth(192,168,1,11))
        self.label.setText('connect')

    def stop(self):
        self.label.setText('stop')
        dll.pySMCClose()

    def delete(self):
        dll.pySMCWriteOutBit(1,1)
        dll.pySMCWriteOutBit(2,1)
        dll.pySMCWriteOutBit(3,1)
        dll.pySMCWriteOutBit(4,1)
        dll.pySMCWriteOutBit(5,1)
        dll.pySMCWriteOutBit(6,1)
        dll.pySMCWriteOutBit(7,1)
        dll.pySMCWriteOutBit(8,1)

    def xPul1(self):
        dll.pySMCPMovePluses(X_IAXIS,10000,IFABS_NO)

    def xPul2(self):
        dll.pySMCPMovePluses(X_IAXIS,-10000,IFABS_NO)

    def yPul1(self):
        dll.pySMCPMovePluses(Y_IAXIS,10000,IFABS_NO)

    def yPul2(self):
        dll.pySMCPMovePluses(Y_IAXIS,-10000,IFABS_NO)

    def zPul1(self):
        dll.pySMCPMovePluses(Z_IAXIS,10000,IFABS_NO)

    def zPul2(self):
        dll.pySMCPMovePluses(Z_IAXIS,-10000,IFABS_NO)

    def xHome(self):
        dll.pySMCHomeMove(X_IAXIS)              #X轴回零运动

    def yHome(self):
        dll.pySMCHomeMove(Y_IAXIS)              #Y轴回零运动

    def zHome(self):
        dll.pySMCHomeMove(Z_IAXIS)              #Z轴回零运动

    def out1(self):
        dll.pySMCWriteOutBit(1,0)

    def out2(self):
        dll.pySMCWriteOutBit(2,0)

    def out3(self):
        dll.pySMCWriteOutBit(3,0)

    def out4(self):
        dll.pySMCWriteOutBit(4,0)

    def displayUi(self, MicroValve):
        test1=float('%.3f' % (dll.pySMCGetWorkPosition(X_IAXIS)/10000))
        test2=dll.pySMCGetWorkPosition(X_IAXIS)%10000

    def handleDisplay(self, data):
        self.label.setText('x:'+str(data))   #槽函数


class Backend(QThread):     #新建一个线程类
    update_date = pyqtSignal(QString) #pyqt信号
    def run(self):      #重载Qthread run
        while True:
            # data =dll.pySMCGetWorkPosition(X_IAXIS)/10000
            # data1 =dll.pySMCGetWorkPosition(X_IAXIS)%10000
            data = float(dll.pySMCGetWorkPosition(X_IAXIS))
            data = str("%.3f"% (data/10000))
            # print(data)
            # data = QDateTime.currentDateTime()
            self.update_date.emit(QString(data))   #发送信号
            time.sleep(0.05)

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    import ctypes
    import threading

    SMC_OUT_VALIDVALUE     =   0    #//有效电平，通用IO为低电平, 当切换初始电平后，输出电平会相反
    SMC_OUT_INVALIDVALUE   =  1    #//高电平
    OUT_1   =	1		#OUT输出口1
    OUT_2   =	2		#OUT输出口2
    OUT_3   =	3		#/OUT输出口3
    OUT_4   =	4		#//OUT输出口4
    OUT_5   =	5		#//OUT输出口5
    OUT_6   =	6		#//OUT输出口6
    OUT_7   =	7		#//OUT输出口7
    OUT_8   =	8		#//OUT输出口8
    X_IAXIS	=   0		#//X轴
    Y_IAXIS	=	1		#//Y轴
    Z_IAXIS =   2		#//Z轴
    IFABS_YES  =  1		#//绝对坐标系
    IFABS_NO   =   0		#//不是绝对坐标系

    from time import ctime,sleep


    dll = ctypes.windll.LoadLibrary("pySmc.dll")
    app = QtGui.QApplication(sys.argv)
    MicroValve = QtGui.QDialog()
    ui = Ui_MicroValve()
    ui.setupUi(MicroValve)


    demoThread = Backend()
    demoThread.start();     #.start 执行了一个run
    demoThread.update_date.connect(ui.handleDisplay)    #信号与槽连接

    MicroValve.show()
    sys.exit(app.exec_())
