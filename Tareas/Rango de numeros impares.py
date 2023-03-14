#Realice un programa que pida al usuario un número entero positivo y después imprima en pantalla todos los números impares desde el uno hasta dicho número separado por comas. 

num = int(input("Ingrese un número entero positivo: "))
impares = []
for n in range(1, num):
    if n % 2 != 0:
        impares.append(int(n))

print(impares)