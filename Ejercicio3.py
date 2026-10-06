# Ejercicio 3: Pila enlazada + iterador

class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombreself.siguiente = None

class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None

    def apilar(self, evolucion):
        evolucion.siguiente = self.evoluciones 
        self.evoluciones = evolucion

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar."
        tope = self.evoluciones
        self.evoluciones = tope.siguiente
        tope.siguiente = None
        return tope

    def mostrar_evoluciones(self):
        nombres = [evo.nombre for evo in self]
        for nombre in reversed(nombres):
            print(nombre)

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones:
    def __init__(self, tope):
        self.actual = tope

    def __next__(self):
        if self.actual is None:
            raise StopIterartion
        valor = self.actual
        self.actual = self.actual.siguiente
        return valor