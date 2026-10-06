# Ejercicio 3: Sistema de Evoluciones de Pokémon

class Evolucion:

    def __init__(self, nombre: str):
        self.nombre = nombre

class IteradorPilaEvoluciones():
    def __init__(self, evoluciones):
        self.evoluciones = evoluciones

        if len(evoluciones) > 0:
            self.actual = evoluciones[0]
        else:
            self.actual = None

        self.posicion = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.posicion >= len(self.evoluciones):
            raise StopIteration("Se llegó la final de la lista")
        self.actual = self.evoluciones[self.posicion]
        self.posicion = self.posicion + 1
        return self.actual

class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = []

    def apilar(self, evolucion: Evolucion):
        self.evolucion.append(evolucion)
    
    def desapilar(self):
        if len(self.evoluciones) == 0:
            print("No hay evoluciones para desapilar.")

        return self.evoluciones.pop()

    def mostrar_evoluciones(self):
        for evolucion in self:
            print(evolucion.nombre)

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)