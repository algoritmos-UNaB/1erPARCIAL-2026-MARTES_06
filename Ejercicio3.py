
class Evolucion:
    def __init__(self, nombre):
        self.nombre=nombre
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
class Pila_Evolutiva:
    def__init__(self):
        self.evoluciones=None
    def apilar(self, evolucion):
        nuevo=Nodo(evolucion)
        nuevo.siguiente=self.evoluciones
        self.evoluciones = nuevo
    def desapilar(self):
        if self.evoluciones is None:
            return 'No hay evoluciones inferiores para desapilar'
        evolucion=self.evoluciones.dato
        self.evoluciones=self.evoluciones.siguiente
        return evolucion
    def __iter__(self):
        return Iterador_Pila_Evolutiva(self.evoluciones)
class Iterador_Pila_Evolutiva:
    def __init__(self,actual):
        self.actual=actual
    def __next__(self):
        if self.actual is None
            raise StopIteration
        evolucion=self.actual.dato
        self.actual=self.actual.siguiente
        retun evolucion
        #