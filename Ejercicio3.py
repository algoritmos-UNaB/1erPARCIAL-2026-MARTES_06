class Nodo:
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Evolucion:
    
    def __init__(self, nombre: str):
        self.nombre = nombre

class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = []

    def apilar(self, evolucion):
        self.evoluciones.append(evolucion)

    def desapilar(self):
        if self.evoluciones == 0:
            return None
        return self.evoluciones.pop

    def mostrar_evoluciones(self):
        for evolucion in self:
            print(evolucion.nombre)

class IteradorPilaEvoluciones:

    def __init__(self, primero):
        self.actual = primero
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
    
        evolucion = self.actual.dato
        self.actual = self.actual.siguiente

        return evolucion

        1