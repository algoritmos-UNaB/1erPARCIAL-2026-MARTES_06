class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = None

    def apilar(self, evolucion):
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones que desapilar"
        nodo = self.evoluciones
        self.evoluciones = nodo.siguiente
        nodo.siguiente = None
        return nodo

    def mostrar_evoluciones(self):
        nombres = []
        for evolucion in self:
            nombres.append(evolucion.nombre)
        for nombre in reversed(nombres):
            print(nombre)

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones:

    def __init__(self, evoluciones):
        self.actual = evoluciones

    def __iter__(self):
        return self    

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        valor = self.actual
        self.actual = self.actual.siguiente
        return valor