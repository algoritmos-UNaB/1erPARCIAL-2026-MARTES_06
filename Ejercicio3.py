from Ejercicio2 import PokemonNode

class Evolucion():

    def  __init__(self, nombre:str):
        if type(nombre) != str:
            raise TypeError("El nombre debe ser un string..")
        self.nombre = nombre

class IteredorPilaEvoluciones():
    
    def __init__(self,prim):
        self.actual = prim
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        evolucion = self.actual.nombre
        self.actual = self.actual.sig
        return evolucion

class PilaEvoluciones():
    def __init__(self):
        self.evoluciones = None

    def apilar(self, evolucion:Evolucion):
        self.evoluciones = PokemonNode(evolucion.nombre, self.evoluciones)

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones qye desapilar"
        
        evolucion = self.evoluciones.nombre
        self.evoluciones = self.evoluciones.sig
        return evolucion

    def mostrar_evoluciones(self):
        if self.evoluciones is None:
            return "No hay evoluciones para mostrar,,"
        for evolucion in self.evoluciones:
            print(f"\n{evolucion.nombre}")

    def __iter__(self):
        return IteredorPilaEvoluciones(self.evoluciones)


