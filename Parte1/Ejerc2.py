"""Ejercicio 2:Promedio de temperaturas"""
temptotal=0
for i in range(5):
    temp=int(input("Ingrese la temperatura: "))
    temptotal=temptotal+temp

promedio=temptotal/5
print(f"El promedio de las temperaturas es de: {promedio}")