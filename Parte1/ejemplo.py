
"""
https://github.com/pabratte/desarrollo_de_software/wiki/Ejercios-de-Python-(parte-1)

Ejercicio 1:Suma de numeros
a = int(input("Ingrese el primer valor: "))    
b = int(input("Ingrese el segundo valor: "))
c = int(input("Ingrese el tercer valor: "))

d = a+b+c
print("La suma de los valores {}, {} y {} es {}".format(a,b,c,d))
print(f"La suma de los valores {a}, {b}, {c} es {d}")"""


"""Ejercicio 2:Promedio de temperaturas
temptotal=0
for i in range(5):
    temp=int(input("Ingrese la temperatura: "))
    temptotal=temptotal+temp

promedio=temptotal/5
print(f"El promedio de las temperaturas es de: {promedio}")
"""

"""Ejercicio 3: Bitcoins a pesos
bitcoins = int(input("Ingrese la cantidad de bitcoins: "))
peso=8260873.61

result=bitcoins*peso

print(f"La cantidad de pesos que equivalen a {bitcoins} Bitcoins es de ${result}")"""

"""Ejercicio 4:Descuento en el supermercado
compra=int(input("Ingrese el valor de la compra: "))
if(compra>3500):
    descuento=(compra*10)/100
    total=compra-descuento
    print(f"El monto a pagar con el descuento del 10% es de {total}")
else:
    print(f"El monto a pagar es de {compra}")"""


"""Ejercicio 5: Club deportivo

nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))

if(edad>=13 and edad<15):
    print(f"El nombre de la categoria es INFANTILES")
elif(edad>=15 and edad<17):
    print(f"El nombre de la categoria es CADETES")
elif(edad>=17 and edad<19):
    print(f"El nombre de la categoria es JUVENILES")
elif(edad>=19):
    print(f"El nombre de la categoria es MAYORES")
    """

"""Ejercicio 6: Asado

invitados=int(input("Ingrese la cantidad de invitados: "))
precio=int(input("Ingrese el precio de 1kg de carne: "))

carne=0.7*invitados
total=carne*precio

print(f"Le debera pedir al carnicero {carne} kg y necesita ${total} para pagar")"""