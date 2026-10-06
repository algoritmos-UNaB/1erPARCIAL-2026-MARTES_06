class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = []

    def apilar(self, evolucion: Evolucion):
        self.evoluciones.append(evolucion)

    def desapilar(self):
        if len(self.evoluciones) == 0:
            return "No hay evoluciones para desapilar."

        return self.evoluciones.pop()

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