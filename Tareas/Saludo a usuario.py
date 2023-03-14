#Desarrolle una función llamada saludo, en donde se solicite el nombre al usuario y cada vez que se invoque dicha función, se imprima por pantalla "Hola <Nombre_Usuario>".
nombre = input("Ingrese su nombre: ")

def Saludo(nombre):
  print(f"Hola  {nombre} ")
imprimir=Saludo
imprimir(nombre)