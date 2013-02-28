import sys
import numpy as np
infile = open (sys.argv[1],"r")
rango=[]
frecuencia=[]
lineas= infile.readlines()
for li in lineas:
    a=li.split(' ')
    rango.append(a[0])
    frecuencia.append(a[1])
infile.close()
i=0
j=0
for pos in rango:
    rango[j]=np.log(float(pos))
    j=j+1

for pos in frecuencia:
    frecuencia[i]= np.log(float(pos))
    i=i+1
for pos in rango:
    print pos
for pos in frecuencia:
    print pos
ajuste=np.polyfit(rango, frecuencia, 1)
nombreArchivo = "ajuste_"
nombreArchivo+=sys.argv[1]
outfile=open(nombreArchivo,"w")
outfile.write("pendiente: ")
outfile.write(str(ajuste[0]))
outfile.write('\n')
outfile.write("intercepto: ")
outfile.write(str(ajuste[1]))
outfile.write('\n')
    
