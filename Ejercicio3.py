class Nodo:
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Evolucion:
    
    def __init__(self, nombre: str):
        self.nombre = nombre

class ListaEnlazada:

    def __init__(self):
        self.primero = None
    
    def esta_vacia(self):
        return self.primero is None

    def insertar_al_inicio(self, dato):
        nuevo = nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def insertar_al_final(self, dato):
        nuevo = nodo(dato)

        if self.primero is None:
            self.primero = nuevo
            return
        actual = self.primero

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def eliminar_al_inicio(self):
        if self.primero is None:
            return None

        dato = self.primero.dato
        self.primero = self.primero.siguiente

        return dato


class PilaEvoluciones:

    def __init__(self):
        self.evoluciones = ListaEnlazada()

    def apilar(self, evolucion):
        self.evoluciones.append(evolucion)

    def desapilar(self):
        if len(self.evoluciones) == 0:
            return "No existen evoluciones para desapilar."

        return self.evoluciones.pop

    def mostrar_evoluciones(self):
        for evolucion in self:
            print(evolucion.nombre)

class IteradorPilaEvoluciones:

    def __init__(self, primero):
        self.actual = primero
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
    
        evolucion = self.actual.dato
        self.actual = self.actual.siguiente

        return evolucion