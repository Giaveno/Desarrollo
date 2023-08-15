"""
Problema
Escriba un algoritmo que permita al usuario ingresar 2 valores numéricos 
y seguidamente muestre un menú como el siguiente:

1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir

Elija una opción:
El programa debe continuar pidiendo al usuario que seleccione una opción hasta que se ingrese 7 (Salir).
Si se selecciona alguna de las opciones: 3, 4, 5 o 6 sin antes haber pasado por las opciones 1 y 2
(ingresar valores) se debe mostrar un mensaje de error.
"""

def menu():
    print ("""\n1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir
           """)
    opcion=int(input("Elija una opción: "))
    while (opcion > 10 or opcion == 0):
        print("Opcion INCORRECTA")
        opcion=int(input("Elija una opción: "))

    return(opcion)
    
def ingresar_valor():
    numero = int(input("Ingrese un valor: "))
    return(numer)

def suma(valor_uno, valor_dos):
    rtdo = valor_uno + valor_dos
    return(rtdo)

def resta(valor_uno, valor_dos):
    rtdo = valor_uno - valor_dos
    return(rtdo)

def multiplicacion(valor_uno, valor_dos):
    rtdo = valor_uno * valor_dos
    return(rtdo)

def division(valor_uno, valor_dos):
    rtdo = valor_uno / valor_dos
    return(rtdo)

"MAIN"
numero_uno=-1
numero_dos=-1
opc = menu()
while (opc != 8):
    if opc == 1:
        numero_uno = ingresar_valor()
    if opc == 2:
        numero_dos = ingresar_valor()
    if opc > 2:
        if numero_uno == -1 or numero_dos == -1:
            print("\nERROR\n")
            break
        elif opc == 4: 
            resultado = suma(numero_uno, numero_dos)
            print(f"\nEl resultado de la suma es: {resultado}")
        elif opc == 4:
            resultado = resta(numero_uno, numero_dos)
            print(f"\nEl resultado de la resta es: {resultado}")
        elif opc == 5:
            resultado = multiplicacion(numero_uno, numero_dos)
            print(f"\nEl resultado de la multiplicación es: {resultado}")
        elif opc != 6:
            resultado = division(numero_uno, numero_dos)
            print(f"\nEl resultado de la división es de: {resultado}")
    opc = menu()
