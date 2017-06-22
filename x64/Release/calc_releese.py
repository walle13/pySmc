# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
# ---num0 = 0
# ---num1 = 0    按键新输入的数
# ---num2 = 0    计算后缓存的数
# ---flag1 = 0   判断计算类型 1 2 3 4 --- + - * /
# ---flag0 = 0
# ---zero = 0     判断输入的数值是否为零，0 表示为0 。区分运算 0 和输入 0

from PyQt4 import QtCore, QtGui

import sys

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

num0 = 0
num1 = 0
num2 = 0
flag1 = 0
flag0 = 0
zero = 1


class Ui_Form(QtGui.QDialog):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("CALC"))
        Form.resize(347, 341)
        Form.setAutoFillBackground(False)
        self.pushButton_1 = QtGui.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 200, 71, 61))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 200, 71, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 200, 71, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 71, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 130, 71, 61))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 130, 71, 61))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 60, 71, 61))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 60, 71, 61))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 60, 71, 61))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 270, 71, 61))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 270, 71, 61))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 60, 71, 61))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(260, 130, 71, 61))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 200, 71, 61))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(260, 270, 71, 61))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(180, 270, 71, 61))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe 仿宋 Std R"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "WALLE_CALC", None))
        self.pushButton_1.setText(_translate("Form", "1", None))
        self.pushButton_2.setText(_translate("Form", "2", None))
        self.pushButton_3.setText(_translate("Form", "3", None))
        self.pushButton_4.setText(_translate("Form", "4", None))
        self.pushButton_5.setText(_translate("Form", "5", None))
        self.pushButton_6.setText(_translate("Form", "6", None))
        self.pushButton_7.setText(_translate("Form", "7", None))
        self.pushButton_8.setText(_translate("Form", "8", None))
        self.pushButton_9.setText(_translate("Form", "9", None))
        self.pushButton_10.setText(_translate("Form", "0", None))
        self.pushButton_11.setText(_translate("Form", ".", None))
        self.pushButton_12.setText(_translate("Form", "+", None))
        self.pushButton_13.setText(_translate("Form", "-", None))
        self.pushButton_14.setText(_translate("Form", "*", None))
        self.pushButton_15.setText(_translate("Form", "/", None))
        self.pushButton_16.setText(_translate("Form", "=", None))

        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL("clicked()"), self.clicked),
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL("clicked()"), self.clear),
        QtCore.QObject.connect(self.pushButton_12, QtCore.SIGNAL("clicked()"), self.add),
        QtCore.QObject.connect(self.pushButton_13, QtCore.SIGNAL("clicked()"), self.sub),
        QtCore.QObject.connect(self.pushButton_14, QtCore.SIGNAL("clicked()"), self.mul),
        QtCore.QObject.connect(self.pushButton_15, QtCore.SIGNAL("clicked()"), self.div),
        QtCore.QObject.connect(self.pushButton_16, QtCore.SIGNAL("clicked()"), self.allcalc),
        # self.setWindowTitle("Connections")

    def add(self):
        global flag1, num2, num1, num0, flag0
        if flag0 == 6:  # 判断上位是不是 =
            if num1 != 0:  # 判断  = 之后，是开始新一轮计算还是运动原结果
                flag1 = 5
                num2 = 0  # 清除运算结果
            else:
                num2 = num0
                flag1 = 1  # 代表加法
        elif flag1 == 0:
            flag1 = 1
        self.calc()
        flag1 = 1  # 代表加法
        flag0 = 0  # 清除 “= ”记录
        print("nun2 %s" % num2)
        print("+")
        # self.label.setText("%s" % num2)  # 打印输出结果

        # if flag0 == 5:  # 判断上位是不是 =
        #     num2 = num0
        # if num1 != 0:  # 如果有新输入要被运算数，进行运算
        #     num2 += num1
        #     num1 = 0
        #     self.label.setText("%s" % num2)  # 打印输出结果
        #     print("nun2 %s" % num2)
        # else:
        #     self.label.setText("+")
        #     print("+")

    def sub(self):
        global flag1, num2, num1, num0, flag0
        if flag0 == 6:  # 判断上位是不是 =
            if num1 != 0:  # 判断  = 之后，是开始新一轮计算还是运动原结果
                flag1 = 5
                num2 = 0  # 清除运算结果
            else:
                num2 = num0
                flag1 = 2  # 代表减法
        elif flag1 == 0:
            flag1 = 2
        self.calc()
        flag1 = 2  # 代表加法
        flag0 = 0  # 清除 “= ”记录
        print("nun2 %s" % num2)
        print("-")
        # if flag0 == 5:  # 判断上位是不是 =
        #     num2 = num0
        # if num1 != 0:  # 如果有新输入要被运算数，进行运算
        #     if num2 == 0:
        #         num2 = num1
        #     else:
        #         num2 -= num1
        #     num1 = 0
        #     self.label.setText("%s" % num2)  # 打印输出结果
        #     print("nun2 %s" % num2)
        # else:
        #     self.label.setText("-")
        #     print("-")

    def mul(self):
        global flag1, num2, num1, num0, flag0
        if flag0 == 5:  # 判断上位是不是 =
            if num1 != 0:  # 判断  = 之后，是开始新一轮计算还是运动原结果
                flag1 = 5
                num2 = 0  # 清除运算结果
            else:
                num2 = num0
                flag1 = 3  # 代表成法
        elif flag1 == 0:
            flag1 = 3
        self.calc()
        flag1 = 3  # 代表加法
        flag0 = 0  # 清除 “= ”记录
        print("nun2 %s" % num2)
        print("*")
        # if flag0 == 5:       #判断上位是不是 =
        #     num2 = num0
        # if num1 != 0:  # 如果有新输入要被运算数，进行运算
        #     if num2 == 0:
        #         num2 = num1 * 1
        #     else:
        #         num2 = num1 * num2
        #     num1 = 0
        #     self.label.setText("%s" % num2)  # 打印输出结果
        #     print("nun2 %s" % num2)
        # else:
        #     self.label.setText("*")
        #     print("*")

    def div(self):
        global flag1, num2, num1, num0, flag0
        if flag0 == 5:  # 判断上位是不是 =
            if num1 != 0:  # 判断  = 之后，是开始新一轮计算还是运动原结果
                flag1 = 5
                num2 = 0  # 清除运算结果
            else:
                num2 = num0
                flag1 = 4  # 代表除法
        elif flag1 == 0:
            flag1 = 4
        self.calc()
        flag1 = 4  # 代表加法
        flag0 = 0  # 清除 “= ”记录
        print("nun2 %s" % num2)
        print("/")
        # self.label.setText("%s" % num2)  # 打印输出结果

        # if flag0 == 5:      # 判断上位是不是 =
        #     num2 = num0
        # if num1 != 0:  # 如果有新输入要被运算数，进行运算
        #     if num2 == 0:
        #         num2 = num1 / 1
        #     else:
        #         num2 = num2 / num1
        #     num1 = 0
        #     self.label.setText("%f" % num2)  # 打印输出结果,
        #     print("nun2 %s" % num2)
        # else:
        #     self.label.setText("/")
        #     print("/")

    def calc(self):
        global flag1, num2, num1, num0, flag0, zero
        if num1 != 0:
            if flag1 == 1:
                num2 += num1
                self.label.setText("%s" % num2)
            elif flag1 == 2:
                if num1 != 0:  # 如果有新输入要被运算数，进行运算
                    if (num2 == 0 and zero != 0):  # 排除默认 0 和输入 0 的计算
                        num2 = num1 - 0
                    else:
                        num2 = num2 - num1
                else:
                    num2 = num1 - num2
                    # num2 -= num1
                self.label.setText("%s" % num2)
            elif flag1 == 3:
                if num1 != 0:  # 如果有新输入要被运算数，进行运算
                    if (num2 == 0 and zero != 0):  # 排除默认 0 和输入 0 的计算
                        num2 = num1 * 1
                    else:
                        num2 = num2 * num1
                else:
                    num2 = num1 * num2
                self.label.setText("%s" % num2)
            elif flag1 == 4:
                if num1 != 0:  # 如果有新输入要被运算数，进行运算
                    if (num2 == 0 and zero != 0):  # 排除默认 0 和输入 0 的计算
                        num2 = num1 / 1
                    else:
                        num2 = num2 / num1
                    self.label.setText("%f" % num2)
                    print('right')
                else:
                    # self.label.setText("%f" % num2)
                    self.label.setText("ERROR")
                    self.clear()
                    print('errr')
            elif flag1 == 5:
                self.label.setText("%f" % num0)
            print("nun2 %s" % num2)
            if num2 == 0:
                zero = 0
            else:
                zero = 1
            num1 = 0
            num0 = num2  # 缓存 “=” 计算结果
            # num2 = 0
            # flag0 = 5  # 完成“=”计算，标记
        else:
            if zero == 0:
                if flag1 == 1:
                    num2 += num1
                    self.label.setText("%s" % num2)
                elif flag1 == 2:
                    num2 -= num1
                    self.label.setText("%s" % num2)
                elif flag1 == 3:
                    num2 *= num1
                    self.label.setText("%s" % num2)
                elif flag1 == 4:
                    self.label.clear()
                    self.label.setText("Error")

            else:
                if flag1 == 1:
                    self.label.setText("+")
                elif flag1 == 2:
                    self.label.setText("-")
                elif flag1 == 3:
                    self.label.setText("*")
                elif flag1 == 4:
                    self.label.setText("/")
                elif flag1 == 5:
                    self.label.setText("=")
                else:
                    self.label.setText("%f" % num2)

    def allcalc(self):
        global flag1, num2, num1, num0, flag0, zero
        flag0 = 6  # 完成“=”计算，标记
        if (flag1 == 4 and num1 == 0 and zero != 0):
            num2 = 1
            num0 = num2  # 缓存 “=” 计算结果
            self.label.setText("%f" % num2)
        else:
            self.calc()
        flag1 = 0
        if num2 == 0:  # 判断 = 运算之后的结果，为 0 做特殊标记。
            zero = 0
        else:
            zero = 1
        print('num2= %s' % num2)
        print('num1= %s' % num1)

    def clicked(self):
        global num1, flag0, num2, zero
        if flag0 == 6:
            num2 = 0
        button = self.sender()
        num1 = num1 * 10 + int(button.text())
        self.label.setText("%s" % num1)
        if num1 == 0:
            zero = 0
        flag0 = 0  # 清空 “=” 计算标记
        print("nun1 %s" % num1)  # 在监视窗输出

    def clear(self):
        global flag1, num2, num1, flag0, num0, zero
        flag1 = 0
        num1 = 0
        num2 = 0
        num0 = 0
        flag0 = 0
        zero = 1
        self.label.setText("")
        print('clear')


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

'''    def keyPressEvent(self, event):
        key = event.key()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_1 :
            QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL("clicked()"), self.clicked),
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_2:
            QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.clicked),   '''
