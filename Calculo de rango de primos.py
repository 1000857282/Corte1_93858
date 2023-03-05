#Realice un programa que solicite un número al usuario, después indique si es primo o no; además imprima los números primos hasta este número.
num = int(input("Ingrese un número: "))
primos = []
if num > 1:
  cont = 0 #Contador aqui es cero, cuenta la cantidad de ceros
  n = 2
 
  while n < num and cont==0:#mientras el n sea menor a el num ingresado y el contador sea igual a cero
    resto = num % n
    #print(f"{num} % {n} = {resto} ")

    if resto == 0:
      cont+=1
      
    n+=1
  for n in range(2,num+1):
    if n % 2 != 0:
        primos.append(int(n))
  print(primos)

  if cont==0:
      print("El numero que usted ingreso es primo")
  else:
      print("el número que usted ingreso no es primo")
else:
  print("el numero que usted ingreso no es primo")