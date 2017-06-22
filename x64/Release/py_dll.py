#  -*- coding:utf-8 -*-

import ctypes
import math
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

dll = ctypes.windll.LoadLibrary("pySmc.dll")

# SMCHANDLE * aaa = NULL;

print(dll.pySMCOpenEth(192,168,1,11))
dll.pySMCWriteOutBit(2,0)
dll.pySMCPMovePluses(Y_IAXIS,10000,IFABS_NO)
#dll.pySMCHomeMove(Y_IAXIS)              #Y轴回零运动
print('%.3f'%(dll.pySMCGetPosition(Y_IAXIS)/10000))            #读取Y轴机械坐标
print('%.3f'%(dll.pySMCGetWorkPosition(Y_IAXIS)/10000))            #读取Y轴工件坐标
#print(dll.test1(1,2,3),123)
