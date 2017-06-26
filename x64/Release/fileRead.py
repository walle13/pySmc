# -*- coding: utf-8 -*-
# fr = file_object.read()  #用read()方法读取文件内容
# fr = file_object.readline()  # readline() 读单行
#  line = line.strip('\n')  #去除 “\n”
# fr1 = file_object.readline() fr2 = file_object.readline()  #读两行
# fr = file_object.readlines()  #readlines() #读全部行,用‘***’ ，‘**’， 分开

# # File: readline-example-5.py
#
# file = open("sample.txt")
#
# for line in file:
#     pass # do something


import sys
import time
lines = []
line = []

file_object = open("micro.txt")
line = file_object.readline() #读一行，带有‘\n’
lines = file_object.readlines() #读全部文件
# gcode_all.append(gcode_line_i.strip('\n'))
line_N1 = "G1 X218.99 Y78.99 F5000"
if line_N1[0]=='G':
    print 'G'
else:
    print 'err'

# for line in lines:
#     line = line.strip('\n')  #去除 “\n”
#     print(line)
    #
    # if not runcode:
    #     runcode = 1
    #     gCode =[]
    #     len（gCode）= 5
    #     time.sleep(0.5)

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
