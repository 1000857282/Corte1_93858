
def digitos():
    n = int(input("Ingrese uun numero: "))
    digit_equal = 0
    digit_different = 0
    while n != 0:
        x = (n// 10)
        dig = n-(x*10)
        n = x
        if dig ==5:
            digit_equal += 1
            print("salto")
        else:
            print(dig)
            digit_different += 1
    print(f"Iguales a 5 {digit_equal} ")
    print(f"diferentes a 5  {digit_different} ")
    print(f"números de digitos {digit_equal+digit_different} ")

#codigo no funciono pero lo hzo el profesor

if __name__ == "__main__":
    digitos("")