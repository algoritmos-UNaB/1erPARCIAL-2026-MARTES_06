#Sistemas de Evoluciones de Pokémon

class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre

class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = []

    def apilar(self,evolucion):
        self.evoluciones.append(evolucion)
    
    def desapilar(self):
        if self.evoluciones:
            return self.evoluciones.pop()
        else:
            return "No hay evoluciones para desapilar"

    def mostrar_evoluciones(self):
        for evolucion in self.evoluciones:
            print(evolucion.nombre)
        
    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones:
    def __init__(self, evoluciones):
        self.evoluciones = evoluciones
        self.actual = len(evoluciones) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual < 0:
            raise StopIteration
    
    evolucion = self.evoluciones[self.actual]
    self.actual -= 1
    return evolucion