class Evolucion():
    def __init__ (self,nombre):
    self.nombre=nombre
    self.siguiente= None

class PilaEvoluciones():
    def __init__(self):
    self.evoluciones= None

    
    def apilar(self,evolucion):
        evolucion.siguiente=self.evoluciones
        self.evoluciones=evolucion
    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar"
        evolucion=self.evoluciones
        self.evoluciones=evolucion.siguiente
        return evolucion
    def mostrar_evoluciones(self):
        actual= self.evoluciones
        nombres=[]
        for evolucion in self:
            nombres.append(evolucion.nombre)
        for nombre in reversed(nombres):
            print(nombre)
    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones():
    def __init__(self,actual):
        self.actual=actual
    def __iter__(self):
        return self
    def __next__(self):
        if self.actual is None:
            raise StopInteration
        evolucion= self.actual
        self.actual=self.actual.siguiente
        return evolucion