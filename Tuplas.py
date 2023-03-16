def main(a,b,*args,**kwargs,):
    print(a)
    print(b)
    print(args) #imprime las varibales que no defini y que no mencione
    print(kwargs) #imprime las varibales definidas

if __name__=="__main__":
    main(1,2,3,4,5,i=10,j=20)