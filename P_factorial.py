import Factorial as f
#from Factorial impor fcn_factorial as f --> es otra forma de importar

def main():
    n = int(input("Ingrese el numero de grupos: "))
    m = int(input("Ingrese el numero de muestras: "))
    resultado = ((f(n))/(f(m)*f(n-m)))
    print(f"El numero de combinaciones posibles es: {resultado}")

    result =(f.fcn_factorial)


if __name__=="__main__":
    main()