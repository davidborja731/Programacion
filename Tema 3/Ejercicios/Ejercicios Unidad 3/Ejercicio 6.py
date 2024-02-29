print("Con isalpha()")
nombre=input("Dime una frase ")
xd=nombre.isalpha()
if xd == True:
    print("Caracteres alfabeticos")
if xd == False:
    print("hay caracteres no alfabeticos") 
print("-------------------------------------")
print("Sin isalpha()")
nombre2=input("Dime una frase ")
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
for i in nombre2: 
    if i in ALPHABET:
        code = True
        pass
    else:
        print("No son todos alfabeticos")
        code=False
        break
if code == True:
    print("Son todos alfabeticos")
