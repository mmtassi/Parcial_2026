from abc import ABC, abstractmethod


class SuperPlomero:
    def __init__(self, vidas):
        self.vidas = vidas
        self.puntos = 0
        self.estado = Pequeno()

    def recibir_danio(self):
        self.estado.recibir_danio(self)

    def obtener_objeto(self, objeto):
        objeto.aplicar(self)

    def saltar_sobre(self, enemigo):
        enemigo.recibir_salto(self)

    def lanzar_bola_fuego(self, enemigo):
        if self.estado.puede_lanzar_fuego():
            enemigo.recibir_fuego(self)
        else:
            raise ValueError("No podes tirar fuego")

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad
        if self.puntos >= 1000:
            self.vidas +=1
            self.puntos = 0

    def perder_vida(self):
        self.vidas -= 1

        if self.vidas == 0:
            raise ValueError("Juego terminado")


class EstadoPlomero(ABC):

    @abstractmethod
    def recibir_danio(self, plomero):
        pass

    @abstractmethod
    def obtener_hongo(self, plomero):
        pass

    def puede_lanzar_fuego(self):
        return False


class Pequeno(EstadoPlomero):

    def recibir_danio(self, plomero):
        plomero.perder_vida()

    def obtener_hongo(self, plomero):
        plomero.estado = Grande()


class Grande(EstadoPlomero):

    def recibir_danio(self, plomero):
        plomero.estado = Pequeno()

    def obtener_hongo(self, plomero):
        plomero.sumar_puntos(100)


class Fuego(EstadoPlomero):

    def recibir_danio(self, plomero):
        plomero.estado = Grande()

    def obtener_hongo(self, plomero):
        plomero.sumar_puntos(100)

    def puede_lanzar_fuego(self):
        return True


class ObjetoEspecial(ABC):

    @abstractmethod
    def aplicar(self, plomero):
        pass


class Moneda(ObjetoEspecial):

    def aplicar(self, plomero):
        plomero.sumar_puntos(50)


class HongoMagico(ObjetoEspecial):

    def aplicar(self, plomero):
        plomero.estado.obtener_hongo(plomero)


class FlorFuego(ObjetoEspecial):

    def aplicar(self, plomero):
        plomero.estado = Fuego()

class CajaMisterio:
    def __init__(self, contenido):
        self._contenido = contenido

    def tocar(self, plomero):
        if self._contenido is None:
            raise ValueError("La caja ya fueusada")

        plomero.obtener_objeto(self._contenido)
        self._contenido = None


class Enemigo(ABC):
    def __init__(self, puntos):
        self._puntos = puntos
        self._derrotado = False

    @abstractmethod
    def recibir_salto(self, plomero):
        pass

    def recibir_fuego(self, plomero):
        self.derrotar(plomero)

    def atacar(self, plomero):
        plomero.perder_vida()

    def derrotar(self, plomero):
        if not self._derrotado:
            self._derrotado = True
            plomero.sumar_puntos(self._puntos)

    def derrotado(self):
        return self._derrotado


class Caminante(Enemigo):
    def __init__(self):
        super().__init__(100)

    def recibir_salto(self, plomero):
        self.derrotar(plomero)


class Tortuga(Enemigo):
    def __init__(self):
        super().__init__(200)
        self._saltos_recibidos = 0
        self._en_caparazon = False

    def recibir_salto(self, plomero):
        self._saltos_recibidos += 1
        self._en_caparazon = True
        if self._saltos_recibidos == 2:
            self.derrotar(plomero)


class Fantasma(Enemigo):
    def __init__(self):
        super().__init__(300)

    def recibir_salto(self, plomero):
        pass


class Nivel:
    def __init__(self):
        self._enemigos = []
        self._objetos = []
        self._cajas = []

    def agregar_enemigo(self, enemigo):
        self._enemigos.append(enemigo)

    def agregar_objeto(self, objeto):
        self._objetos.append(objeto)

    def agregar_caja(self, caja):
        self._cajas.append(caja)

    def completado(self):
        for enemigo in self._enemigos:
            if not enemigo.derrotado():
                return False
        return True









