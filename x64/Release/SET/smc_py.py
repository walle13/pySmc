# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smc_py.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MicroValve.resize(551, 456)
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
        self.label.setGeometry(QtCore.QRect(420, 282, 81, 20))
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
        self.lineEdit = QtGui.QLineEdit(MicroValve)
        self.lineEdit.setGeometry(QtCore.QRect(410, 380, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(MicroValve)
        QtCore.QObject.connect(MicroValve, QtCore.SIGNAL(_fromUtf8("accepted()")), self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MicroValve)

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MicroValve = QtGui.QDialog()
    ui = Ui_MicroValve()
    ui.setupUi(MicroValve)
    MicroValve.show()
    sys.exit(app.exec_())

