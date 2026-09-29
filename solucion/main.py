from solucion.clases import *

print("requerimiento 6")
plomero1 = SuperPlomero(3)
hongo1 = HongoMagico()
caja1 = CajaMisterio(hongo1)

caja1.tocar(plomero1)
try:
    caja1.tocar(plomero1)
except ValueError as error:
    print(error)

print("\nrequerimiento 7")
plomero2 = SuperPlomero(3)
caminante = Caminante()
nivel = Nivel()
nivel.agregar_enemigo(caminante)

caminante.recibir_salto(plomero2)
print(caminante.derrotado())

print("\nrequerimiento 8")
plomero3 = SuperPlomero(3)
tortuga = Tortuga()
tortuga.recibir_salto(plomero3)
print(tortuga.derrotado())
print(tortuga._en_caparazon)

print("\nrequerimiento 9")
plomero4 = SuperPlomero(3)
tortuga1 = Tortuga()
tortuga1.recibir_salto(plomero4)
print(tortuga1.derrotado())
tortuga1.recibir_salto(plomero4)
print(tortuga1.derrotado())

print("\nrequerimiento 10")
plomero5 = SuperPlomero(3)
fantasma = Fantasma()
fantasma.recibir_salto(plomero5)
print(fantasma.derrotado())

print("\nrequerimiento 11")
plomero6 = SuperPlomero(3)
fantasma1 = Fantasma()
fantasma1.recibir_fuego(plomero6)
print(fantasma1.derrotado())

print("\nrequerimiento 12")
plomero7 = SuperPlomero(3)
tortuga2 = Tortuga()
try:
    plomero7.lanzar_bola_fuego(tortuga2)
except ValueError as error:
    print(error)

print("\nrequerimiento 13")
plomero8 = SuperPlomero(3)
caminante2 = Caminante()
print(plomero8.puntos)
caminante2.recibir_salto(plomero8)
print(plomero8.puntos)

print("\nrequerimiento14")
plomero9 = SuperPlomero(3)
nivel = Nivel()

caminante3 = Caminante()
caminante4 = Caminante()

nivel.agregar_enemigo(caminante3)
nivel.agregar_enemigo(caminante4)

print(nivel.completado())

plomero9.saltar_sobre(caminante3)
plomero9.saltar_sobre(caminante4)

print(nivel.completado())