class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None

class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None

    def apilar(self, evo: Evolucion):
        evo.siguiente = self.evoluciones
        self.evoluciones = evo

    def desapilar(self):
        if self.evoluciones is None:
            return 'No se puede desapilar mas'
        ultimo = self.evoluciones
        self.evoluciones = ultimo.siguiente
        return ultimo

    def mostrar_evoluciones(self):
        names = []
        nodo = self.evoluciones
        while nodo is not None:
            names.append(nodo.nombre)
            nodo = nodo.siguiente
        for nombre in reversed(names):
            print(nombre)

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)


class IteradorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        valor = self.actual
        self.actual = self.actual.siguiente
        return valor