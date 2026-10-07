class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.siguiente = None 

    def __str__(self):
        return self.nombre


class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None 

    def esta_vacia(self) -> bool:
        return self.evoluciones is None

    def apilar(self, evolucion: Evolucion):
        
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion

    def desapilar(self):
        if self.esta_vacia():
            return "No hay evoluciones para desapilar."
        tope = self.evoluciones
        self.evoluciones = tope.siguiente
        tope.siguiente = None 
        return tope

    def mostrar_evoluciones(self):
        nombres = [evo.nombre for evo in self]
        if not nombres:
            print("No hay evoluciones.")
            return
        print(" -> ".join(reversed(nombres)))

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)


class IteradorPilaEvoluciones:
    def __init__(self, tope: Evolucion):
        self.actual = tope

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        valor = self.actual
        self.actual = self.actual.siguiente
        return valor