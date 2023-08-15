"""Ejercicio 4:Descuento en el supermercado"""
compra=int(input("Ingrese el valor de la compra: "))
if(compra>3500):
    descuento=(compra*10)/100
    total=compra-descuento
    print(f"El monto a pagar con el descuento del 10% es de {total}")
else:
    print(f"El monto a pagar es de {compra}")