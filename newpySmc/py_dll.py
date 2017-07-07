#  -*- coding:utf-8 -*-

import ctypes
from ctypes import *
import math
SMC_OUT_VALIDVALUE     =   0    #//有效电平，通用IO为低电平, 当切换初始电平后，输出电平会相反
SMC_OUT_INVALIDVALUE   =  1    #//高电平
OUT_1   =	1		#OUT输出口1
OUT_2   =	2		#OUT输出口2
OUT_3   =	3		#/OUT输出口3
OUT_4   =	4		#//OUT输出口4
OUT_5   =	5		#//OUT输出口5
OUT_6   =	6		#//OUT输出口6s
OUT_7   =	7		#//OUT输出口7
OUT_8   =	8		#//OUT输出口8
X_IAXIS	=   0		#//X轴
Y_IAXIS	=	1		#//Y轴
Z_IAXIS =   2		#//Z轴
IFABS_YES  =  1		#//绝对坐标系
IFABS_NO   =   0		#//不是绝对坐标系
# list g_handle
# g_handle[0] = None
g_handle = c_char()
ip = "192.168.1.11"
# ip = c_wchar("aa")

# b = pointer(a)        # 创建指针
# g_handle = POINTER(c_int)(a) # 创建指针
#
dll = ctypes.windll.LoadLibrary("smc6x.dll")
axis_iaxis = [0,1,2,3]
dist_array = [100,100,100,200]


# SMCHANDLE * aaa = NULL;
# dll.SMCOpenEth.restype = c_int # addf 返回值的类型是 flaot
# dll.SMCOpenEth.argtypes = (c_char_p,POINTER(Point)) # addf 有两个形参，都是 float 类型c_char_p
dll.SMCOpenEth.argtypes = (c_char_p,c_char_p)
 # addf 有两个形参，都是 float 类型c_char_p

print(dll.SMCOpenEth(ip,byref(g_handle)))
	# iresult = SMCOpenEth("192.168.1.11", &g_handle);

# SMCOpenEth(char *ipaddr, SMCHANDLE * phandle);

print(dll.SMCHomeMove(byref(g_handle),X_IAXIS));             #Y轴回零运动
# dll.pySMCHomeMove(Y_IAXIS)              #Y轴回零运动B
# dll.pySMCHomeMove(Z_IAXIS)              #Y轴回零运动
# dll.SMCWriteOutBit(2,1)
# dll.SMCWriteOutBit(2,0)
# dll.SMCPMovePluses(Y_IAXIS,10000,IFABS_NO)
#
# dll.SMCVectMoveStop()
# dll.SMCVectMoveStart()
# # print(dll.pySMCVectMoveLineN(3,float(101.1), float(101.1), float(101.1), float(101.1),float(30), IFABS_YES))
# print(dll.SMCVectMoveLineN(3,10000,10000,1000,200,30, IFABS_YES))  #多轴插补 距离/1000
# # dll.pySMCVectMoveStop()
# # #dll.pySMCHomeMove(Y_IAXIS)              #Y轴回零运动
# X_Position = dll.SMCGetPosition(X_IAXIS)/10000
# Y_Position = dll.SMCGetPosition(Y_IAXIS)/10000
# Z_Position = dll.SMCGetPosition(Z_IAXIS)/10000
# X_WorkPosition =dll.SMCGetWorkPosition(X_IAXIS)/10000
# Y_WorkPosition =dll.SMCGetWorkPosition(Y_IAXIS)/10000
# Z_WorkPosition =dll.SMCGetWorkPosition(Z_IAXIS)/10000
# print(('X:%.3f'%(X_Position)) + (' Y:%.3f'%(X_Position)) + (' Z:%.3f'%(X_Position)))            #读取XYZ轴机械坐标
# print(('X:%.3f'%(X_WorkPosition)) + (' Y:%.3f'%(Y_WorkPosition)) + (' Z:%.3f'%(Z_WorkPosition)))            #读取XYZ轴机械坐标
#
# #print(dll.test1(1,2,3),123)
