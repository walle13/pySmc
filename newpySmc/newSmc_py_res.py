
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
import sys , re , os
import ctypes
from ctypes import *
import math

data_all = 11
g_handle = c_char()
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
        MicroValve.resize(700, 505)
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
        self.label_X = QtGui.QLabel(MicroValve)
        self.label_X.setGeometry(QtCore.QRect(420, 282, 81, 20))
        self.label_X.setObjectName(_fromUtf8("label_X"))
        self.textBrowser = QtGui.QTextBrowser(MicroValve)
        self.textBrowser.setGeometry(QtCore.QRect(410, 30, 180, 231))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_Y = QtGui.QLabel(MicroValve)
        self.label_Y.setGeometry(QtCore.QRect(420, 300, 81, 20))
        self.label_Y.setObjectName(_fromUtf8("label_Y"))
        self.label_Z = QtGui.QLabel(MicroValve)
        self.label_Z.setGeometry(QtCore.QRect(420, 320, 81, 20))
        self.label_Z.setObjectName(_fromUtf8("label_Z"))
        self.lineEdit_1 = QtGui.QLineEdit(MicroValve)
        self.lineEdit_1.setGeometry(QtCore.QRect(420, 340, 113, 20))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.label_1 = QtGui.QLabel(MicroValve)
        self.label_1.setGeometry(QtCore.QRect(420, 380, 81, 20))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(MicroValve)
        self.label_2.setGeometry(QtCore.QRect(420, 360, 81, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(MicroValve)
        self.label_3.setGeometry(QtCore.QRect(420, 400, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(MicroValve)
        self.label_4.setGeometry(QtCore.QRect(420, 420, 81, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_test4 = QtGui.QPushButton(MicroValve)
        self.pushButton_test4.setGeometry(QtCore.QRect(310, 430, 81, 71))
        self.pushButton_test4.setObjectName(_fromUtf8("pushButton_test4"))
        self.pushButton_test1 = QtGui.QPushButton(MicroValve)
        self.pushButton_test1.setGeometry(QtCore.QRect(40, 430, 81, 71))
        self.pushButton_test1.setObjectName(_fromUtf8("pushButton_test1"))
        self.pushButton_test2 = QtGui.QPushButton(MicroValve)
        self.pushButton_test2.setGeometry(QtCore.QRect(130, 430, 81, 71))
        self.pushButton_test2.setObjectName(_fromUtf8("pushButton_test2"))
        self.pushButton_test3 = QtGui.QPushButton(MicroValve)
        self.pushButton_test3.setGeometry(QtCore.QRect(220, 430, 81, 71))
        self.pushButton_test3.setObjectName(_fromUtf8("pushButton_test3"))
        self.lineEdit_2 = QtGui.QLineEdit(MicroValve)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 440, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(MicroValve)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 470, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_vext_x2 = QtGui.QPushButton(MicroValve)
        self.pushButton_vext_x2.setGeometry(QtCore.QRect(600, 190, 81, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(9)
        self.pushButton_vext_x2.setFont(font)
        self.pushButton_vext_x2.setObjectName(_fromUtf8("pushButton_vext_x2"))
        self.pushButton_vext_x1 = QtGui.QPushButton(MicroValve)
        self.pushButton_vext_x1.setGeometry(QtCore.QRect(600, 110, 81, 71))
        self.pushButton_vext_x1.setObjectName(_fromUtf8("pushButton_vext_x1"))
        self.pushButton_vext_y2 = QtGui.QPushButton(MicroValve)
        self.pushButton_vext_y2.setGeometry(QtCore.QRect(600, 350, 81, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(9)
        self.pushButton_vext_y2.setFont(font)
        self.pushButton_vext_y2.setObjectName(_fromUtf8("pushButton_vext_y2"))
        self.pushButton_vext_y1 = QtGui.QPushButton(MicroValve)
        self.pushButton_vext_y1.setGeometry(QtCore.QRect(600, 270, 81, 71))
        self.pushButton_vext_y1.setObjectName(_fromUtf8("pushButton_vext_y1"))

        self.retranslateUi(MicroValve)
        self.displayUi(MicroValve)
        QtCore.QObject.connect(MicroValve, QtCore.SIGNAL(_fromUtf8("accepted()")), self.label_X.clear)
        QtCore.QMetaObject.connectSlotsByName(MicroValve)

    def retranslateUi(self, MicroValve):
        MicroValve.setWindowTitle(_translate("MicroValve", "Dialog", None))
        self.pushButton_connect.setText(_translate("MicroValve", "connect", None))
        self.pushButton_microValve.setText(_translate("MicroValve", "Micro Valve", None))
        self.pushButton_yHome.setText(_translate("MicroValve", "File open", None))
        self.pushButton_xPul2.setText(_translate("MicroValve", "X-", None))
        self.pushButton_stop.setText(_translate("MicroValve", "stop", None))
        self.pushButton_16.setText(_translate("MicroValve", ".", None))
        self.pushButton_xPul1.setText(_translate("MicroValve", "X+", None))
        self.pushButton_yPul1.setText(_translate("MicroValve", "Y+", None))
        self.pushButton_zPul1.setText(_translate("MicroValve", "Z+", None))
        self.pushButton_out4.setText(_translate("MicroValve", "OUT4", None))
        self.pushButton_xHome.setText(_translate("MicroValve", "Home Move", None))
        self.pushButton_yPul2.setText(_translate("MicroValve", "Y-", None))
        self.pushButton_out1.setText(_translate("MicroValve", "OUT1", None))
        self.pushButton_out2.setText(_translate("MicroValve", "OUT2", None))
        self.pushButton_out3.setText(_translate("MicroValve", "OUT3", None))
        self.pushButton_zHome.setText(_translate("MicroValve", "Run", None))
        self.pushButton_zPul2.setText(_translate("MicroValve", "Z-", None))
        self.label_X.setText(_translate("MicroValve", "Textlabel_X", None))
        self.label_Y.setText(_translate("MicroValve", "Textlabel_Y", None))
        self.label_Z.setText(_translate("MicroValve", "Textlabel_Z", None))
        self.label_1.setText(_translate("MicroValve", "Textlabel_Z", None))
        self.label_2.setText(_translate("MicroValve", "Textlabel_Z", None))
        self.label_3.setText(_translate("MicroValve", "Textlabel_Z", None))
        self.label_4.setText(_translate("MicroValve", "Textlabel_Z", None))
        self.pushButton_test4.setText(_translate("MicroValve", "TEST4", None))
        self.pushButton_test1.setText(_translate("MicroValve", "TEST1", None))
        self.pushButton_test2.setText(_translate("MicroValve", "TEST2", None))
        self.pushButton_test3.setText(_translate("MicroValve", "TEST3", None))
        self.pushButton_vext_x2.setText(_translate("MicroValve", "VECT_X-", None))
        self.pushButton_vext_x1.setText(_translate("MicroValve", "VECT_X+", None))
        self.pushButton_vext_y2.setText(_translate("MicroValve", "VECT_Y-", None))
        self.pushButton_vext_y1.setText(_translate("MicroValve", "VECT_Y+", None))

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
        QtCore.QObject.connect(self.pushButton_microValve, QtCore.SIGNAL("clicked()"), self.micro),
        QtCore.QObject.connect(self.pushButton_vext_x1, QtCore.SIGNAL("clicked()"), self.vextX1),
        QtCore.QObject.connect(self.pushButton_vext_x2, QtCore.SIGNAL("clicked()"), self.vextX2),
        # QtCore.QObject.connect(self.pushButton_vext_y1, QtCore.SIGNAL("clicked()"), self.vextY1),
        # QtCore.QObject.connect(self.pushButton_vext_y2, QtCore.SIGNAL("clicked()"), self.vextY2),
        QtCore.QObject.connect(self.pushButton_test1, QtCore.SIGNAL("clicked()"), self.test1),
        QtCore.QObject.connect(self.pushButton_test2, QtCore.SIGNAL("clicked()"), self.test2),
        QtCore.QObject.connect(self.pushButton_test3, QtCore.SIGNAL("clicked()"), self.test3),
        QtCore.QObject.connect(self.pushButton_test4, QtCore.SIGNAL("clicked()"), self.test4),

# dll.SMCOpenEth.restype = c_int # addf 返回值的类型是 flaot
# dll.SMCOpenEth.argtypes = (c_char_p,POINTER(Point)) # addf 有两个形参，都是 float 类型c_char_p
    def connect(self):
        ip = "192.168.1.11"
        dll.SMCOpenEth.argtypes = (c_char_p,c_char_p)
        print(dll.SMCOpenEth(ip,byref(g_handle)))
        self.label_X.setText('connect')

    def stop(self):
        dll.SMCVectMoveStop.argtypes = (c_char_p)
        dll.SMCClose.argtypes = (c_char_p)
        dll.SMCVectMoveStop(byref(g_handle))
        dll.SMCClose(byref(g_handle))
        self.label_X.setText('stop')


    def delete(self):
        dll.SMCWriteOutBit.argtypes = (c_char_p,c_int,c_int)
        dll.SMCWriteOutBit(byref(g_handle),1,1)
        dll.SMCWriteOutBit(byref(g_handle),2,1)
        dll.SMCWriteOutBit(byref(g_handle),3,1)
        dll.SMCWriteOutBit(byref(g_handle),4,1)
        dll.SMCWriteOutBit(byref(g_handle),5,1)
        dll.SMCWriteOutBit(byref(g_handle),6,1)
        dll.SMCWriteOutBit(byref(g_handle),7,1)
        dll.SMCWriteOutBit(byref(g_handle),8,1)
        print('delete')

    def xPul1(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),X_IAXIS , 100)
        dll.SMCPMove(byref(g_handle),X_IAXIS,100.00,IFABS_YES)

    def xPul2(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),X_IAXIS , 100)
        dll.SMCPMove(byref(g_handle),X_IAXIS,-100.00,IFABS_NO)

    def yPul1(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),Y_IAXIS , 100)
        dll.SMCPMove(byref(g_handle),Y_IAXIS,100.00,IFABS_NO)

    def yPul2(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),Y_IAXIS , 100)
        dll.SMCPMove(byref(g_handle),Y_IAXIS,-100.00,IFABS_NO)

    def zPul1(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),Z_IAXIS , 50)
        dll.SMCPMove(byref(g_handle),Z_IAXIS,-100.00,IFABS_NO)

    def zPul2(self):
        dll.SMCSetLocateAcceleration.argtypes = (c_char_p,c_uint,c_uint)
        dll.SMCPMove.argtypes = (c_char_p, c_uint, c_double, c_uint)

        dll.SMCSetLocateAcceleration(byref(g_handle),Z_IAXIS , 50)
        dll.SMCPMove(byref(g_handle),Z_IAXIS,-100.00,IFABS_NO)

    def vextX1(self):
        dll.pySMCVectMoveStart()
        dll.pySMCVectMoveLineN(3 , 100000 , 100000 , 50000 , 0 , 30 , IFABS_YES)  #多轴插补 距离/1000
        # dll.pySMCVectMoveLineN(3 , 1000000 , 10000 , 50000 , 0 , 300 , IFABS_YES)  #多轴插补 距离/1000
        dll.pySMCVectMoveLineN(3 , 200000 , 20000 , 50000 , 0 , 30 , IFABS_YES)  #多轴插补 距离/1000

    def vextX2(self):
        dll.pySMCVectMoveStart()
        # dll.pySMCVectMoveLineN(3 , 1000000 , 10000 , 50000 , 0 , 300 , IFABS_YES)  #多轴插补 距离/1000
        # dll.pySMCVectMoveLineN(3 , 0 , 0 , 500000 , 0 , 300 , IFABS_YES)  #多轴插补 距离/1000
        dll.pySMCVectMoveLineN(3 ,0 , 1000 , 0 , 0 , 30 , IFABS_YES)  #多轴插补 距离/1000


    def xHome(self):    #HOME MOVE
        # dll.pySMCHomeMove(X_IAXIS)              #X轴回零运动
        dll.SMCHomeMove.argtypes = (c_char_p,c_uint)
        dll.SMCHomeMove(byref(g_handle),Z_IAXIS)
        while 1:    #检测轴移动状态
            ifHomeMove3 = dll.SMCHomeMove(byref(g_handle),Z_IAXIS)
            if ( ifHomeMove3 ==0):
                break

        dll.SMCHomeMove.argtypes = (c_char_p,c_uint)
        dll.SMCHomeMove(byref(g_handle),Y_IAXIS)
        while 1:    #检测轴移动状态
            ifHomeMove2 = dll.SMCHomeMove(byref(g_handle),Y_IAXIS)
            if (ifHomeMove2 ==0):
                break

        dll.SMCHomeMove.argtypes = (c_char_p,c_uint)
        dll.SMCHomeMove(byref(g_handle),X_IAXIS)
        while 1:    #检测轴移动状态
            ifHomeMove1 = dll.SMCHomeMove(byref(g_handle),X_IAXIS)
            if (ifHomeMove1 ==0):
                break

    def yHome(self):        #FILE OPEN
        # dll.pySMCHomeMove(Y_IAXIS)              #Y轴回零运动
        file_object = open("micro.gcode")
        lines = file_object.readlines() #读全部文件
        line_N1 = file_object.readline()   #读一行，带有‘\n’
        for line_N1 in lines:
            line_N1 = line_N1.strip('\n')  #去除 “\n”
            self.textBrowser.append(line_N1)
            print(line_N1)

    def zHome(self):    #RUN
        # dll.pySMCHomeMove(Z_IAXIS)              #Z轴回零运动
        global data_all
        file_object = open("micro.gcode")
        line_N1 = file_object.readline() #读一行，带有‘\n’
        lines = file_object.readlines() #读全部文件
        pul_X=0
        pul_Y=0
        pul_Z=0
        pul_U=0
        for line_N1 in lines:
            line_N1 = line_N1.strip('\n')  #去除 “\n”
            #print(line_N1)

            if line_N1[0]=='G' :        #识别指令是否为 ‘G’ 指令
                line_G= re.findall(".*G(\d+(?:\.\d+)?)",line_N1)  #读取G指令的类型
                if line_G[0] == "1":    #识别指令是否为 ‘G1’ 指令
                    # print 'G1'

                    position_X = re.findall(".*X(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
                    position_Y = re.findall(".*Y(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
                    position_Z = re.findall(".*Z(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
                    position_U = re.findall(".*U(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
                    speed_F = re.findall(".*F(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
                    position_all = position_X + position_Y + position_Z + position_U
                    print position_all , position_X , position_Y , position_Z , position_U ,speed_F

                    if position_X:
                        pul_X = int(float(position_X[0])*1000)
                    else:
                        pul_X = pul_X

                    if position_Y:
                        pul_Y = int(float(position_Y[0])*1000)
                    else:
                        pul_Y = pul_Y

                    if position_Z:
                        pul_Z = int(float(position_Z[0])*1000)
                    else:
                        pul_Z = pul_Z

                    if speed_F:
                        speed_f = int(float(speed_F[0])/100)
                    else:
                        speed_f = 10
                    # dll.pySMCPMovePluses(X_IAXIS,pul_X,IFABS_NO)
                    # dll.pySMCPMovePluses(Y_IAXIS,pul_Y,IFABS_NO)
                    # dll.pySMCPMovePluses(Z_IAXIS,pul_Z,IFABS_NO)

                    # dll.pySMCVectMoveLineN(2, _axis_iaxis, dist_array, 500, IFABS_NO)
                    # dll.pySMCVectMoveLine1(1, 1000 ,500, IFABS_NO)
                    print pul_X , pul_Y, pul_Z , pul_U
                    dll.SMCVectMoveStart.argtypes = (c_char_p)
                    dll.SMCVectMoveLineN.argtypes = (c_char_p,c_int,c_int_p,c_double_p,c_double,c_int,cint)

                    piaxisList = [1,2,3,4]
                    DistanceList = [pul_X , pul_Y , pul_Z , 0]
                    dll.SMCVectMoveStart(byref(g_handle))
                    dll.SMCVectMoveLineN(byref(g_handle),3 ,byref(piaxisList),byref(DistanceList) , speed_f , IFABS_YES)  #多轴插补 距离/1000
                    print ('ok')
                    print(dll.pySMCGetVectMoveRemainSpace())
                    # time.sleep(5)
                    # while 1:    #检测轴移动状态
                    #     smcvect = dll.pySMCVectMoveEnd()
                    #     if smcvect !=0:
                    #         break

                elif line_G[0] == "2":  #识别指令是否为 ‘G2’ 指令
                    print 'G2'

                elif line_G[0] == "3":  #识别指令是否为 ‘G3’ 指令
                    print 'G3'

                elif line_G[0] == "26":  #识别指令是否为 ‘G26’ 指令 ， 回零点
                    print 'G26'
                    dll.pySMCHomeMove(Z_IAXIS)
                    while 1:    #检测轴移动状态
                        ifHomeMove3 = dll.pySMCIfHomeMoveing(Z_IAXIS)
                        if ( ifHomeMove3 ==0):
                            break

                    dll.pySMCHomeMove(Y_IAXIS)
                    while 1:    #检测轴移动状态
                        ifHomeMove2 = dll.pySMCIfHomeMoveing(Y_IAXIS)
                        if (ifHomeMove2 ==0):
                            break

                    dll.pySMCHomeMove(X_IAXIS)
                    while 1:    #检测轴移动状态
                        ifHomeMove1 = dll.pySMCIfHomeMoveing(X_IAXIS)
                        if (ifHomeMove1 ==0):
                            break
                    #
                    # while 1:    #检测轴移动状态
                    #     smcvect = dll.pySMCVectMoveEnd()
                    #     if smcvect !=0:
                    #         break
                    # print(dll.pySMCHomeMove(Z_IAXIS))

                elif line_G[0] == "90":  #识别指令是否为 ‘G90' 指令 , 绝对坐标系
                    print 'G90'

                else:
                    print 'G_err'

            elif line_N1[0]=='M' :          #识别指令是否为 ‘M’ 指令
                line_M= re.findall(".*M(\d+(?:\.\d+)?)",line_N1)  #正则运算，取M 直接的数据
                while 1:    #检测轴移动状态
                    smcvect = dll.pySMCVectMoveEnd()
                    if smcvect !=0:
                        break

                if line_M[0] == "101":  #识别指令是否为 ‘M102’ 指令
                    print 'M101'
                    dll.pySMCWriteOutBit(4,1)
                    time.sleep(0.1)
                elif line_M[0] == "103":  #识别指令是否为 ‘M103’ 指令
                    print 'M103'
                    dll.pySMCWriteOutBit(4,0)
                    time.sleep(0.1)
                else:
                    print 'err'

            elif line_N1[0] == 'S':         #识别指令是否为 ‘S’ 指令
                print 'S'

            else:
                print 'not find' #解析Gcode





    def out1(self):
        dll.pySMCWriteOutBit(1,0)
        print(dll.pySMCVectMoveStart())  #110014 时候已经运行结束， 0 时候正在运行

    def out2(self):
        dll.pySMCWriteOutBit(2,0)
        print(dll.pySMCVectMovePause())

    def out3(self):
        dll.pySMCWriteOutBit(3,0)
        print(dll.pySMCVectMoveStop())

    def out4(self):
        dll.pySMCWriteOutBit(4,0)
        dll.pySMCVectMoveEnd()


    def test1(self):
        print('test1')
        print('X:'+str(dll.pySMCCheckDown(X_IAXIS)) + ' Y:'+str(dll.pySMCCheckDown(Y_IAXIS)) + ' Z:'+str(dll.pySMCCheckDown(Z_IAXIS)))      #检测轴移动状态

    def test2(self):
        print('test2')
        print('X:'+str(dll.pySMCGetZeroSpeed(X_IAXIS))+ ' Y:'+str(dll.pySMCGetZeroSpeed(Y_IAXIS)) + ' Z:'+str(dll.pySMCGetZeroSpeed(Z_IAXIS)))

    def test3(self):
        print('test3')
        # print(dll.pySMCWaitVectLength())
        # c_double double_buff = 1024.1
        dll.pySMCSetPosition.restype = c_double
        dll.pySMCSetPosition.argtypes = (c_int ,c_double)
        print(dll.pySMCSetPosition(X_IAXIS,1024.4))
        # print(dll.pySMCGetWorkOriginPosition(X_IAXIS))

    def test4(self):
        global data_all
        print('test4')
        print('X:'+str(dll.pySMCIfHomeMoveing(X_IAXIS))+ ' Y:'+str(dll.pySMCIfHomeMoveing(Y_IAXIS)) + ' Z:'+str(dll.pySMCIfHomeMoveing(Z_IAXIS)))
        print(data_all)

    def micro(self):
        #self.textBrowser.setText('stop'+"\n")
        #self.textBrowser.append("123")
        file_object = open("micro.txt")
        lines = file_object.readlines() #读全部文件
        line = file_object.readline()   #读一行，带有‘\n’
        for line in lines:
            line = line.strip('\n')  #去除 “\n”
            self.textBrowser.append(line)
            print(line)
    #    self.textBrowser.toPlainText('stop'+"\n")


    def displayUi(self, MicroValve):
        test1=float('%.3f' % (dll.pySMCGetWorkPosition(X_IAXIS)/10000))
        test2=dll.pySMCGetWorkPosition(X_IAXIS)%10000


    def handleDisplay1(self, data1):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_X.setText('X:'+str(data1))   #槽函数

    def handleDisplay2(self, data2):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_Y.setText('Y:'+str(data2))   #槽函数

    def handleDisplay3(self, data3):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_Z.setText('Z:'+str(data3))   #槽函数

    def handleDisplay4(self, data_t1):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_1.setText(str(data_t1))   #槽函数

    def handleDisplay5(self, data_t2):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_2.setText(str(data_t2))   #槽函数

    def handleDisplay6(self, data_t3):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_3.setText(str(data_t3))   #槽函数

    def handleDisplay7(self, data_t4):  #接收信号
        # self.label.setText('X:'+str(data))   #槽函数
        self.label_4.setText(str(data_t4))   #槽函数

class Backend(QThread):     #新建一个线程类
    update_date1 = pyqtSignal(QString) #创建pyqt信号， update_date 信号
    update_date2 = pyqtSignal(QString) #创建pyqt信号， update_date2 信号
    update_date3 = pyqtSignal(QString) #创建pyqt信号， update_date2 信号
    update_data_t1 = pyqtSignal(QString)
    update_data_t2 = pyqtSignal(QString)
    update_data_t3 = pyqtSignal(QString)
    update_data_t4 = pyqtSignal(QString)

    # data_all = 10
    # def fname(self):
    #     return data_all
    def run(self):      #重载Qthread run
        global data_all
        while True:
            # data =dll.pySMCGetWorkPosition(X_IAXIS)/10000
            # data1 =dll.pySMCGetWorkPosition(X_IAXIS)%10000

            data1 = float(dll.pySMCGetPosition(X_IAXIS))
            data1 = str("%.3f"% (data1/10000))
            data2 = float(dll.pySMCGetWorkPosition(X_IAXIS))
            data2 = str("%.3f"% (data2/10000))
            data3 = float(dll.pySMCGetWorkPosition(Z_IAXIS))
            data3 = str("%.3f"% (data3/10000))
            # data3 = str(dll.pySMCVectMoveEnd())     #检测轴移动状态

            data_t1 = str(dll.pySMCVectMoveEnd())     #检测插补运行状态

            data_all = dll.pySMCVectMoveEnd()
            data_t2 = str(dll.pySMCGetVectMoveState())     #检测插补状态
            data_t3 = str(dll.pySMCWaitVectLength(1000000))     #检测轴移动状态
            # data_t3 = str(data_t3)
            # data_t4 = float(dll.pySMCGetCurRunVectLength()) #插补运动可以填入的线段数
            # data_t4 = str("%.3f"% (data_t4/1000))     #检测轴移动状态
            data_t4 = str(dll.pySMCGetVectMoveRemainSpace())

            # print(data)
            # data = QDateTime.currentDateTime()
            self.update_date1.emit(QString(data1))   #发送 update_date 信号，附带 data 数据
            self.update_date2.emit(QString(data2))   #发送 update_date2 信号，附带 data2 数据
            self.update_date3.emit(QString(data3))   #发送 update_date3 信号，附带 data3 数据
            self.update_data_t1.emit(QString(data_t1))
            self.update_data_t2.emit(QString(data_t2))
            self.update_data_t3.emit(QString(data_t3))
            self.update_data_t4.emit(QString(data_t4))
            time.sleep(0.05)


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
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



    dll = ctypes.windll.LoadLibrary("smc6x.dll")
    app = QtGui.QApplication(sys.argv)
    MicroValve = QtGui.QDialog()
    ui = Ui_MicroValve()
    ui.setupUi(MicroValve)


    demoThread = Backend()
    demoThread.start();     #.start 执行了一个run
    demoThread.update_date1.connect(ui.handleDisplay1)    #信号与槽连接 update_date---ui.handleDisplay
    demoThread.update_date2.connect(ui.handleDisplay2)    #信号与槽连接 update_date---ui.handleDisplay2
    demoThread.update_date3.connect(ui.handleDisplay3)    #信号与槽连接 update_date---ui.handleDisplay2
    demoThread.update_data_t1.connect(ui.handleDisplay4)
    demoThread.update_data_t2.connect(ui.handleDisplay5)
    demoThread.update_data_t3.connect(ui.handleDisplay6)
    demoThread.update_data_t4.connect(ui.handleDisplay7)
    # buff = demoThread.fname()

    MicroValve.show()
    sys.exit(app.exec_())
