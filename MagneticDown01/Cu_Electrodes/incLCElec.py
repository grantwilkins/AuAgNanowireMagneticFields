dAng = 0.01

fdf = open('strucold','r')

struc = []

for line in fdf:
	struc.append(line)

fdf.close()
lineLC1 = struc[2].split('LatticeConstant')
lineLC2 = lineLC1[1].split('Ang')

currentLC = float(lineLC2[0])
newLC = currentLC + dAng

strucOut = open('STRUCnew2.fdf', 'w')
strucOut.write( struc[0].strip() + "\n")
strucOut.write( struc[1].strip() + "\n")
strucOut.write('LatticeConstant		' + str(newLC) + ' Ang' + "\n")
for i in range(3, len(struc)):
	strucOut.write(struc[i].strip() + "\n")

strucOut.close()
