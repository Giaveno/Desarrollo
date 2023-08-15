"""
Funciones para operar sobre una lista
Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random).
Luego:

Muestre la lista
El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista
son mayores a dicho valor, para eso debe utilizar una función. La función debe recibir 
como argumentos la lista y un entero, y debe retornar la cantidad de valores
de la lista mayores a dicho entero.
Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.
"""
import random
lista=[]
listaAux=[]

def generar():
    for i in range(10):
        num=random.randint(1, 20)
        lista.append(num)

def mostrar():
    print("La lista generada es: ")
    while(len(lista) != 0):
        valor=lista.pop()
        listaAux.append(valor)
        print(f"- {valor} -")

def mayores():
    cant=0
    while(len(listaAux) != 0):
        valor=listaAux.pop()
        lista.append(valor)
        if valor > entero:
            cant+=1
    return(cant)

def promedio():
    total=0
    while(len(lista) != 0):
        valor=lista.pop()
        listaAux.append(valor)
        total+=valor
    prom = total/20
    return(prom)

def buscar():
    mayor=0
    menor=21
    while(len(listaAux) != 0):
        valor=listaAux.pop()
        if valor > mayor:
            mayor=valor
        if valor < menor:
            menor=valor
    return(mayor, menor)

generar()
mostrar()
entero=int(input("Ingrese un valor: "))
cantidad = mayores()
print(f"La cantidad de valores mayores a {entero} sobre la lista es: {cantidad}")
prom = promedio()
print(f"El promedio de los valores generados es de: {prom}")
(may, men)=buscar()
print(f"El mayor generado es {may} y el menor es {men}")