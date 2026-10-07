class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Nodo:
    def __init__(self):
        self.evolucion = evolucion
        self.siguiente = None

class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = None


    def apilar(self, evolucion: Evolucion):
        nuevo_nodo = Nodo(evolucion)
        nuevo_nodo.siguiente = self.evoluciones
        self.evoluciones = nuevo_nodo

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar."

         evolucion = self.evoluciones.evolucion
         self.evoluciones = self.evoluciones.siguiente

         return evolucion

     def mostrar_evoluciones(self):
        actual = self.evoluciones

        while actual is not None:
            print(actual.evolucion)
            actual = actual.siguiente
        
     def __iter__(self):
        return ItadorPilaEvoluciones(self.evoluciones)

class ItadorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        evolucion = self.actual.evolucion
        self.actual = self.actual.siguiente

        return evolucion 