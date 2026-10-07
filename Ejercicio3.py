class Evolucion:
     def __init__(self, nombre):
        self.nombre = nombre
class PIlaEvoluciones:
     def __init__(self):
        self.evoluciones = []
     
    def apilar(self, evolucion):
        self.evoluciones.append(evolucion)
    def desapilar(self):
        if len(self.evoluciones) == 0:
            return "No hay evoluciones para desapilar"
        return self.evoluciones.pop()
    def mostrar_evoluciones(self):
        for evolucion in self:
            print(evolucion.nombre)
    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)
class IteradorPilaEvoluciones:
    def __init__(self, evoluciones):
        self.evoluciones = evoluciones
        self.actual = 0
    def __next__(self):
        if self.actual >= 1 len(self.evoluciones):
            raise StopIteration
        evolucion = self.evoluciones[self.actual]
        self.actual += 1
        return evolucion