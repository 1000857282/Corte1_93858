a = float(input("Ingrese el valor del lado a : "))
b = float(input("Ingrese el valor del lado b : "))
c = float(input("Ingrese el valor del lado c : "))
if a == b and  b == c : #3 lados iguales
  print("Es un triángulo equilatero")
elif a == b and b ==c or a != c or b != c and a != b: #2 lados iguales
  print("Es un triángulo isósceles")
elif a != b and b != c: #Ningun lado igual
  print("Es un triángulo escaleno")         