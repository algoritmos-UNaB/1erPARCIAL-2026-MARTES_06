class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre


class PilaEvoluciones:
    def __init__(self):
        self.evoluciones = None

    def apilar(self, evolucion: Evolucion):
        nuevo_nodo = NodoPila(evolucion)
        nuevo_nodo.siguiente = self.evoluciones
        self.evoluciones = nuevo_nodo
        print(f"Evolucion '{evolucion.nombre}' apilada.")

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar."
        evolucion_a_devolver = self.evoluciones.evolucion   
        self.evoluciones = self.evoluciones.siguiente
        print(f"Evolución '{evolucion_a_devolver.nombre}' desapilada.")
        return evolucion_a_devolver

    def mostrar_evoluciones(self):
        print("\n--- Mostrando Evoluciones (de la más reciente a la más antigua) ---")
        actual = self.evoluciones
        if actual is None:
            print("La pila está vacía.")
            return       
        while actual is not None:
            print(f"- {actual.evolucion.nombre}")
            actual = actual.siguiente

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)

# Si bien la consigna no requiere crear esta clase, creí adecuado hacerla dado que necesitaba un nodo
# que almacene el dato (Evolucion) y un puntero al siguiente nodo
class NodoPila:
    def __init__(self, evolucion: Evolucion):
        self.evolucion = evolucion
        self.siguiente = None


class IteradorPilaEvoluciones:
    def __init__(self, tope_pila):
        self.actual = tope_pila

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        evolucion_actual = self.actual.evolucion
        self.actual = self.actual.siguiente
        return evolucion_actual