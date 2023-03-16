cadena ="Hola mundo!"
print(cadena[6])
print(len(cadena))

texto= " " #imprimir uno por uno

#accesiendo con for
for i in cadena:
    texto+= str(f" {i},") #str: i8mprime como texto, osea horizontal, si le quito la coma imprime sin la coma
    print(texto)

#accediendo con un while
contador = 0
texto2 = " "
while contador < len(cadena):
    texto2+= str(f"{cadena[contador]}, ")
    contador+=1
print(texto2)
