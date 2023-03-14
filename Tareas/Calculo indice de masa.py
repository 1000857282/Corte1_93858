P = float(input("Ingrese su peso en kg: "))
E = float(input("Ingrese su estatura en m: "))
IMC = P/E**2
imc= round(IMC,2)
print(f"Su indice de masa corporal es de: {imc} ")