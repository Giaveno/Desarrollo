"""Ejercicio 5: Club deportivo"""

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