class Evolucion:
    def __init__(self, nombre: str):
         self.nombre = nombre
         self.siguiente = None


class PilaEvoluciones:
    def __init__(self)
        self.evoluciones 

    def apilar(self, evolucion: Evolucion):
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion

    def desapilar(self):
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar actualmente."
        tope = self.evoluciones
        self.evoluciones = tope.siguiente
        tope.siguiente = None
        return tope

    def mostrar_evoluciones(self):
        nombres = []
        actual = self.evoluciones
        while actual is not None:
            nombres.append(actual.nombre)
            actual = actual.siguiente
        for nombre in reversed (nombres):
            print(nombre)

    def __iter__(self):
        return IteradorPilaEvoluciones(self.evoluciones)


class IteradorPilaEvoluciones:
    def __init__(self, actual: Evolucion):
        self.actual = actual

    def __iter__ (self):
        if self.actual is None:
            raise StopIteration
            valor = self.actual
            self.actual = self.actual.siguiente
            return valor

if __name__ == "__main__":
    pila = PilaEvoluciones()
    pila.apilar(Evolucion("Charmander"))
    pila.apilar(Evolucion("Charmeleon"))
    pila.apilar(Evolucion("Charizard"))

    print("Orden apilado")
    pila.mostrar_evoluciones
