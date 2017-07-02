firstX=200
firstY=60
f=open("micro.gcode", "w+")
f.write("G90"+"\n"+"G26"+"\n"+"M103"+"\n"+"M207 N1"+"\n")
f.write("G1 X200 Y65 Z0.5 F3000"+"\n")
f.write("G1 X200 Y65 Z0.5 F3000"+"\n")
for i in range(0,20):
    for j in range(0,20):
        temX1=str(firstX+float(i)/1-0.01)
        temY1=str(firstY+float(j)/1-0.01)
        temX2=str(firstX+float(i)/1)
        temY2=str(firstY+float(j)/1)
        f.write("M101""\n")
        f.write("G1 X"+ temX1 + " " + "Y"+ temY1 +" F5000"+ "\n")
        f.write("G1 X"+ temX2 + " " + "Y"+ temY2 +" F50"+ "\n")
        f.write("M103""\n")
    j=0
f.write("G1 Z60"+"\n")
f.write("M113 S0.0"+"\n"+"M140 S0.0"+"\n"+"M04"+"\n")
f.close()

# old  gcode
# f=open("micro.gcode", "w+")
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
