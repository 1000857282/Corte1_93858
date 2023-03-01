pfinal = float(input("Ingrese el precio final de su compra: "))
vb= pfinal/(1 + 0.19)
iva = pfinal - vb
VB = round(vb,2)
IVA = round(iva,2)

print(f"El valor del iva agregado es de: {IVA} ")
print(f"El valor bruto del producto es: {VB} ")