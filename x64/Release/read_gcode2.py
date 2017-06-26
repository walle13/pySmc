# -*- coding:utf-8 -*-
import os
import time

count = 0
thefile = open(r"1.txt",'rb')

while True:
    buffer = thefile.read(1024 * 8192)
    if not buffer:
        break
    count += buffer.count('\n')
thefile.close()
print count


thefile = open(r"1.txt",'rb')
glines=thefile.readlines()
# print (glines)

i=0
while count!=0:
    i=i+1
    print(glines[i])
    count=count-1
    time.sleep(0.2)
print("end")

thefile.close()
