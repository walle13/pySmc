# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

class MyWindow(QtGui.QWidget):
    '''自定义窗口类'''
    ############################# 构造、析构函数 #################################
    def __init__(self,parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(MyWindow,self).__init__(parent)
        # 设置窗口固定尺寸
        self.setFixedSize(QtCore.QSize(800,600))
        # 创建主控件
        bodyWidget = QtGui.QWidget(self)
        # 创建主布局
        mainLayout = QtGui.QVBoxLayout(bodyWidget)
        # 遍历创建按钮
        for i in range(4):
            # 创建自定义按钮
            button = MyButton(self)
            # 设置文本内容
            button.setText("测试%s" % i)
            # 添加控件
            mainLayout.addWidget(button)
            # 设置按钮点击连接槽函数
            button.clicked.connect(self.OnClick)
    ############################### 命令 ########################################
    def OnClick(self):
        '''响应点击'''
        QtGui.QMessageBox.about(self,"测试","点击弹出窗口成功")
    ################################ 事件 ########################################
    def mousePressEvent(self,event):
        '''鼠标按下事件'''
        # 判断是否为鼠标左键按下
        if event.button() == QtCore.Qt.LeftButton:
            # 设置窗口背景颜色
            self.setStyleSheet('''background-color:cyan;''')
