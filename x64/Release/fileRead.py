# -*- coding: utf-8 -*-
# fr = file_object.read()  #用read()方法读取文件内容
# fr = file_object.readline()  # readline() 读单行
#  line = line.strip('\n')  #去除 “\n”
# fr1 = file_object.readline() fr2 = file_object.readline()  #读两行
# fr = file_object.readlines()  #readlines() #读全部行,用‘***’ ，‘**’， 分开
## 总结
## ^ 匹配字符串的开始。
## $ 匹配字符串的结尾。
## \b 匹配一个单词的边界。
## \d 匹配任意数字。
## \D 匹配任意非数字字符。
## x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
## x* 匹配0次或者多次 x 字符。
## x+ 匹配1次或者多次 x 字符。
## x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
## (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
## (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
##
# # File: readline-example-5.py
#
# file = open("sample.txt")
#
# for line in file:
#     pass # do something


import sys , re , os
import time

lines = []
line = []
line_N1 = []


file_object = open("micro.gcode")
line_N1 = file_object.readline() #读一行，带有‘\n’
lines = file_object.readlines() #读全部文件
# gcode_all.append(gcode_line_i.strip('\n'))
# line_N1 = "G1 X218.99 Y78.99 Z10 F5000"
line_N2 = "M103"
for line_N1 in lines:
    line_N1 = line_N1.strip('\n')  #去除 “\n”
    #print(line_N1)
    if line_N1[0]=='G' :        #识别指令是否为 ‘G’ 指令
        line_G= re.findall(".*G(\d+(?:\.\d+)?)",line_N1)  #读取G指令的类型
        if line_G[0] == "1":    #识别指令是否为 ‘G1’ 指令
            print 'G1'
            position_X = re.findall(".*X(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
            position_Y = re.findall(".*Y(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
            position_Z = re.findall(".*Z(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
            position_U = re.findall(".*U(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
            speed_F = re.findall(".*F(\d+(?:\.\d+)?)",line_N1)  #正则运算，取X，Y 直接的数据
            position_all = position_X + position_Y + position_Z + position_U
            print position_all , position_X , position_Y , position_Z , position_U

            time.sleep(0.1)
        elif line_G[0] == "2":  #识别指令是否为 ‘G2’ 指令
            print 'G2'
        elif line_G[0] == "3":  #识别指令是否为 ‘G3’ 指令
            print 'G3'
        else:
            print 'G_err'

    elif line_N1[0]=='M' :          #识别指令是否为 ‘M’ 指令
        line_M= re.findall(".*M(\d+(?:\.\d+)?)",line_N1)  #正则运算，取M 直接的数据

        if line_M[0] == "101":  #识别指令是否为 ‘M102’ 指令
            print 'M101'
        elif line_M[0] == "103":  #识别指令是否为 ‘M103’ 指令
            print 'M103'
        else:
            print 'err'

    elif line_N1[0] == 'S':         #识别指令是否为 ‘S’ 指令
        print 'S'

    else:
        print 'not find'


# for line in lines:
#     line = line.strip('\n')  #去除 “\n”
#     print(line)
    #
    # if not runcode:
    #     runcode = 1
    #     gCode =[]
    #     len（gCode）= 5
    #     time.sleep(0.5) and line[1]=='1'

file_object.close()



# while 1:
#     line = file_object.readline()
#     print line
#     if not line:
#         break
#     #
# file_object.close()

# fr2 = file_object.readline()
#fr = file_object.read()  #用read()方法读取文件内容
#fr = file_object.readlines()  #readlines() 读全部行
# print fr1,fr2  #打印所读取到的内容

# for line in file_object:
#      process line

# f.write("G90"+"\n"+"G21"+"\n"+"M103"+"\n"+"M207 N1"+"\n")
# f.write("G1 X200 Y65 Z0.5 F3000"+"\n")
# f.write("G92 E0.0"+"\n"+"M113 S1.0"+"\n")
# f.write("M140 S25.0"+"\n"+"M104 S25.0"+"\n"+"M109 S25.0"+"\n")
# f.write("G1 X200 Y65 Z0.5 F3000"+"\n")
# for i in range(0,20):
#     for j in range(0,20):
#         temX1=str(firstX+float(i)/1-0.01)
#         temY1=str(firstY+float(j)/1-0.01)
#         temX2=str(firstX+float(i)/1)
#         temY2=str(firstY+float(j)/1)
#         f.write("M101""\n")
#         f.write("G1 X"+ temX1 + " " + "Y"+ temY1 +" F5000"+ "\n")
#         f.write("G1 X"+ temX2 + " " + "Y"+ temY2 +" F50"+ "\n")
#         f.write("M103""\n")
#     j=0
# f.write("G1 Z60"+"\n")
# f.write("M113 S0.0"+"\n"+"M140 S0.0"+"\n"+"M04"+"\n")
# f.close()

#
# file_object = open('index of.txt', 'a' )
# file_object.write(url+'\n')


# #读文本文件
# input = open('data', 'r')
# #第二个参数默认为r
# input = open('data')
#
#
#
# #读二进制文件
# input = open('data', 'rb')
#
#
# #读取所有内容
# file_object = open('thefile.txt')
# try:
#      all_the_text = file_object.read( )
# finally:
#      file_object.close( )
#
#
# #读固定字节
# file_object = open('abinfile', 'rb')
# try:
#     while True:
#          chunk = file_object.read(100)
#         if not chunk:
#             break
#          do_something_with(chunk)
# finally:
#      file_object.close( )
#
#
# #读每行
# list_of_all_the_lines = file_object.readlines()
#
# 如果文件是文本文件，还可以直接遍历文件对象获取每行：
#
# for line in file_object:
#      process line
