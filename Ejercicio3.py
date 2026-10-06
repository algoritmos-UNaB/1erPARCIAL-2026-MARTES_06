class Evolucion:
    def __init__(self, nombre:str,):
        self.nombre = nombre
        self.siguiente_evolucion = None

class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = None

    def apilar (self, evolucion:Evolucion):
        evolucion.siguiente_evolucion = self.evoluciones
        self.evoluciones = evolucion

    def desapilar (self):
        if self.evoluciones is None:
            return("no hay para desapilar")
        else:
            desapilada = self.evoluciones
            self.evoluciones = desapilada.siguiente_evolucion
            return desapilada

    def mostrar_evoluciones(self):
        actual = self.evoluciones
        while actual != None:
            print(actual.nombre)
            actual = actual.siguiente_evolucion

    def __iter__(self):
        return 

class IteradorPilaEvoluciones:
    def __init__(self, nodo):
        self.actual = nodo