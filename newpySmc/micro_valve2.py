firstX=195
firstY=45
f=open("micro2.gcode", "w+")
f.write("G90"+"\n")
f.write("G1 X205 Y45 Z100 F3000"+"\n")
f.write("G1 Z5 F300"+"\n")
for i in range(0,20):
    for j in range(0,20):
        temX1=str(firstX+float(i)/1-0.01)
        temY1=str(firstY+float(j)/1-0.01)
        temX2=str(firstX+float(i)/1)
        temY2=str(firstY+float(j)/1)
        f.write("M101""\n")
    #    f.write("G1 X"+ temX1 + " " + "Y"+ temY1 +" F5000"+ "\n")
        f.write("G1 X"+ temX2 + " " + "Y"+ temY2 +" U0 F5000"+ "\n")
        f.write("G1 X"+ temX2 + " " + "Y"+ temY2 +" U100 F50"+ "\n")
        f.write("M103""\n")
    j=0
f.write("G1 Z60"+"\n")
f.write("M04"+"\n")
f.close()
