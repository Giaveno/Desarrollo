"""Ejercicio 6: Asado"""

invitados=int(input("Ingrese la cantidad de invitados: "))
precio=int(input("Ingrese el precio de 1kg de carne: "))

carne=0.7*invitados
total=carne*precio

print(f"Le debera pedir al carnicero {carne} kg y necesita ${total} para pagar")