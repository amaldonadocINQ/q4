import random as ran
from datetime import *

heroes = ["Link", "Zelda", "Mario", "Luigi"]
def generarNombre(nombre):
    return ran.choice(nombre)
generarNombre(heroes)

clases = ["Guerrero", "Mago", "Herrero", "Elfo"]
def generarClase(clases):
    return ran.choice(clases)
generarClase(clases)

def generarhp ():
    return ran.randint(80, 120)
hprandom = generarhp()

def mostrarFecha ():
    return datetime.now()
fecha = mostrarFecha ()

print("---Generador de Aventuras---")
print ("Fecha: ", fecha)

print("---Heroes Generados---")
print(f"Heroe 1: {generarNombre(heroes)}, Clase:{generarClase(clases)}, HP:{generarhp()}")
print(f"Heroe 2: {generarNombre(heroes)}, Clase:{generarClase(clases)}, HP:{generarhp()}")
print(f"Heroe 3: {generarNombre(heroes)}, Clase:{generarClase(clases)}, HP:{generarhp()}")
