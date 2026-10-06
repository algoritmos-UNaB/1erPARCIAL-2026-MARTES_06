class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class PilaEvoluciones:

    def __init__(self):
        """
        Lista enlazada que almacena las evoluciones en orden.
        """
        self.evoluciones = None

    def apilar(self, evolucion):
        """
        Metodo que agrega una evolucion a la pila.
        """
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion

    def desapilar(self):
        """
        Metodo que elimina y devuelve la ultima evolucion agregada a la pila.
        Si la pila esta vacia debe devolver un mensaje indicando que no hay evoluciones para desapilar.
        """
        if self.evoluciones is None:
            return "No hay evoluciones para desapilar"

        desapilada = self.evoluciones
        self.evoluciones = self.evoluciones.siguiente
        return desapilada

    def mostrar_evoluciones(self):
        """
        Metodo que imprime todas las evoluciones en el orden en que fueron apiladas.
        Nota: Queremos recorrer la pila utilizando un ciclo for deberan implementar un Iterador para esta clase.
        """
        evoluciones = [evolucion for evolucion in self]  # tope -> base

        for evolucion in reversed(evoluciones):          # base -> tope
            print(evolucion.nombre)

    def __iter__(self):
        """
        Retorna el iterador.
        """
        return IteradorPilaEvoluciones(self.evoluciones)


class IteradorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        evolucion = self.actual
        self.actual = self.actual.siguiente
        return evolucion
