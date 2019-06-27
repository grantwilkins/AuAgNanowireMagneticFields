dAng = 0.01

fin = open('STRUCTc.fdf', 'r')
structc = []
for line in fin:
	structc.append(line)

fin.close()
lc1 = structc[2].split('LatticeConstant')
lc2 = lc1[1].split('Ang')
curLC = float(lc2[0])
newLC = curLC + dAng

structOut = open('STRUCNEW.fdf', 'w')
for i in range(len(structc)):
	if(i == 2):
		structOut.write('LatticeConstant 	' + str(newLC) + ' Ang' + "\n")
	else:
		structOut.write(structc[i].strip() + "\n")

structOut.close()	
