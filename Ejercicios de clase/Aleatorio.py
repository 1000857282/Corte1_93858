import random as rand

for i in range(0,5):
    numero = rand.randint(10,20)
    real = round(rand.uniform(10,20),2)
    letra = rand.choice("murcielago")
    print(numero, end= " ")
    print(real, end= " ")
    print(letra,  " \n ")