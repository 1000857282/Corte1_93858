
def primo():
    num= int(input("Indique la cantidad de numeros:"))
    j = 2; x = 0; n = 2
    print("1")
    while x<= (num-2):
        div = n % j
        if div == 0:
            if n == j:
                print(n, end=",")
                x +=1
            
            j =2
            n+=1
        else:
            j+=1

if __name__ == "__main__":
    primo("")