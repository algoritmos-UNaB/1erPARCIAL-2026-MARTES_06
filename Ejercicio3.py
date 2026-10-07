class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = []

    def apillar(self, evolucion: Evolucion):
        self.evoluciones.append(evolucion)

    def desapilar(self):
        if len(self.evoluciones) == 0:
            return "este pokemon no evoluciono"

    def mostrar_evoluciones(self):
        print ("Evoluciones:")

        for evolucion in self:
            print (evolucion)
    
    def __iter__(self):
        return IteradorPilaEvoluciones

class IteradorPilaEvoluciones:
    def __init__(self, pila)
        self.pila = pilla
        self.actual = len(PilaEvoluciones) - 1
    
    def __inter__(self):
        return self
    
    def __next__(self):
        if self.actual < 0:
        raise StopIteration

        evolucion = self.pila.evoluciones[self.actual]

        self.actual -= 1

        return evolucion

