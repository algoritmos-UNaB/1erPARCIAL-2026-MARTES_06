class Evolucion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# Nodo para enlazar las evoluciones en la pila
Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


Evoluciones:
    def __init__(self):
        self.tope = None
        self.tamano = 0

    def apilar(self, evolucion):
        nuevo_nodo = Nodo(evolucion)
        # El nuevo nodo apunta al que estaba antes arriba
        nuevo_nodo.siguiente = self.tope
        # Ahora el tope de la pila es el nuevo nodo
        self.tope = nuevo_nodo
        self.tamanio += 1
    def desapilar(self):
        # Si la pila no tiene elementos
        if self.tope is None:
            return "No hay evoluciones para desapilar."
        
        # Guardamos el dato que esta arriba para devolverlo
        elemento_eliminado = self.tope.dato
        # Movemos el tope al nodo de abajo
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return elemento_eliminado

    def mostrar_evoluciones(self):
        actual = self.tope
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def __iter__(self):
        # Devuelve el iterador empezando desde el tope actual
   return IteradorPilaEvoluciones(self.tope)


class IteradorPilaEvoluciones:
    def __init__(self, actual):
        self.actual = actual

    def __iter__(self):
        return self

    def __next__(self):
        # Si ya llegamos al final de la pila, corta el for
        if self.actual is None:
            raise StopIteration
        
        # Se toma dato actual y se avanza en el puntero
        valor = self.actual.dato
        self.actual = self.actual.siguiente
        return valor