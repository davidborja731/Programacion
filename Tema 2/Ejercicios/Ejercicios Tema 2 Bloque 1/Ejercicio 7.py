super1=int(input("Dime un año: "))
if super1%4 == 0:
    if super1%100:
        if super1%400:
            print("Es un año bisisesto")
else:
    print("No es un año bisisesto")