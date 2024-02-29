edad=int(input("indica tu edad "))
peso=int(input("indica tu peso "))
ritmo=int(input("indica tu ritmo cardiaco "))
plaquetas=int(input("indica tus plaquetas "))
if edad>=18 and edad<=65:
    xd=2
else:
     print("No eres compatible")
if xd==2:
     if peso >= 55:
          xd2=3
else:
    print("No eres compatible")       
if xd2==3:
     if ritmo>=55 and ritmo<110:
          xd3=4
else:
     print("No eres compatible")
if xd3 == 4:
     if plaquetas >= 150000:
          print("Eres compatible")
else:
     print("No eres compatible")