class Evolucion:
    def __init__(self, nombre: str):
        self.nombre = nombre


class NodoEvolucion:
    #clase auxiliar para construir la estructura lineal enlazada de la pila
    def __init__(self, evolucion: Evolucion):
        self.evolucion = evolucion
        self.siguiente = Nodo


class PilaEvoluciones: 
    def __init__(self):
        self.cima = None #Apunta al nodo superior de la pila

    def apilar(self, evolucion: Evolucion):
        nuevo_nodo = NodoEvolucion(evolucion)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            return "No hay evoluciones para desapilar"

        evolucion_extraida = self.cima.evolucion
        self.cima = self.cima.siguiente
        return evolucion_extraida

    def mostrar_evoluciones(self):
        #para mostrar el orden en que fueron apiladas primero recolectamos los elementos recorriendo la pila
        actual = self.cima
        elementos = []

        while actual is not None:
            elementos.append(actual.evolucion.nombre)
            actual = actual.siguiente

        #invertimos la lista
        for nombre in reversed(elementos):
            print (f "Evolucion: [nombre]")

    def __iter__(self)
         #retorna una nueva instancia apuntando a la cima actual
         return IteradorPilaEvoluciones(self.cima)

class IteradorPilaEvoluciones:
    def __init__(self, self nodo_inicio: NodoEvolucion):
        self.actual = nodo_inicio

    def __next__(self):
        if self.actual is None:
            raise StopIteration

            evolucion_retorno = self.actual.evolucion
            self.actual = self.actual.siguiente
            return evolucion_retorno
         

