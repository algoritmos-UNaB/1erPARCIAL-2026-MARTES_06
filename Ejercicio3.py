class Evolucion:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.siguiente = None

class PilaEvoluciones:
    def __init__(self):
        self.tope = None

    def apilar(self, evolucion: Evolucion):
        evolucion.siguiente = self.tope
        self.tope = evolucion

    def desapilar(self):
        if self.tope is None:
            return "No hay evoluciones para desapilar"
        eliminada = self.tope
        self.tope = eliminada.siguiente
        eliminada.siguiente = None
        return eliminada

    def mostrar_evoluciones(self):
        nombres = [evo.nombre for evo in self]
        for nombre in reversed(nombres):
            print(nombre)
    
    def __iter__(self):
        return IteradorPilaEvoluciones(self.tope)

class IteradorPilaEvoluciones:
    def __init__(self, tope: Evolucion):
        self.actual = tope

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        valor = self.actual
        self.actual = self.actual.siguiente
        return valor