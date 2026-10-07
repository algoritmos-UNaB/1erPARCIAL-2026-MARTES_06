class Evolucion:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.siguiente: Evolucion = None

class PilaEvoluciones:
    def __init__(self):
        self.evoluciones: Evolucion = None
    def apilar(self, evolucion: Evolucion):
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion
    def despilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar."
        
        evolucion_desapilada = self.evoluciones
        self.evoluciones = self.evoluciones.siguiente
        evolucion_desapilada.siguiente = None
        return evolucion_desapilado
    def mostrar_evoluciones(self):
        actual = self.evoluciones
        if actual is None:
            print("No hay evoluciones registradas.")
            return

        print("Evoluciones (de la mas reciente a la mas antigua):")
        while actual is not None:
            print(f"- {actual.nombre}")
            actual = actual.siguiente
    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

class IteradorPilaEvoluciones:
    def __init__(self, inicio: Evolucion):
        self.actual: Evolucion = inicio
    def __next__(self) -> Evolucion:
        if self.actual is None:
            raise StopIteration

        evolucion_actual = self.actual
        self.actual = self.actual.siguiente
        return evolucion_actual