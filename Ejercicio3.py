class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Nodo:
    def __init__(self, evolucion):
        self.evolucion = evolucion
        self.siguiente = None

class PilaEvoluciones:
    def __init__(self):
        self.tope = None

    def apilar(self, evolucion):
        
        nuevo = Nodo(evolucion)
        nuevo.siguiente= self.tope
        self.tope = nuevo
        
    def desapilar(self):

        if self.tope == None:
            return "No hay evolucion para desapilar"   

        evolucion = self.tope.evolucion
        self.tope = self.tope.siguiente

        return evolucion

    def mostrar_evoluciones(self):
        for evolucion in self:
            print(evolucion) 

    def __iter__(self):
        return IteradorPilaEvoluciones(self.tope)  

class IteradorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual

    def __next__(self):

        if self.actual == None:
            raise StopIteration

        evolucion = self.actual.evolucion  
        self.actual = self.actual.siguiente

        return evolucion