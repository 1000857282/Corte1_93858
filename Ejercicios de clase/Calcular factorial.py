#Realice un Programa que cálcule el número factorial de un número seleccionado por el usuario.
print("Escoja uno de los siguientes números para cálcular su factorial : \n") 
print(" 8 ")
print(" 20 ")
print(" 12 ")

opc = int(input("Escoja una opción: "))
factorial = 1
if opc==8:
  for n in range(1,(opc+1)):
    factorial = factorial *n
  print(f"el factorial de {opc}, es: {factorial} ")
elif opc==20:
  for n in range(1,(opc+1)):
    factorial = factorial *n
  print(f"el factorial de {opc}, es: {factorial} ")
elif opc==12:
  for n in range(1,(opc+1)):
    factorial = factorial *n
  print(f"el factorial de {opc}, es: {factorial} ")
  
else:
  print("la opción que usted eligio, no está dentro de las opciones dadas")
