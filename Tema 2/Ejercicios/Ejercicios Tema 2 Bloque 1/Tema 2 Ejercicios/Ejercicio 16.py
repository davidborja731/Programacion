hora=int(input("Dame una hora: "))
minutos=int(input("Dame un minuto: "))
segundos=int(input("Dame unos segundos: "))
second=segundos+1
if second==59+1 and minutos==59:
    xd=hora+1
    print(xd,":00:00")
if second<59+1 and minutos<59:
    xd3=segundos+1
    print(hora,":",minutos,":",xd3)
if second==59+1 and minutos<59:
    xd4=minutos+1
    print(hora,":",xd4,":00")