n = input("Ingrese un numero: ")

dimension =  len(n)
contador=0
#print(dimension,type(n))
#if dimension < 2 and dimension > 8
if 2 < dimension < 8:
    #pass
    for i in n:
        #if int(i) == 5: #ambos enteros
        if i == "5": # o ambos en str
            print("salto")
            contador+=1
        else:
            print(i)
    print(f"numeros iguales a 5:  {contador}")
    print(f"numeros diferernte de 5: {dimension - contador} ")
    print(f"Total de digitos:  {dimension}")


else:
    print("Error, fuiera de rango")
