class Evolucion:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.siguiente = None

class PilaEvoluciones:
    def __init__ (self):
        self.tope = None

    def apilar (self, evolucion):
        evolucion.siguiente = self.tope
        self.tope = evolucion

    def desapilar (self):
        if self.tope is None:
            return "No hay evoluciones para desapilar"
        else:
            retirar = self.tope
            self.tope = self.tope.siguiente
            return retirar
    
    def mostrar_evoluciones (self):
        evolucion_actual = self.tope
        while evolucion_actual is not None:
            print (evolucion_actual.nombre)
            evolucion_actual = evolucion_actual.siguiente
    
    def __iter__ (self):
        return IteradorPilaEvoluciones(self.tope)


class IteradorPilaEvoluciones:
    def __init__ (self, actual)
        self.actual = actual

    def __next__ (self):
        if self.actual is None:
            raise StopIteration
        act = self.actual
        self.actual = self.actual.siguiente
        return act