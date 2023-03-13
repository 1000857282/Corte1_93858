num = int(input("Cuantos números desea generar de la serie de fibonacci?: "))
x = 0
a = 0
b = 1

for x in range(1,num+1):
    x=x+1
    c = a + b
    a = b
    b = c
    print(a,end=" , ")#para imprimir horizontalmente 
