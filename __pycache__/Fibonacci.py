num = int(input("Cuantos números desea generar de la serie de fibonacci?: "))
n = 1

for x in range(0,num+1):
    num+=1
    n+=1

    fibonacci = num + n

    a = fibonacci + (n+1)

    print(fibonacci)
   


