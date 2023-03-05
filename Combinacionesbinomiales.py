#Desarrolle un programa  para calcular el número de conbinaciones binomiales que pueden darse en un conjunto de n elementos organizados en r número de muestras sin orden.
n = int(input("Ingrese un número: "))
m = int(input("Ingrese un número: "))

def combinaciones(n,m):
  if m > n:
    return 0
  else: 
    numerador = 1
    for x in range(n, n - m, -1):
      numerador *= x

    denominador = 1
    for x in range(1, m + 1):
      denominador *= x
    return numerador // denominador 