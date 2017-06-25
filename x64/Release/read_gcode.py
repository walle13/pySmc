# -*- coding:utf-8 -*-
import os
import time

gcode_file = open("micro.gcode")
gcode_all=[]
gcode_list=[]

while 1:
    gcode_line_i = gcode_file.readline()
    if not gcode_line_i:
        break
    gcode_all.append(gcode_line_i.strip('\n'))

for gcode_line_i in gcode_all:
	gcode_list.append(gcode_line_i)
	if len(gcode_list)== 5:
		print(gcode_list[0])# 你需要改这条
        gcode_list.pop(0)
        time.sleep(0.01)

for gcode_line_rest_4 in gcode_list:
	print(gcode_line_rest_4)# 你需要改这条

#gcode_file.close()
