class Evolucion:
    #nodo de la pila que guarda el nombre de la evolucion
    def __init__ (self, nombre: str) :

        self.nombre = nombre
        self.siguiente = None #enlace al nodo de abajo


class PilaEvoluciones:
    #pila con nodos enlazados
    def __init__ (self) :
        
        self.evoluciones = None #tope de la pila, puse None para que la pila este vacia

    def apilar (self, evolucion: Evolucion) :
        #nuevo nodo con el tope actual
        evolucion.siguiente = self.evoluciones
        self.evoluciones = evolucion


    def desapilar (self) :
        #si no hay tope, la pila esta vacia y no tiene nada para sacar
        if self.evoluciones is None :

            return "No hay evoluciones para desapilar"
        
        tope = self.evoluciones #guarda el tope actual
        self.evoluciones = tope.siguiente #nuevo tope
        tope.siguiente = None

        return tope

    def mostrar_evoluciones (self) :
        #recorre la pila usando el iterador
        for nombre in self.evoluciones.nombre :

            print (nombre)

    def __iter__ (self) :
        #usa la pila en un for
        return IteradorPilaEvoluciones (self.evoluciones)


class IteradorPilaEvoluciones :

    def __init__ (self, actual: Evolucion) :
        
        self.actual = actual #nodo en el que esta actualmente el iterador

    def __iter__ (self) :

        return self

    def __next__ (self) :
        #si no hay nodos, avisa al for que termino
        if self.actual is None :

            raise StopIteration 
        
        valor = self.actual #guarda el nodo actual
        self.actual = self.actual.siguiente #siguiente nodo

        return valor


"""Nombre y Apellido: RODRIGO MATIAS LOPEZ
Email: rodlopez003@gmail.com
Comisión: 1"""