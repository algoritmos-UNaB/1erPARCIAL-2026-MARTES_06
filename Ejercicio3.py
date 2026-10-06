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
            return "No hay evoluciones para desapilar"
        evolucion_removida = self.evoluciones
        self.evoluciones = self.evoluciones.siguiente
        return evolucion_removida

    def mostrar_evoluciones(self):
        actual = self.evoluciones
        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

    
class IteradorPilaEvoluciones:
    def __init__(self, tope):
        self.actual = tope


    def __next__(self):
        if self.actual is None:
            raise StopIteration("No hay mas elementos en la pila")


        dato_actual = self.actual
        self.actual = self.actual.siguiente
        return dato_actual