#Punto del parcial
def fibonacci():
    n = int(input("Ingrese la cantidad de numeros que quiere vicualizar"))
    a = 0;  b=1
    print(a)
    print(b)
    for i in range(n-2):
        c = a+b
        a = b
        b = c
        print(c)

if __name__ == "__main__":
    fibonacci("")