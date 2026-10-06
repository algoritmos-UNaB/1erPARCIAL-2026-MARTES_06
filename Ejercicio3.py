class Evolucion: 
    def __init__(self, nombre: str):
        self.nombre = nombre 
        self.siguiente = None

class IteradorPilaEvoluciones:
    def __int__(self, actual: Evolucion):
        self.actual = actual

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        valor = self.actual.nombre
        self.actual = self.actual.siguiente
        return valor

class PilaEvoluciones:
    def __init__(self):
        self.tope = None

    def apilar(self, evolucion: Evolucion):
        evolucion.siguiente = self.tope
        self.tope = evolucion

    def desapilar(self):
        if self.tope  is None:
            return "No hay evoluciones para desapilar."

        desapilado = self.tope
        self.tope = self.tope.siguiente
        desapilado.siguiente = None
        return desapilado

def mostrar_evoluciones(self):
    elementos = []
    actual = self.tope
    while actual is not None:
        elementos.append(actual.nombre)
        actual = actual.siguiente
    for nombre in reversed(elementos):
        print(nombre)

def __iter__(self):
    return IteradorPilaEvoluciones(self.tope)
