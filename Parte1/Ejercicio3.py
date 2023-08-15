import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

"""Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta respetando el siguiente formato:
"<num_atleta> - : (<tiempo_llegada> segundos)", donde <num_atleta> es el número del atleta,
 su nombre y <tiempo_llegadad> su tiempo de llegada."""

def imprimir(atletas): 
      for atleta in atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']} segundos)")

"Escribir una función que devuelva el número del atleta que resultó ganador."
def ganador(atletas):
    primero=99.99
    numero=0
    for atleta in atletas:
        if atleta['tiempo_llegada'] < primero:
            primero = atleta['tiempo_llegada']
            numero = atleta['numero']
    return numero

"Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos (nombre, número y tiempo de llegadad)."
def datos_competidor(atletas, num):
    for atleta in atletas:
        if atleta['numero'] == num: 
            return {
                "nombre": atleta['nombre'],
                "numero": atleta['numero'],
                "tiempo_llegada": atleta['tiempo_llegada']
            }


"Utilizar la función anterior para generar y almacenar una lista de atletas"
lista_atletas = generar_lista_de_atletas()
imprimir(lista_atletas)
primero=ganador(lista_atletas)
print(f"El ganador fue el N°: {primero}")
num=int(input("Ingrese el número del competidor del cual desea obtener los datos: "))
datos = datos_competidor(lista_atletas, num)
print(f"Datos del atleta {num}: Nombre: {datos['nombre']}, Tiempo: {datos['tiempo_llegada']} segundos")
