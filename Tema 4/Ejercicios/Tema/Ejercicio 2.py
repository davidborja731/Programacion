fecha="12/31/20"
fecha2=fecha.split("/")
dia=fecha2[0]
mes=fecha2[1]
año="20"+fecha2[2]
xd="-".join([dia,mes,año])
print(xd)