import pytest
from solucion.clases import *

#requerimiento 1
def test_estado_inicial():
    plomero = SuperPlomero(3)

    plomero.recibir_danio()

    # pequeño pierde una vida al recibir danio
    assert plomero.vidas == 2

#requerimiento 2
def test_pequeno_a_grande():
    plomero = SuperPlomero(3)
    hongo = HongoMagico()

    plomero.obtener_objeto(hongo)
    plomero.recibir_danio()

    # no deberia pasar a pequeno
    assert plomero.vidas == 3

#requerimiento 3
def test_grande_con_hongo():
    plomero = SuperPlomero(3)
    hongo = HongoMagico()

    plomero.obtener_objeto(hongo)
    plomero.obtener_objeto(hongo)

    assert plomero.puntos == 100


#requerimiento 4
def test_grande_pasa_a_pequeno():
    plomero = SuperPlomero(3)
    hongo = HongoMagico()

    plomero.obtener_objeto(hongo)
    plomero.recibir_danio()
    assert plomero.vidas == 3
    # cuando pasa a pequeno y recibe danio danio le saca vida
    plomero.recibir_danio()

    assert plomero.vidas == 2


#requerimiento 5
def test_fuego_pasa_a_grande():
    plomero = SuperPlomero(3)
    flor = FlorFuego()

    plomero.obtener_objeto(flor)
    plomero.recibir_danio()
    plomero.recibir_danio()

    assert plomero.vidas == 3

    plomero.recibir_danio()

    assert plomero.vidas == 2

#requerimiento 15
def test_caja_con_hongo():
    plomero = SuperPlomero(3)
    hongo = HongoMagico()
    caja = CajaMisterio(hongo)
    caminante = Caminante()

    caja.tocar(plomero)
    caminante.atacar(plomero)
    plomero.recibir_danio()
    #como quedo pequeno, otro danio le saca una vida
    assert plomero.vidas == 2

# requetimiento 16
def test_fuego_mata_fantasma_y_gana_300_puntos():
    plomero = SuperPlomero(3)
    flor = FlorFuego()
    fantasma = Fantasma()

    plomero.obtener_objeto(flor)
    plomero.lanzar_bola_fuego(fantasma)

    assert fantasma.derrotado()
    assert plomero.puntos == 300


# requerimiento 17
def test_caja_usada_no_entrega_de_nuevo():
    plomero = SuperPlomero(3)
    moneda = Moneda()
    caja = CajaMisterio(moneda)

    caja.tocar(plomero)

    assert caja._contenido == None


# requerimiento 18
def test_perder_ultima_vida_interrumpe_juego():
    plomero = SuperPlomero(1)

    with pytest.raises(ValueError):
        plomero.recibir_danio()

    assert plomero.vidas == 0
