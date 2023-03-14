nota1 = float(input("Ingrese el valor de la nota 1: "))
nota2 = float(input("Ingrese el valor de la nota 2: "))
nota3 = float(input("Ingrese el valor de la nota 3: "))
promedio =  (nota1 + nota2 + nota3)/3
if promedio > 3.0:
  print("Aprobo")
else:
  print("No aprobo")
  
print(f"El promedio de notas del estudiante es: {promedio} ")